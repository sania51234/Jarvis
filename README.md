# Jarvis

This is a voice-controlled personal assistant inspired by Iron Man's "Jarvis." It can open websites, play music from a predefined library, read out the latest news, and interact with OpenAI's GPT to answer questions or perform tasks.

## Features

- **Voice Commands**: Use your voice to open websites like Google, Facebook, YouTube, and LinkedIn.
- **Music Playback**: Request songs from a predefined library and Jarvis will play them using web links.
- **Latest News**: Get the latest headlines from India using the News API.
- **OpenAI Integration**: Ask Jarvis general questions or request tasks to be performed via OpenAI's GPT-3.5-turbo model.
- **Text-to-Speech**: Responses are read out loud using `gTTS` (Google Text-to-Speech) and played via `pygame`.

## Requirements

Make sure you have the following dependencies installed:

```bash
pip install speechrecognition pyttsx3 gtts pygame requests openai
```
# Getting Started

```bash
git clone https://github.com/yourusername/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```
## Setup OpenAI and News API Keys:
You will need API keys for both OpenAI and the News API.

Get your OpenAI API key from OpenAI's platform.
Get your News API key from NewsAPI.
Once you have them, replace <Your Key Here> in the code with your actual keys.

# Run the Program
```bash
python main.py
```
Jarvis will initialize, and you can interact with it using voice commands. Speak "Jarvis" to activate it, and then give your command.

# Commands
- **Website Navigation**: You can ask Jarvis to open websites like Google, YouTube, Facebook, or LinkedIn.
Example: "Jarvis, open Google."

- **Music Playback**: Request a song from your predefined library.
Example: "Jarvis, play [song name]."

- **News**: Ask for the latest news headlines.
Example: "Jarvis, tell me the news."

- **General AI Questions**:Ask anything you would normally ask an AI-powered assistant.


# Future Improvements
- Adding support for more websites and services.
- Extending the predefined music library to include streaming services like Spotify.
- Adding more complex AI tasks with OpenAI's models.Example: "Jarvis, what is the capital of France?"


