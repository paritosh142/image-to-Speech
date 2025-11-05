import os
import uuid
import streamlit as st
from dotenv import load_dotenv
from transformers import pipeline
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from huggingface_hub import InferenceClient

# ---------- ENV ----------
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACE_API_TOKEN") or os.getenv("HUGGINGFACEHUB_API_TOKEN")

# ---------- CACHED RESOURCES ----------
@st.cache_resource
def get_caption_model():
    # You can switch to a lighter model if RAM is tight:
    # return pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")
    return pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")

@st.cache_resource
def get_story_llm():
    # Gemini 2.5 Flash (fast & cheap)
    return ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

@st.cache_resource
def get_hf_client():
    if not HF_TOKEN:
        return None
    # fal-ai provider serves Kokoro quickly
    return InferenceClient(provider="fal-ai", api_key=HF_TOKEN)

# ---------- FUNCTIONS ----------
def generate_caption(image_path: str) -> str:
    model = get_caption_model()
    result = model(image_path)
    return result[0].get("generated_text", "").strip()

def generate_story(scenario: str) -> str:
    llm = get_story_llm()
    prompt_template = """
    You are a creative storyteller who can craft engaging and imaginative stories from simple narrative.
    Create a story using the scenario provided; the story should have maximum of 50 words.
    Scenario: {scenario}
    Story:
    """
    prompt = PromptTemplate(template=prompt_template, input_variables=["scenario"])
    chain = prompt | llm
    generated = chain.invoke({"scenario": scenario})
    return (generated.content or "").strip()

def kokoro_tts_bytes(text: str) -> bytes | None:
    """
    Generate speech (WAV bytes) from text using Kokoro via HF InferenceClient (fal-ai).
    Returns bytes suitable for st.audio(..., format="audio/wav")
    """
    client = get_hf_client()
    if client is None:
        raise RuntimeError("Hugging Face token not found. Set HF_TOKEN or HUGGINGFACE_API_TOKEN in your .env.")

    # NOTE: 'voice' param is NOT supported by the fal-ai TTS endpoint here
    audio_bytes = client.text_to_speech(text, model="hexgrad/Kokoro-82M")
    if not audio_bytes or len(audio_bytes) < 100:
        return None
    return audio_bytes

# ---------- STREAMLIT APP ----------
def main():
    st.set_page_config(page_title="IMG2SPEECH", page_icon=":robot_face:")
    st.title("Image → Story → Speech :robot_face:")
    st.write("Upload an image, and let the AI generate a caption, turn it into a short story, and read it aloud — all here.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        os.makedirs("img", exist_ok=True)

        ext = uploaded_file.name.split(".")[-1]
        file_path = os.path.join("img", f"{uuid.uuid4()}.{ext}")

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getvalue())

        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # 1) Caption
        with st.spinner("Generating caption..."):
            try:
                caption = generate_caption(file_path)
            except Exception as e:
                st.error(f"Error generating caption: {e}")
                return

        st.subheader("🖼️ Generated Caption")
        st.write(caption or "(empty)")

        # 2) Story
        with st.spinner("Crafting a short story..."):
            try:
                story = generate_story(caption)
            except Exception as e:
                st.error(f"Error generating story: {e}")
                return

        st.subheader("📖 Generated Story")
        st.write(story or "(empty)")

        # 3) Speech (play directly, no file saved)
        with st.spinner("Generating speech with Kokoro..."):
            try:
                audio_bytes = kokoro_tts_bytes(story)
            except Exception as e:
                st.error(f"Error generating speech: {e}")
                audio_bytes = None

        if audio_bytes:
            st.subheader("🔊 Listen")
            # Streamlit can play bytes directly; declare format so it renders a player
            st.audio(audio_bytes, format="audio/wav")
            # Optional: also expose a download button
            st.download_button("Download WAV", data=audio_bytes, file_name="story.wav", mime="audio/wav")
        else:
            st.warning("Could not generate audio. Check your HF token, network, or try again.")

if __name__ == "__main__":
    main()
