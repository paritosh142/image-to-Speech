from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
scenario = "A cat exploring a futuristic city"

prompt_template = """
You are a creative storyteller who can craft engaging and imaginative stories from simple narrative.
Create a story using the scenario provided; the story should have maximum of 50 words.
Scenario: {scenario}
Story:
"""

prompt = PromptTemplate(template=prompt_template, input_variables=["scenario"])

# Use the new Runnable API instead of LLMChain
chain = prompt | llm

generated_story = chain.invoke({"scenario": scenario})

# print(f"input Scenario: {scenario}")
print("Generated Story:", generated_story.content)
