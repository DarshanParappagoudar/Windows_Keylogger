Python Keylogger
This Python program serves as a basic keylogger that logs keystrokes and sends them via email. It runs in the background, capturing all keyboard input and storing it in a log file. Additionally, it emails the log file periodically to a specified email address.

Features --
Logs all keystrokes (including special keys)
Stores keystrokes in a local log file (log.txt)
Sends log file via email

Requirements --
Python 3.x
pynput library: Used to monitor keyboard input
smtplib library: Used to send emails
An email account for sending and receiving logs
Allow less secure apps in your Gmail settings if you're using Gmail as the sender

Installation -- 
Clone this repository to your local machine:
git clone https://github.com/your_username/keylogger.git

Navigate to the project directory:
cd keylogger

Install the required Python libraries:
pip install -r requirements.txt

Usage--
Modify the send_mail() function with your email credentials and recipient email address.

Run the script:
python keylogger.py

The keylogger will start running in the background, logging all keystrokes.
Press Esc key to stop the keylogger. The log file will be saved as log.txt in the project directory.

Important Note
Security: Be cautious while using this tool, as keyloggers can be considered malicious software. Ensure you have appropriate permissions to monitor keyboard input, and only use it for lawful purposes.
