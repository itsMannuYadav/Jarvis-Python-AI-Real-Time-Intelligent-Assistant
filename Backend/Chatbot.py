from groq import Groq # Importing the Groq library to use its API.
from json import load, dump # Importing functions to read and write JSON files.
import datetime # Importing the datetime module for real-time date and time information.
from dotenv import dotenv_values # Importing dotenv_ values to read environment variables from a .env file.

# Load environment variables from the . env file.
env_vars = dotenv_values(".env")

# Retrieve speci fic environment variables for username, assistant name, and API key.
Username =  env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")
GroqAPIKey = env_vars.get("GroqAPIKey")


# Initialize the Groq client using the provided API key.
client = Groq(api_key=GroqAPIKey)

# Initialize an empty list to store chat messages.
messages = []

# Define a system message that provides context to the AI chatbot about its rote and behavior.
System = """"""

# A list of system instructions for the chatbot.
SystemChatBot = [
    {"role": "system", "content": System}
]

# Attempt to load the chat log from a JSON file.
try:
    with open(r"Data\ChatLog.json", "r") as f:
        messages= load(f)  # Load existing messages from the chat log.
except FileNotFoundError:
# If the file doesn't exist, create an empty JSON file to store chat logs.
    with open(r"Data\ChatLog.json", "w") as f:
        dump([],f)

# Function to get real-time date and time information.
def Realtimelnformation():
    current_date_time = datetime.datetime.now()  #Get the current date and time.
    day = current_date_time.strftime("%A") #Day of the week
    date = current_date_time.strftime("%d") # Day of the month.
    month = current_date_time.strftime("%B")  # Full month name.
    year = current_date_time.strftime("%Y")  # Year.
    hour = current_date_time.strftime( "%H" )  # Hour in 24-hour format
    minute = current_date_time.strftime( "%M" )  # Minute.
    second = current_date_time.strftime("%S")  # Second.


    # Format the information into a string.
    data = f"Please use this real-time information if needed,\n"  
    data += f"Day: {day}\nDate: {date}\nMonth: {month}\nYear: {year}\n"
    data += f" Time: {hour} hours : {minute} minutes : {second} seconds.\n"
    return data    
    
    # Function to modify the chatbot's response for better formatting.
    def AnswerModifier(Answer):
        lines = Answer.split( '\n')  # Split the response into lines.
        non_empty_lines = [line for line in lines if line. strip()]
        