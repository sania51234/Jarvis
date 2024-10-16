import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
import asyncio
import signal

recognizer = sr.Recognizer()
engine = pyttsx3.init() 
newsapi = "<Your Key Here>"

# Asynchronous speak function using gTTS and Pygame
async def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load and play the MP3 file asynchronously
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()

    # Wait until the music stops playing asynchronously
    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)  # Yield control to the event loop

    pygame.mixer.music.unload()
    os.remove("temp.mp3")

# Async OpenAI call
async def aiProcess(command):
    client = OpenAI(api_key="<Your Key Here>")

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please."},
            {"role": "user", "content": command}
        ]
    )
    
    return completion.choices[0].message.content

# Handle music playback and commands
async def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
        else:
            await speak("Sorry, I couldn't find that song.")
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Speak out the headlines
            for article in articles:
                await speak(article['title'])
        else:
            await speak("Sorry, I couldn't fetch the news at the moment.")
    else:
        # Let OpenAI handle the request
        output = await aiProcess(c)
        await speak(output)

# Graceful shutdown for pygame mixer
def shutdown(signal, frame):
    print("\nShutting down Jarvis...")
    pygame.mixer.quit()
    exit(0)

signal.signal(signal.SIGINT, shutdown)

# Main function to handle listening and processing commands
async def main():
    await speak("Initializing Jarvis....")
    
    while True:
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Listening for wake word 'Jarvis'...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)
                word = recognizer.recognize_google(audio)

                if word.lower() == "jarvis":
                    await speak("Hey! What can I help you with?")
                    with sr.Microphone() as source:
                        print("Jarvis Active, listening for command...")
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)
                        await processCommand(command)

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"Error: {e}")

# Entry point of the program
if __name__ == "__main__":
    pygame.mixer.init()  # Initialize pygame mixer globally
    asyncio.run(main())
