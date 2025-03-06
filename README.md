# Python-project
## Chatbot Using Python

# KTM Information Bot

## Project Overview

This project is a simple and interactive Python-based bot designed to fetch and provide information about KTM motorcycles using the Embedchain library. The bot sources data from web pages and YouTube videos and answers user queries based on the gathered content.

## Technologies Used

Python: The core programming language.

Embedchain: A powerful library for building knowledge-based apps.

OS Module: To manage environment variables.

How It Works

Setting up API Key:

The OPEN_API_KEY is required and stored securely in the environment variable.

Creating the Bot:

KTM_bot = App() initializes an instance of the App class from the Embedchain library.

Adding Data Sources:

KTM_bot.add("web_page", "<URL>") adds knowledge from the specified web pages.

KTM_bot.add("youtube_video", "<URL>") fetches information from a YouTube video.

Querying Information:

response = KTM_bot.query("who is founder of KTM") sends a query to the bot.

print(response) displays the response based on the gathered knowledge.



