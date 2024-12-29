import openai
from datetime import datetime
import json
import pyttsx3
import speech_recognition as sr
from pathlib import Path
import os

# Initialize FRIDAY AI
class FridayAI:
    def __init__(self, name="FRIDAY", personality="INTJ", version="1.0"):
        self.name = name
        self.personality = personality
        self.version = version
        self.tasks = []  # List to manage tasks
        self.memory = {}  # Memory to store user-specific data
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.personality_data = {}
        self.knowledge_base = {}
        self.functional_responses = {}

        self.load_datasets()

    def load_datasets(self):
        """Load datasets from text files."""
        try:
            with open('personality.txt', 'r') as file:
                self.personality_data = json.load(file)
            with open('knowledge_base.txt', 'r') as file:
                self.knowledge_base = json.load(file)
            with open('functional_responses.txt', 'r') as file:
                self.functional_responses = json.load(file)
        except Exception as e:
            print(f"Error loading datasets: {e}")

    def speak(self, text):
        """Convert text to speech."""
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        """Listen to the user's voice input and convert it to text."""
        with sr.Microphone() as source:
            self.speak("Listening...")
            try:
                audio = self.recognizer.listen(source)
                return self.recognizer.recognize_google(audio)
            except sr.UnknownValueError:
                return "I couldn't understand that. Please repeat."
            except sr.RequestError:
                return "Speech service is unavailable."

    def introduce(self):
        return self.personality_data.get("responses", {}).get("greeting", f"Hello! I am {self.name}, your AI assistant.")

    def chat(self, prompt):
        """Simulates a conversational response using OpenAI's GPT model."""
        return self.chat_with_gpt(prompt)

    def chat_with_gpt(self, prompt):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": f"You are an AI assistant named {self.name} with an {self.personality} personality."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def add_task(self, task):
        """Add a task to FRIDAY's task list."""
        self.tasks.append({"task": task, "added_on": datetime.now()})
        return f"Task '{task}' added successfully."

    def list_tasks(self):
        """List all tasks."""
        if not self.tasks:
            return "No tasks found."
        return "\n".join([f"{i + 1}. {task['task']} (Added on {task['added_on']})" for i, task in enumerate(self.tasks)])

    def prioritize_tasks(self):
        """Suggest a priority task based on time or importance."""
        if not self.tasks:
            return "You have no tasks to prioritize."
        return f"I suggest focusing on: {self.tasks[0]['task']}"

    def remember(self, key, value):
        """Store user-specific data in memory."""
        self.memory[key] = value
        return f"I've remembered this: {key} = {value}"

    def recall(self, key):
        """Recall user-specific data."""
        return self.memory.get(key, "I don't remember that yet.")

    def generate_code(self, description):
        """Placeholder for self-coding functionality using GPT."""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert AI coder."},
                    {"role": "user", "content": f"Write code for: {description}"}
                ]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def access_files(self, directory="."):
        """List files in a given directory."""
        try:
            files = os.listdir(directory)
            return "\n".join(files) if files else "No files found."
        except Exception as e:
            return f"Error accessing files: {str(e)}"

# Initialize FRIDAY instance
friday = FridayAI()

# Voice-based chat interface
friday.speak(friday.introduce())

while True:
    user_input = friday.listen()
    if user_input.lower() in ["exit", "quit", "bye"]:
        friday.speak(friday.personality_data.get("responses", {}).get("farewell", "Goodbye! See you soon."))
        break

    elif user_input.lower().startswith("add task"):
        task = user_input[9:].strip()
        if task:
            response = friday.add_task(task)
            friday.speak(response)
        else:
            friday.speak("Please specify the task to add.")

    elif user_input.lower() == "list tasks":
        response = friday.list_tasks()
        friday.speak(response)

    elif user_input.lower() == "prioritize task":
        response = friday.prioritize_tasks()
        friday.speak(response)

    elif user_input.lower().startswith("remember"):
        parts = user_input[8:].split("=", 1)
        if len(parts) == 2:
            key, value = parts[0].strip(), parts[1].strip()
            response = friday.remember(key, value)
            friday.speak(response)
        else:
            friday.speak("Please provide the data in 'remember key = value' format.")

    elif user_input.lower().startswith("recall"):
        key = user_input[6:].strip()
        response = friday.recall(key)
        friday.speak(response)

    elif user_input.lower().startswith("generate code"):
        description = user_input[13:].strip()
        if description:
            response = friday.generate_code(description)
            friday.speak("Code generated. Check the output console.")
            print("FRIDAY:\n", response)
        else:
            friday.speak("Please describe the code you want me to generate.")

    elif user_input.lower().startswith("access files"):
        directory = user_input[12:].strip() if len(user_input) > 12 else "."
        response = friday.access_files(directory)
        friday.speak("Here are the files.")
        print("FRIDAY:\n", response)

    else:
        response = friday.chat(user_input)
        friday.speak(response)
        print("FRIDAY:", response)
