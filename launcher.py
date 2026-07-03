import subprocess
import time
import requests
import webbrowser
import pyperclip
import os
import sys
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
APP = os.path.join(BASE_DIR, "app.py")

# Use the current Python interpreter (works everywhere)
PYTHON = sys.executable

print("=" * 60)
print("            Z3r0Trace Launcher")
print("=" * 60)

# -----------------------------
# Start Flask
# -----------------------------

print("[+] Starting Flask Server...")

flask_process = subprocess.Popen(
    [PYTHON, APP],
    cwd=BASE_DIR
)

time.sleep(3)

# -----------------------------
# Check Ngrok
# -----------------------------

ngrok_path = shutil.which("ngrok")

if ngrok_path:

    print("[+] Starting Ngrok Tunnel...")

    ngrok_process = subprocess.Popen(
        [ngrok_path, "http", "5000"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    public_url = None

    # Wait until Ngrok API becomes available
    for _ in range(20):

        try:

            response = requests.get(
                "http://127.0.0.1:4040/api/tunnels",
                timeout=2
            )

            data = response.json()

            if data["tunnels"]:

                public_url = data["tunnels"][0]["public_url"]

                break

        except Exception:

            pass

        time.sleep(1)

    if public_url:

        pyperclip.copy(public_url)

        print()

        print("=" * 60)

        print(f"Local URL : http://127.0.0.1:5000")
        print(f"Public URL: {public_url}")

        print("=" * 60)

        webbrowser.open(public_url)

    else:

        print("[!] Ngrok started but public URL could not be retrieved.")

        webbrowser.open("http://127.0.0.1:5000")

else:

    print("[!] Ngrok not found.")

    webbrowser.open("http://127.0.0.1:5000")

print()
print("Z3r0Trace is running...")
print()

try:

    while True:
        time.sleep(1)

except KeyboardInterrupt:

    flask_process.terminate()

    if ngrok_path:
        ngrok_process.terminate()

    print("Stopped.")