import subprocess
import time
import requests
import webbrowser
import pyperclip
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

PYTHON = os.path.join(BASE_DIR, "venv", "Scripts", "python.exe")
APP = os.path.join(BASE_DIR, "app.py")

print("=" * 60)
print("            Z3r0Trace Launcher")
print("=" * 60)

# --------------------------------------------------
# Start Flask
# --------------------------------------------------

print("[+] Starting Flask Server...")

flask_process = subprocess.Popen(
    [PYTHON, APP],
    cwd=BASE_DIR
)

time.sleep(3)

# --------------------------------------------------
# Start Ngrok
# --------------------------------------------------

print("[+] Starting Ngrok Tunnel...")

ngrok_process = subprocess.Popen(
    ["ngrok", "http", "5000"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

time.sleep(5)

# --------------------------------------------------
# Get Public URL
# --------------------------------------------------

print("[+] Fetching Public URL...")

public_url = None

try:

    tunnels = requests.get(
        "http://127.0.0.1:4040/api/tunnels"
    ).json()

    public_url = tunnels["tunnels"][0]["public_url"]

except Exception:

    print("[-] Unable to read Ngrok URL.")

# --------------------------------------------------
# Copy URL
# --------------------------------------------------

if public_url:

    pyperclip.copy(public_url)

    print()

    print("=" * 60)

    print(f"Local URL : http://127.0.0.1:5000")

    print(f"Public URL: {public_url}")

    print()

    print("Public URL copied to clipboard!")

    print("=" * 60)

    webbrowser.open(public_url)

else:

    webbrowser.open("http://127.0.0.1:5000")

print()

print("Z3r0Trace is Running")

print()

try:

    while True:
        time.sleep(1)

except KeyboardInterrupt:

    flask_process.terminate()
    ngrok_process.terminate()

    print("Stopped.")