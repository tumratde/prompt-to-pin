<p align="center">
  <img src="./assets/Arduino_AI_Agent.png" alt="Prompt to Pin Banner" width="600"/>
</p>


# Prompt-to-Pin: An AI-Powered Arduino Agent Built with Strands Agent SDK

> **A showcase of modern GenAI architecture using Strands SDK, MCP protocol, and Claude 3.5 to bridge natural language and embedded systems programming.**

## 🎯 Project Overview

Imagine telling an AI: "Blink the onboard LED every second and show a log for each blink." ...and it writes the code, compiles it, uploads it to your Arduino, and even opens the serial monitor — all from one prompt.

Prompt-to-Pin demonstrates advanced GenAI agent architecture by creating an intelligent system that translates natural language descriptions into working Arduino code. This project showcases:

- **Agent-based AI Architecture** using Strands SDK
- **Model Context Protocol (MCP)** for tool integration
- **Large Language Model Integration** with Claude via Amazon Bedrock
- **End-to-end automation** from prompt to deployed embedded code

## 🏗️ Architecture Benefits

### **Strands SDK Framework**
- **Structured Agent Design**: Leverages Strand's conversation management and tool orchestration
- **Async Processing**: Handles multiple operations (compile, upload, monitor) efficiently
- **Error Handling**: Built-in retry mechanisms and graceful failure recovery
- **Extensible**: Easy to add new tools and capabilities

### **MCP Protocol Integration**
- **Standardized Tool Interface**: Uses Model Context Protocol for seamless LLM-tool communication
- **Modular Architecture**: Arduino operations abstracted into reusable MCP server
- **Type Safety**: Structured data exchange between agent and hardware tools
- **Scalable**: Can easily integrate additional MCP servers for other microcontrollers

### **Claude 3.5 + Bedrock Integration**
- **Advanced Code Generation**: Leverages Claude's superior coding capabilities
- **Context Awareness**: Maintains conversation state for iterative development
- **AWS Integration**: Production-ready deployment through Bedrock
- **Cost Optimization**: Efficient token usage through structured prompting

## 🚀 Key Benefits

### **For Developers**
- **Rapid Prototyping**: From idea to working hardware in seconds
- **Learning Tool**: Understand Arduino programming through natural language exploration
- **Debugging Assistant**: Get explanations and fixes for hardware issues

### **For Education**
- **Accessibility**: Makes embedded programming accessible to non-programmers
- **Interactive Learning**: Learn by describing what you want to achieve
- **Instant Feedback**: See results immediately on physical hardware

### **For Industry**
- **Proof of Concept**: Demonstrates GenAI application in embedded systems
- **Automation Pipeline**: Shows end-to-end automation capabilities
- **Modern Architecture**: Uses latest GenAI patterns and protocols

## 📁 Project Structure

```
prompt-to-pin/
├── agent.py               # Main Strands-based CLI agent
├── README.md              # Project documentation
├── assets/
│   └── Arduino_Agent_Demo.mp4
│   └── hardware_setup.png
│   └── Arduino_AI_Agent.jpeg
├── examples/
│   ├── basic_blink.ino    # Generated example sketches
│   └── button_LED_control.ino
├── requirements.txt       # Dependencies
```

---

## 📦 Quick Start

### Prerequisites
- Python 3.8+
- Arduino board (Uno, Nano, ESP32, etc.)
- USB cable
- macOS/Linux 

### Installation

```bash
# Clone and setup
git clone https://github.com/tumratde/prompt-to-pin.git
cd prompt-to-pin

# Create virtual environment
python3 -m venv prompt-env
source prompt-env/bin/activate  

# Install dependencies
pip install -r requirements.txt

# Install Arduino CLI 
brew install arduino-cli  # On Linux: curl -fsSL https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh | sh

# Setup AWS credentials for Bedrock
aws configure  # Or set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
```

---

## 🚀 Usage

```bash
# Connect your Arduino and run
python agent.py
```

### Example Interactions

**Basic LED Control:**
```
> Make the onboard LED blink every 1 second with serial output
```

