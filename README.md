Remote Access Trojan (RAT) - Python Version
This is a basic Python-based Remote Access Trojan (RAT) for educational purposes. It allows an attacker to perform various actions on a target machine, such as taking screenshots, retrieving browsing history, getting the device's location, and more. This script demonstrates how to interact with a target machine over a network.

Features
Screenshot Capture: Take a screenshot of the target machine and save it on the attacker's system.

Browser History: Retrieve the last 20 URLs visited from the Chrome browser.

Location Information: Obtain the IP address, location (city, region, country), and geolocation coordinates of the target.

SSH Port Access: Open an SSH port (port 22) and start the SSH service on the target machine.

Command Execution: Execute commands on the target machine and send the output back to the attacker.

Important Legal Warning
This tool is intended for educational purposes only. Unauthorized access to computer systems and networks is illegal and unethical. Only use this tool on machines you own or have explicit permission to test. Always adhere to ethical hacking standards.

Requirements
Python 3.x

Required Python libraries:

pyautogui (for taking screenshots)

requests (for retrieving location information)

pysqlite3 (for retrieving Chrome browsing history)

You can install the required libraries using the following command:

bash
Kopyala
Düzenle
pip install pyautogui requests pysqlite3
Files
server.py: This is the attacker's listener script. It listens for incoming connections from the target and issues commands.

client.py: This is the client script that runs on the target machine. It connects to the attacker's server and executes the commands sent by the attacker.

Usage Instructions
1. Setting up the Attacker's Server (Listener)
Run the server.py script on the attacker's machine. It will listen for incoming connections from the target machine on port 4444.

bash
Kopyala
Düzenle
python server.py
Once the server is running, it will display a prompt where the attacker can enter commands to control the target machine.

2. Setting up the Target Machine
Modify the SERVER_IP variable in client.py with the IP address of the attacker's machine.

Example: SERVER_IP = '192.168.1.100' (replace with your actual attacker's IP address).

python
Kopyala
Düzenle
SERVER_IP = '192.168.1.100'  # Replace with the attacker's IP address
Run the client.py script on the target machine. It will automatically connect to the attacker's server.

bash
Kopyala
Düzenle
python client.py
3. Commands for the Attacker
Once the target machine connects to the attacker's server, the attacker can issue the following commands:

screenshot: Capture a screenshot from the target machine.

history: Retrieve the last 20 URLs visited from the target's Chrome browser.

location: Get the target's IP address, city, region, country, and geolocation coordinates.

open_ssh: Open an SSH port (22) and start the SSH service on the target machine.

exit: Close the connection with the target machine.

Example Attacker Command:
ruby
Kopyala
Düzenle
>> screenshot
The attacker can enter these commands into the terminal, and the output (e.g., the screenshot or browsing history) will be displayed or saved on the attacker's machine.

4. Saving the Output
For commands like screenshot, the captured data will be saved as received_screenshot.png on the attacker's machine.

For other commands, the output will be displayed directly in the attacker's terminal.

Security Considerations
Ensure you have proper authorization before testing on any system.

The RAT only works in local or controlled environments. It will not bypass advanced network security measures such as firewalls, IDS, etc.

This tool is not meant to be used for malicious purposes or unauthorized access to devices.

Disclaimer
This project is NOT intended for illegal use. Use it responsibly and only for ethical purposes. The developer assumes no responsibility for the misuse of this tool.
