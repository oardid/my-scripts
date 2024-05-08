#!/bin/usr/python3

# Script Name:                  ops401-challenge07
# Author:                       Omar Ardid
# Date of latest revision:      05/07/2024
# Purpose:                      Adding recursively feature to encrypt and decrypt folder and all its contents
# Resources:                    https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python https://www.pythoncentral.io/recursive-file-and-directory-manipulation-in-python-part-1/

import subprocess
from cryptography.fernet import Fernet
import os 

# Function to generate and write a key to a file
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

# Function  to load the key from a file
def load_key():
    return open("key.key", "rb").read()

# Function to encrypt a file
def encrypt_file(file_path, key):
    try:
        f = Fernet(key)
        with open(file_path, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(file_path, "wb") as file:
            file.write(encrypted_data)
        print("File encrypted successfully!")
    except Exception as e:
        print(f"Error encrypting file: {e}")

# Function to decrypt a file
def decrypt_file(file_path, key):
    try:
        f = Fernet(key)
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(file_path, "wb") as file:
            file.write(decrypted_data) 
        print("File decrypted successfully!")
    except FileNotFoundError:
        print(f"Error: Encrypted file '{file_path}' not found.")

def encrypt_directory(directory_path, key):
    # Using Recursively to encrypt all files in the specified directory and its subdirectories
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            encrypt_file(file_path, key) # Encrypt each file
    print("Directory has been encrypted!")

def decrypt_directory(directory_path, key):
    # Using Recursively to decrypt all files in the specified directory and its subdirectories
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            decrypt_file(file_path, key) # Decrypt each file
    print("Directory has been decrypted!")

while True:  
    print("~~~~ Encrypting and Decrypting MENU ~~~~")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")
    print("5. Install Cryptography")
    print("6. Encrypt a folder and all its contents")
    print("7. Decrypt a folder and all its contents")
    print("8. Exit")
    choice = input("Before running this script make sure to have 'Cryptography' installed.\nEnter your choice: ").lower()
    if choice == '1': 
        write_key() # Generating a key
        key = load_key() # Load that generated key into "key" variable
        file_path = input("Enter the file path to encrypt: ")
        encrypt_file(file_path, key) # Encrypt the specified file
    elif choice == '2':
        if key is None:
            print("Error: Please encrypt a file (option 1) first to generate the key.")
            continue
        file_path = input("Enter the file path to decrypt: ")
        decrypt_file(file_path, key) # Decrypt the specified file
    elif choice == '3':
        write_key() # Generating a key
        key = load_key() # Load that generated key into "key" variable
        message = input("Enter a message to encrypt: ").encode()
        fernet = Fernet(key)
        encrypted_message = fernet.encrypt(message)
        print("Encrypted message:", encrypted_message) # Encrypts specified message inputed
    elif choice == '4':
        key = load_key() # Loading the key
        encrypted_message = input("Enter the encrypted message: ")
        fernet = Fernet(key)
        try:
            decrypted_message = fernet.decrypt(encrypted_message.encode()).decode()
            print("Decrypted message:", decrypted_message) # Decrypts the message
        except Exception as e:
            print(f"Error decrypting message: {e}") 
    elif choice == '5':
        try:
            subprocess.run(["pip3", "install", "cryptography"], check=True)
            print("Cryptography installed successfully!")
        except subprocess.CalledProcessError:
            print("Error installing cryptography.")
    elif choice == '6':
        write_key() # Generating a key
        key = load_key() # Load that generated key into "key" variable
        folder_path = input("Enter the folder path to encrypt: ")
        encrypt_directory(folder_path, key) # Encrypts the specified directory
    elif choice == '7':
        key = load_key() # Loading the key
        folder_path = input("Enter the folder path to decrypt: ")
        decrypt_directory(folder_path, key) # Decrypt the specified directory
    elif choice == '8':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
