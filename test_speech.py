# test_kokoro_inference.py
import os
import uuid
from pathlib import Path
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

def get_hf_token():
    load_dotenv()
    return (
        os.getenv("HF_TOKEN")
        or os.getenv("HUGGINGFACE_API_TOKEN")
        or os.getenv("HUGGINGFACEHUB_API_TOKEN")
    )

def save_audio_bytes(wav_bytes: bytes, out_path: str) -> str:
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(wav_bytes)
    return out_path

def kokoro_tts(text: str, filename: str | None = None):
    """
    TTS with Kokoro served via fal-ai provider using Hugging Face InferenceClient.
    Returns path to saved audio (wav).
    """
    token = get_hf_token()
    if not token:
        raise RuntimeError("HF token not found. Set HF_TOKEN or HUGGINGFACE_API_TOKEN in .env")

    client = InferenceClient(provider="fal-ai", api_key=token)

    print("⏳ Requesting audio from Kokoro (hexgrad/Kokoro-82M) via fal-ai...")
    # no 'voice' arg – only text and model
    audio_bytes = client.text_to_speech(
        text,
        model="hexgrad/Kokoro-82M"
    )

    if not audio_bytes or len(audio_bytes) < 100:
        raise RuntimeError("Empty or too-small audio reply. Try again or change provider/model.")

    if filename is None:
        filename = f"kokoro_{uuid.uuid4().hex}.wav"

    out_path = save_audio_bytes(audio_bytes, filename)
    print(f"✅ Saved: {out_path}")
    return out_path


if __name__ == "__main__":
    TEXT = (
        
        "Aur Haan Meri tatti to sirf meri tatti hai kisi aur ki tatti nahi to tu he meri tatti kha kisi aur ko mt bol meri tatti khane ko aur agar meri tatti se moossk aaye to  naak bnd krke kha leo pr tujhe meri tatti abhi aur isi waqt khani hogi aur mujhe meri tatti ki rating bhe deni pdegi terko"
    )
    try:
        path = kokoro_tts(TEXT)
        print("▶️ Play the WAV file to hear the result.")
    except Exception as e:
        print("❌ TTS failed:", e)

