from pynput import keyboard
import hashlib
from cryptography.fernet import Fernet

# Generate a random encryption key
def generate_key():
    return Fernet.generate_key()

# Encrypt the input using the encryption key
def encrypt_input(input_text, key):
    cipher_suite = Fernet(key)
    encrypted_text = cipher_suite.encrypt(input_text.encode())
    return encrypted_text

# Callback function to encrypt and print the keystrokes
def on_press(key):
    try:
        # Convert the key to string
        key_str = str(key.char)
        # Encrypt the key
        encrypted_key = encrypt_input(key_str, encryption_key)
        print(f"Encrypted Keystroke: {encrypted_key.decode()}")
    except AttributeError:
        print(f"Special Key: {key}")

# Generate encryption key
encryption_key = generate_key()

# Create keyboard listener
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Keep the listener running until a key interruption
try:
    listener.join()
except KeyboardInterrupt:
    pass