**Sensor Integration:**
```
> Read temperature from a DHT22 sensor on pin 2 and display on serial monitor every 5 seconds
```

**Complex Projects:**
```
> Create a traffic light system with red on pin 8, yellow on pin 9, green on pin 10. Cycle every 3 seconds.
```

### What Happens Automatically
✅ Generates optimized Arduino sketch  
✅ Compiles with proper libraries  
✅ Detects and uploads to your board  
✅ Opens serial monitor (macOS/Linux)  
✅ Provides clear status updates

---

## 🎥 Demo

[![YouTube Demo](https://img.shields.io/badge/Watch-Demo-red?logo=youtube)](https://www.youtube.com/watch?v=SsTIuNGquJ0)

*Watch the agent transform natural language into working Arduino code in seconds*

---

## ✨ Key Features

### **Intelligent Code Generation**
- Natural language to Arduino C++ translation
- Context-aware code optimization
- Automatic library inclusion and pin configuration
- Error correction and debugging suggestions

### **Seamless Hardware Integration**
- Auto-detection of connected Arduino boards
- Automatic port selection and configuration
- Real-time compilation and upload
- Integrated serial monitoring with auto-launch

### **Developer Experience**
- Clear, structured response summaries
- Error handling with helpful suggestions
- Support for complex multi-component projects

---

## 🏛️ Technical Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Natural       │    │   Strands SDK     │    │   MCP Arduino   │
│   Language      │───▶│   Agent          │───▶│   Server        │
│   Input         │    │   Framework      │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                ▲
                                │                        │
                                ▼                        ▼
                       ┌──────────────────┐    ┌─────────────────┐
                       │   Claude 3.5     │    │   Arduino CLI   │
                       │   via Bedrock    │    │   + Hardware    │
                       └──────────────────┘    └─────────────────┘
                                ▲
                                │
                                ▼
                       ┌──────────────────┐
                       │   Conversation   │
                       │   Context &      │
                       │   Memory         │
                       └──────────────────┘
```

### **Component Breakdown**

**🧠 Strands SDK Agent**
- Orchestrates the entire workflow
- Manages conversation state and context
- Handles error recovery and user feedback
- Provides structured response formatting

**🔧 MCP Arduino Server**
- Abstracts Arduino CLI operations
- Provides type-safe tool interfaces
- Handles board detection and management
- Manages compilation and upload processes

**🤖 Claude 3.5 Integration**
- Generates optimized Arduino sketches
- Provides code explanations and documentation
- Suggests improvements and alternatives
- Handles debugging and troubleshooting

---

## 🎓 Learning Outcomes

This project demonstrates :

- **Modern AI Agent Architecture**: Using Strands SDK for production-ready agents
- **Protocol Integration**: Implementing MCP for standardized tool communication
- **Cloud AI Services**: Leveraging AWS Bedrock for scalable LLM integration
- **Hardware Abstraction**: Creating seamless software-hardware interfaces
- **Error Handling**: Implementing robust failure recovery mechanisms

---

## 🤖 Tech Stack

| Component | Technology | Purpose |
|-----------|------------|----------|
| **Agent Framework** | Strands SDK | Conversation management, tool orchestration |
| **LLM Provider** | Claude 3.5 via Amazon Bedrock | Code generation, natural language processing |
| **Tool Protocol** | Model Context Protocol (MCP) | Standardized LLM-tool communication |
| **Hardware Interface** | mcp-arduino-server + Arduino CLI | Board management, compilation, upload |
| **Runtime** | Python 3.8+ | Cross-platform compatibility |

---

## 📞 Contact

**GitHub**: [@tumratde](https://github.com/tumratde)  
**Author**: Deepinder Singh Tumrate

---

<div align="center">

**⭐ Star this repo if you found it helpful!**

[Report Bug](https://github.com/tumratde/prompt-to-pin/issues) • [Request Feature](https://github.com/tumratde/prompt-to-pin/issues) • [Documentation](https://github.com/tumratde/prompt-to-pin/wiki)

</div>
