# FRIDAY

> **A local AI-powered desktop assistant built with Python, Ollama, and a custom web-based interface.**

FRIDAY is a personal desktop AI assistant designed to interact with the user, understand commands, perform system-level actions, and provide AI-powered responses — all while running locally.

The project is being developed as a learning and experimentation project focused on **Artificial Intelligence, automation, local LLMs, and desktop applications**.

---

## ✨ Features

### 🤖 Local AI

* Uses **Ollama** to run Large Language Models locally.
* Supports conversational AI without relying entirely on cloud APIs.
* Uses a dedicated intent-routing system to determine what the user wants.

### 🧠 Intelligent Routing

FRIDAY separates commands from normal conversations using an AI-based router.

For example:

```text
User → "Open Chrome"
       ↓
Intent Router
       ↓
open_app
       ↓
Chrome launches
```

While a normal question can be routed to the conversational model.

### 🖥️ Desktop Automation

Current system-level capabilities include:

* Opening applications
* Handling time and date requests
* Executing supported system actions
* Conversational interaction

More automation capabilities are being added as development continues.

### 🎨 Custom User Interface

FRIDAY is being developed with a custom **HTML, CSS, and JavaScript interface** instead of relying on a traditional command-line interface.

The goal is to provide a modern desktop-assistant experience while keeping the existing Python AI backend.

---

## 🏗️ Architecture

The current architecture is roughly:

```text
                    ┌───────────────┐
                    │     USER      │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │   FRIDAY UI   │
                    │ HTML/CSS/JS   │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Python Backend│
                    └───────┬───────┘
                            │
                   ┌────────┴────────┐
                   ▼                 ▼
             ┌───────────┐     ┌───────────┐
             │  Intent   │     │ Convers-  │
             │  Router   │     │ ational   │
             │ Gemma 3   │     │ Qwen 3    │
             └─────┬─────┘     └───────────┘
                   │
                   ▼
             ┌─────────────┐
             │   Actions   │
             │ Windows API │
             └─────────────┘
```

---

## 🧰 Tech Stack

### Backend

* **Python**
* **Ollama**
* **Gemma 3 4B** — intent routing
* **Qwen 3 4B** — conversational responses

### Frontend

* **HTML**
* **CSS**
* **JavaScript**

### AI / ML

* Local Large Language Models
* Intent classification
* Natural language processing
* Local inference

### Other

* Windows automation
* Git & GitHub

---

## 📂 Project Structure

```text
FRIDAY/
│
├── backend/
│   ├── main.py
│   ├── router.py
│   └── ...
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── Models/
│   └── ...
│
├── README.md
└── .gitignore
```

> The exact structure may change as the project evolves.

---

## ⚙️ Requirements

Before running FRIDAY, make sure you have:

* Windows
* Python 3.x
* Ollama
* Git
* A system capable of running the selected local models

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Install and pull the required Ollama models:

```bash
ollama pull gemma3:4b
ollama pull qwen3:4b
```

---

## 🚀 Running FRIDAY

### 1. Clone the repository

```bash
git clone https://github.com/SuryaChauhan123/FRIDAY.git
cd FRIDAY
```

### 2. Start Ollama

Make sure Ollama is running on your system.

### 3. Start FRIDAY

Run the Python backend using the project's entry point:

```bash
python main.py
```

### 4. Open the interface

The web-based interface can be opened through the project's frontend entry point.

> Setup instructions will be updated as the frontend/backend integration is finalized.

---

## 🧪 Current Development Status

FRIDAY is an **active work-in-progress project**.

### Currently working

* [x] Local LLM integration
* [x] Ollama integration
* [x] AI intent routing
* [x] Application launching
* [x] Time/date functionality
* [x] Conversational AI
* [x] End-to-end execution
* [ ] Final web UI integration
* [ ] Application closing
* [ ] Expanded system controls
* [ ] Improved error handling
* [ ] Voice interaction
* [ ] Production-ready packaging

### Voice

FRIDAY previously included **Kokoro TTS**, but voice output is currently not operational and is being worked on separately.

---

## 🎯 Future Plans

Some planned improvements include:

* [ ] Complete desktop UI
* [ ] Voice input and output
* [ ] Application management
* [ ] System monitoring
* [ ] More Windows automation
* [ ] Better conversational memory
* [ ] Custom wake word
* [ ] Desktop notifications
* [ ] Improved response speed
* [ ] Packaged desktop application
* [ ] More intelligent task execution

---

## 💡 Why FRIDAY?

The project started as an experiment to understand how local AI models can interact with a computer rather than simply generating text.

The long-term goal is to develop FRIDAY into a more capable **local AI desktop assistant** that can understand natural-language commands and perform useful tasks on the user's system.

---

## 📸 Screenshots

Screenshots and a demonstration video will be added as the interface develops.

---

## 👨‍💻 Author

**Surya**

First-year B.Tech student interested in:

* Artificial Intelligence & Machine Learning
* Python
* Local LLMs
* Automation
* Web Development

---

## 📜 License

This project is currently intended as a personal learning and development project.

License information will be added as the project matures.
