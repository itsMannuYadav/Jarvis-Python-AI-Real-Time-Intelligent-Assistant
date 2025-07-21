# Jarvis Python AI Real Time Intelligent Assistant

![Jarvis Banner](Frontend/Graphics/banner.png)

## Overview
Jarvis is a powerful, real-time, intelligent assistant built with Python. It combines advanced AI models, real-time search, automation, and a modern GUI to help you with daily tasks, answer questions, generate images, and much more—all in one place.

---

## Features
- **Conversational AI**: Chat with Jarvis using natural language, powered by Cohere and Groq LLMs.
- **Real-Time Search**: Get up-to-date information from Google, YouTube, and the web.
- **Automation**: Open/close apps, set reminders, play music, and more.
- **Image Generation**: Create images from text prompts using AI.
- **Speech Recognition & Synthesis**: Talk to Jarvis and get spoken responses.
- **Modern GUI**: User-friendly interface built with PyQt5.
- **Persistent Chat Logs**: All conversations are saved for future reference.
- **Secure API Key Management**: Uses a `.env` file for sensitive keys (never committed to the repo).

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/itsMannuYadav/Jarvis-Python-AI-Real-Time-Intelligent-Assistant.git
   cd Jarvis-Python-AI-Real-Time-Intelligent-Assistant
   ```

2. **Install dependencies:**
   ```bash
   pip install -r Requirements.txt
   ```

3. **Set up environment variables:**
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Fill in your API keys and configuration in `.env`.

4. **Run the application:**
   ```bash
   python Main.py
   ```

---

## Project Structure
```
Main.py
Requirements.txt
.env.example
Backend/
    Automation.py
    Chat.py
    ImageGeneration.py
    Model.py
    RealtimeSearchEngine.py
    SpeechToText.py
    TextToSpeech.py
Data/
Frontend/
    GUI.py
    Files/
    Graphics/
```

---

## Usage
- **Start Jarvis**: Run `python Main.py` and interact via the GUI or terminal.
- **Chat**: Ask questions, get real-time info, or automate tasks.
- **Image Generation**: Use prompts like "generate image of a cat".
- **Automation**: Try commands like "open notepad", "set a reminder at 9pm".

---

## Environment Variables
Sensitive information is stored in a `.env` file (not tracked by git). See `.env.example` for required variables:
- `CohereAPIKey`
- `GroqAPIKey`
- `Username`
- `Assistantname`

---

## Security
- **Never share your real `.env` file.**
- API keys are required for full functionality. If you lose your `.env`, generate new keys from the provider dashboards.

---

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## License
This project is licensed under the MIT License.

---

## Acknowledgements
- [Cohere](https://cohere.com/)
- [Groq](https://groq.com/)
- [PyQt5](https://riverbankcomputing.com/software/pyqt/)
- [Other open-source libraries](Requirements.txt)

---

## Screenshots
![Jarvis GUI](Frontend/Graphics/screenshot1.png)

---

## Contact
Created by Mannu Yadav. For questions, reach out via GitHub Issues or email (see profile).
