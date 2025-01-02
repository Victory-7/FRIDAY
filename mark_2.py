import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import datetime
import os
import sys
import smtplib
from transformers import pipeline
from helpers import speak, takeCommand, weather, cpu, joke, screenshot  # Modularized helpers
import json
from textblob import TextBlob
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import schedule
import time

# Initialize Text-to-Speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Load NLP model for adaptability
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")
sentiment_analyzer = pipeline("sentiment-analysis")

def spell_correct(input_text):
    blob = TextBlob(input_text)
    return str(blob.correct())

class FridayAI:
    def __init__(self):
        self.user_data = self.load_user_data()
        self.init_web_browser()

    def init_web_browser(self):
        if sys.platform.startswith("linux"):
            self.chrome_path = '/usr/bin/google-chrome'
        elif sys.platform == "darwin":
            self.chrome_path = 'open -a /Applications/Google\\ Chrome.app'
        elif sys.platform.startswith("win"):
            self.chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
        else:
            print('Unsupported OS')
            exit(1)
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(self.chrome_path))

    def load_user_data(self):
        try:
            with open('user_data.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_user_data(self):
        with open('user_data.json', 'w') as file:
            json.dump(self.user_data, file)

    def wish_user(self):
        hour = int(datetime.datetime.now().hour)
        if hour < 12:
            greet = "Good Morning"
        elif hour < 18:
            greet = "Good Afternoon"
        else:
            greet = "Good Evening"

        speak(f"{greet}, {self.user_data.get('name', 'Suhani')}! How can I assist you today?")

    def interpret_query(self, query):
        query = spell_correct(query)
        sentiment = sentiment_analyzer(query)[0]
        if sentiment['label'] == 'NEGATIVE':
            speak("I sense some negativity. I'm here to help if you need me.")
        
        # Integrate NLP model for open-ended queries
        if 'search' in query or 'find' in query:
            speak('What would you like me to search for?')
            search_query = takeCommand()
            url = f'https://google.com/search?q={search_query}'
            webbrowser.get('chrome').open_new_tab(url)
            speak(f"Here are the results for {search_query}.")

        elif 'news' in query:
            speak('Fetching the latest news...')
            # Placeholder for news function
            speak("Here's the top headline: ...")

        elif 'remember' in query:
            speak("What should I remember?")
            memory = takeCommand()
            self.user_data['memory'] = memory
            self.save_user_data()
            speak(f"I will remember this: {memory}.")

        elif 'recall' in query or 'remember anything' in query:
            memory = self.user_data.get('memory', 'I do not have anything to recall.')
            speak(memory)

        elif 'chat' in query or 'talk' in query:
            speak('Sure! Let\'s talk. What\'s on your mind?')
            user_input = takeCommand()
            response = chatbot(user_input)
            speak(response[0]['generated_text'])

        else:
            speak("I'm not sure how to handle that request. I'm learning every day!")

    def handle_command(self, command):
        if 'wikipedia' in command:
            speak('Searching Wikipedia...')
            command = command.replace('wikipedia', '')
            results = wikipedia.summary(command, sentences=2)
            speak(results)
        elif 'open youtube' in command:
            webbrowser.get('chrome').open_new_tab('https://youtube.com')
        elif 'play music' in command:
            os.startfile("D:\\Music\\favorite.mp3")
        elif 'time' in command:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {current_time}.")
        elif 'set reminder' in command:
            speak("What reminder would you like to set?")
            reminder = takeCommand()
            speak("When should I remind you?")
            time_str = takeCommand()
            self.schedule_reminder(reminder, time_str)
        else:
            self.interpret_query(command)

    def schedule_reminder(self, reminder, time_str):
        def reminder_function():
            speak(f"Here is your reminder: {reminder}")

        schedule.every().day.at(time_str).do(reminder_function)
        speak(f"Reminder set for {time_str}")

    def proactive_checks(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

    def start(self):
        self.wish_user()
        while True:
            command = takeCommand().lower()
            if 'exit' in command or 'shutdown' in command:
                speak("Goodbye! Have a great day.")
                self.save_user_data()
                sys.exit()
            else:
                self.handle_command(command)

if __name__ == '__main__':
    assistant = FridayAI()
    assistant.start()
