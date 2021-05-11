#!/usr/bin/env python3

# Author: Tom Esch
# Purpose: Encrypt a single string
# Last Revised: April 12th, 2021
# Purpose: Log the encryption event.
# Last Revised: May 5th, 2021

# Import Libraries
from cryptography.fernet import Fernet
import logging
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %%p')
logging.warning('is when this event was logged.') 

# Generate a key and save it into a file - use and then comment out
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)
#     print("Key is "+str(key.decode('utf-8')))

# Load the key from the current directory named 'key.key'
def load_key():
    return open("key.key", "rb").read()

# Main
# write_key() # Generate and write a new key
key = load_key() # Load the previously generated key
print("Key is "+str(key.decode('utf-8')))

message = "Hey budday!".encode()
print("Plaintext is "+str(message.decode('utf-8')))

f = Fernet(key) # Initialize the Fernet class

encrypted = f.encrypt(message) # Encrypt the message

# Print how it looks
print ("Ciphertext is "+str(encrypted.decode('utf-8')))

# Fin 


