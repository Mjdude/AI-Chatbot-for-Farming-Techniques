# Download necessary data for the chatbot


# Create a new chatbot instance
from chatterbot import ChatBot


bot = ChatBot('SimpleBot', read_only=False , logic_adapters=["chatterbot.logic.BestMatch"])