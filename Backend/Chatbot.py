from groq import Groq # Importing the Groq library to use its
from json import load, dump # Importing functions to read and
import datetime # Importing the datetime module for real-time
from dotenv import dotenv_values # Importing dotenv_ values to

# Load environment variables from the . env file.
env_vars = dotenv_values(".env")


write JSON files.
date and time information.
read environment variables from a
env file.

.env")
env vars
# Retrieve speci fic environment variables for username,
Username =  env_vars.get("")
Assistantname = env_vars.get("Assistantname")
GroqAPIKey = env_vars.get("GroqAPIKey")


# Initialize the Groq client using the provided API key.
- Groq(api_key=GroqAPIKey)
client
# Initialize an empty list to store chat messages.
messages
assistant name,
and API key.
# Define a system message that provides context to the AI chatbot about its rote and behavior.
System