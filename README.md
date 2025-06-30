# Prompt-to-Pin: An LLM Agent That Programs Arduino from Natural Language

## 📁 Project Structure

```
prompt-to-pin/
├── agent.py               # Main Strand-based CLI agent
├── README.md              # Project documentation
├── assets/
│   └── demo.gif           # Demo recording
├── requirements.txt       # Dependencies
└── LICENSE
```

---

## 📦 Installation Instructions

```bash
# 1. Clone the repo
$ git clone https://github.com/tumratde/prompt-to-pin.git
$ cd prompt-to-pin

# 2. Create a virtual environment
$ python3 -m venv prompt-env
$ source prompt-env/bin/activate

# 3. Install dependencies
$ pip install -r requirements.txt

# 4. Install Arduino CLI and MCP-Server
$ brew install arduino-cli
$ uvx install mcp-arduino-server@latest
```

---

## 🚀 Usage

```bash
$ python agent.py
```

**Example Prompt:**
```
Blink an LED on pin 13 every second. Send "tick" over serial.
```

The agent will:
- Generate a complete Arduino sketch
- Compile it
- Upload it to your connected Arduino
- Open a serial monitor automatically (macOS only)

---

## 🎥 Demo

![Demo](assets/demo.gif)

---

## ✨ Features
- Strand SDK + MCP toolchain
- Claude via Amazon Bedrock for sketch generation
- Auto board detection and port usage
- Serial monitor auto-launch (macOS)
- Clear response summaries

---

## 🤖 Tech Stack
- **Strand SDK** for agent framework
- **Claude (via Amazon Bedrock)** for LLM
- **MCP + mcp-arduino-server** to compile, upload, and monitor Arduino
- **Arduino CLI** to interface with boards

---

## 📄 License
MIT License