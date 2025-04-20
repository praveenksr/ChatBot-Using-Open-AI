import os
from embedchain import App
from config import OPENAI_API_KEY

# Set the API key for Embedchain
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Create the chatbot
KTM_BOT = App()

# Add content sources
KTM_BOT.add("web_page", "https://en.wikipedia.org/wiki/KTM")
KTM_BOT.add("web_page", "https://www.ktmindia.com/ktm-bikes/naked-bike/ktm-200-duke")
KTM_BOT.add("youtube_video", "https://youtu.be/v4xoIJGS7bI?si=de24Yw9mgBxt_9x2")

# User input
question = input("Ask me anything about KTM: ")
response = KTM_BOT.query(question)
print("\n🔸 Answer:", response)
