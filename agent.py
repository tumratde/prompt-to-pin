import os
import sys
import subprocess
import time
import threading
import random
import logging
from datetime import datetime
from mcp import StdioServerParameters, stdio_client
from strands import Agent
from strands.models import BedrockModel
from strands.tools.mcp import MCPClient

# ─────────────────────────────────────────────────────────────
# Setup Logging
# ─────────────────────────────────────────────────────────────
os.makedirs("logs", exist_ok=True)
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = f"logs/session_{timestamp}.txt"

logging.basicConfig(
    filename=log_filename,
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)-8s - %(message)s"
)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter('%(message)s'))
logging.getLogger().addHandler(console)

print()
print()
logging.info("=" * 75)
print()
logging.info("🤖 Prompt-to-Pin: Natural Language to Arduino Code using Strand SDK")
logging.info("✨ Type your idea — I’ll generate the code, detect the board, compile, and upload it automatically!")
print()
logging.info("=" * 75)

# ─────────────────────────────────────────────────────────────
# Initialize MCP + Model
# ─────────────────────────────────────────────────────────────
class NullWriter:
    def write(self, txt): pass
    def flush(self): pass

arduino_client = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="uvx", args=["mcp-arduino-server@latest"]
        )
    )
)

bedrock_model = BedrockModel(
    model_id="us.anthropic.claude-3-5-haiku-20241022-v1:0",
    temperature=0.7,
)

SYSTEM_PROMPT = """
Arduino expert. Generate code, detect boards, upload automatically.
Always mention the exact port used for upload.
"""

def extract_port_from_response(response):
    """Extract Arduino port from response"""
    response_text = str(response)
    if "/dev/cu.usbserial" in response_text:
        lines = response_text.split('\n')
        for line in lines:
            if "/dev/cu.usbserial" in line:
                parts = line.split()
                for part in parts:
                    if "/dev/cu.usbserial" in part:
                        return part.strip('.,()[]')
    return None

def open_serial_monitor(port):
    """Open serial monitor in new terminal"""
    def run_monitor():
        try:
            clean_port = port.replace('`', '')  # remove any backticks just in case
            script = f'''
tell application "Terminal"
    do script "echo 'Arduino Serial Monitor - Port: {clean_port}'; arduino-cli monitor -p {clean_port}"
    activate
end tell
'''
            subprocess.run(['osascript', '-e', script])
        except Exception as e:
            logging.warning(f"⚠️  Auto-open failed. Run manually: arduino-cli monitor -p {port}")
    
    thread = threading.Thread(target=run_monitor)
    thread.daemon = True
    thread.start()


def main():
    suggestions = [
        "Make the onboard LED blink every 1 second. Add serial logs to show each blink cycle.",
        "Use a push button on pin 2 to control two LEDs. When the button is pressed, turn on the LED on pin 13 and toggle the LED on pin 12 (on/off each time the button is pressed). Include serial logs for button state and both LED statuses",
        "Create emergency sirens using alternating green and red LEDs (connected from pin 6 to pin 13) and a buzzer on pin 2. Simulate police, ambulance, and fire truck patterns with realistic flashing and sound. Log the active siren type and intensity via Serial Monitor.",
    ]
    logging.info(f"💡 Try a prompt like: {random.choice(suggestions)}\n")
    print()
    user_prompt = input("🧠 Arduino Request: ")
    ## logging.info(f"🧠 Received Prompt: {user_prompt}")

    original_stdout = sys.stdout
    original_stderr = sys.stderr
    sys.stdout = NullWriter()
    sys.stderr = NullWriter()

    try:
        logging.info("🔄 Processing...")

        with arduino_client:
            all_tools = arduino_client.list_tools_sync()
            logging.debug(f"🛠️ Available Tools: {all_tools}")

            enhanced_prompt = f"""
{user_prompt}

Auto-detect Arduino, create code, compile, upload automatically.
IMPORTANT: Always mention the exact port used (like /dev/cu.usbserial-2110).
"""

            sys.stdout = original_stdout
            agent = Agent(tools=all_tools, model=bedrock_model, system_prompt=SYSTEM_PROMPT)
            response = agent(enhanced_prompt)

            logging.info("✅ Upload completed!")

            port = extract_port_from_response(response)
            if port:
                logging.info(f"📺 Opening serial monitor for {port}...")
                time.sleep(1)
                open_serial_monitor(port)
                logging.info("✅ Serial monitor opened in new terminal")
            else:
                logging.warning("⚠️  Port not detected. Check response for manual connection.")

            logging.info("\n📋 Summary:")
            logging.info("-" * 35)
            logging.info(response)
            logging.debug(f"🧾 Full Claude Response:\n{response}")

    except Exception as e:
        sys.stdout = original_stdout
        logging.error(f"❌ Error: {str(e)}")

    finally:
        sys.stdout = original_stdout
        sys.stderr = original_stderr
        logging.info(f"\n📁 Full session log saved to: {log_filename}")

if __name__ == "__main__":
    main()
