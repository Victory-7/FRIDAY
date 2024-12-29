# FRIDAY AI

FRIDAY AI is an advanced, modular AI assistant inspired by JARVIS from *Iron Man* and enhanced with the INTJ personality type. Designed to assist with tasks, manage memory, and provide insightful and conversational responses, FRIDAY is an all-in-one virtual assistant powered by OpenAI's GPT and customizable datasets.

---

## Features

### 1. **Conversational AI**
   - Natural language understanding and responses.
   - OpenAI GPT integration for dynamic conversations.

### 2. **Task Management**
   - Add, list, and prioritize tasks.
   - Memory storage for recalling user-specific data.

### 3. **Dynamic Personality**
   - Loaded with an INTJ personality dataset.
   - Configurable to adapt to other personality types.

### 4. **Knowledge Base**
   - Pre-loaded with technical and general knowledge.
   - Customizable knowledge datasets for personalization.

### 5. **Functional Modules**
   - File management (list, access directories).
   - Self-coding capabilities (generate and debug code).

### 6. **Voice Interaction**
   - Speech recognition for user commands.
   - Text-to-speech functionality for responses.

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/FRIDAY-AI.git
   cd FRIDAY-AI
   ```

2. **Install Dependencies**
   make sure you have Python 3.8 or higher installed.
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare Datasets**
   Create the following text files in the root directory:
   - `personality.txt`
   - `knowledge_base.txt`
   - `functional_responses.txt`

   Could you populate these files with your desired content (examples provided in the repository)?

4. **Run FRIDAY AI**
   ```bash
   python friday_ai_starter.py
   ```

---

## Usage

- Interact with FRIDAY via text or voice commands.
- Add tasks using the command: `add task [task description]`.
- Generate code by describing your requirements: `generate code [description]`.
- Manage memory with commands like `remember [key=value]` and `recall [key]`.
- End the session by saying: `exit`, `quit`, or `bye`.

---

## Roadmap

- [ ] Advanced learning capabilities with NLP.
- [ ] GUI development using PyQt or Flask.
- [ ] Integration with external APIs (e.g., Google Calendar, IoT devices).
- [ ] Vision module for face/object recognition.
- [ ] Deployment via Docker or on cloud services.

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a pull request.

---


## Acknowledgments

- Inspired by JARVIS from *Iron Man*.
- Built with OpenAI GPT for conversational abilities.
- Voice functionality powered by `pyttsx3` and `SpeechRecognition`.

---

## Contact

- **Developer**: Suhani Verma
- **Location**: Rajasthan, India
- **Email**: victory.xmas@gmail.com

Feel free to reach out for collaborations or inquiries!
