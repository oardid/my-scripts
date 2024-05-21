#!/bin/usr/python3

# Script Name:                  ops401-challenge16
# Author:                       Omar Ardid
# Date of latest revision:      05/20/2024
# Purpose:                      Creating a Brute Force Tool
# Resources:                    

import time
import os

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
                    # Removing whitespaces between words
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
    target_string = input("Enter a string to search: ")
    # Asking the user for word list
    wordlistpath = input("Enter word list file path: ")
    # Checking the provided path is a file
    if os.path.isfile(wordlistpath):
        try:
            # Open word list in read mode
            with open(wordlistpath, 'r') as wordlistfile:
                # Check if target string is in word list
                if target_string in wordlistfile.read():
                    # Print if string is found
                    print(f"String '{target_string}' found in the word list.")
                else:
                    # Print if string is not found
                    print(f"String '{target_string}' not found in the word list.")
        except Exception as e:
            # Print any erros that may occur
            print(f"An error occurred: {e}")
    else:
        print("(ง •̀_•́)ง Word file not found. Please enter a vaild file path! ")

def menu():
    while True:
        print("\n~~~~~ Brute Force Wordlist Attack ~~~~~")
        print("1. Offensive; Dictionary Iterator")
        print("2. Defensive; Password Recognzied")
        print("0. Exit")
        choice = input("Enter a number: ")

        if choice == "1":
            offensive()
        elif choice == "2":
            defensive()
        elif choice == "0":
            print("(づ ◕‿◕ )づ Goodbye!")
            break
        else:
            print("\nε(*´･ω･)з Invalid number! ")

if __name__ == "__main__":
    menu()