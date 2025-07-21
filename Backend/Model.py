import cohere #Import the Cohere library for AI services
from rich import print # Imnort the Rich Library to enhance terminal outputs.
from dotenv import dotenv_values #Import dotenv to load environment variables from a .env file


# Load environment variables from the .env file.
env_vars = dotenv_values(".env")

# Retrieve API Key
CohereAPIKey = env_vars.get("CohereAPIKey")

# Create a Cohore client using the provided API Key.
co = cohere.C1ient(api_key=CohereAPIKey)

# Define a list of recognized function keywords for task categorization.
funcs = ["exit", "general", "realtime", "open", "close", "play",
         "generate image", "system", "content", "google search",
         "youtube search","reminder"
         ]
