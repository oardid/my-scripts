#!/bin/usr/python3

# Script Name:                  ops401-challenge06
# Author:                       Omar Ardid
# Date of latest revision:      05/06/2024
# Purpose:                      Creating a python script that encrypts a files
# Resources:                    https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python

import subprocess
from cryptography.fernet import Fernet
import os

def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

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

while True:  
    print("~~~~ Encrypting and Decrypting MENU ~~~~")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Encrypt a message")
    print("4. Decrypt a message")
    print("5. Install Cryptography")
    print("6. Exit")
    choice = input("Before running this script make sure to have 'Cryptography' installed.\nEnter your choice: ").lower()
    if choice == '1': 
        write_key()
        key = load_key()
        file_path = input("Enter the file path to encrypt: ")
        encrypt_file(file_path, key)
    elif choice == '2':
        if key is None:
            print("Error: Please encrypt a file (option 1) first to generate the key.")
            continue
        file_path = input("Enter the file path to decrypt: ")
        decrypt_file(file_path, key)
    elif choice == '3':
        write_key()
        key = load_key()
        message = input("Enter a message to encrypt: ").encode()
        fernet = Fernet(key)
        encrypted_message = fernet.encrypt(message)
        print("Encrypted message:", encrypted_message)
    elif choice == '4':
        key = load_key()
        encrypted_message = input("Enter the encrypted message: ")
        fernet = Fernet(key)
        try:
            decrypted_message = fernet.decrypt(encrypted_message.encode()).decode()
            print("Decrypted message:", decrypted_message)  
        except Exception as e:
            print(f"Error decrypting message: {e}")
    elif choice == '5':
        try:
            subprocess.run(["pip3", "install", "cryptography"], check=True)
            print("Cryptography installed successfully!")
        except subprocess.CalledProcessError:
            print("Error installing cryptography.")
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
