#!/bin/pyhton3

# Import libraries
import requests

# Define variables
# Ask the user for the web address
address = input("Type in the destination URL (format: google.com): \n")

# Concatenate https with user input 
user_url = str('http://' + address)

# Ask the user for the HTTP method they wanted to use
choice = input("Select an HTTP method from the following list:\n get \n post \n put \n delete \n head \n patch \n options \n Type in your selection: ")

# Define variables
def user_menu():

    # Conditional + checking what the user gave us 
    if choice == 'get':
        method = requests.get
    elif choice == 'post':
        method = requests.post
    elif choice == 'put':
        method = requests.put
    elif choice == 'delete':
        method = requests.head
    elif choice == 'head':
        method = requests.head
    elif choice == 'patch':
        method = requests.patch
    elif choice == 'options':
        method = requests.options
    else:
        print("Invalid selection: We'll go with 'get'")
        method = requests.get

    # Actually send the request using the method the user sent
    response = method(user_url)
    return response

# Function that handles output based on user input 

def run_command():
    response = user_menu()
    confirm = input("Please confirm you want to run the following command: \n \n request." + choice + "('" + user_url + "') ----> \n Enter 'y' to confirm or 'n' to cancel.").lower()

    if confirm == 'y':
        print("\nThe status code is: " + str(response.status_code))
        if response.status_code == 200:
            print("That\'s the code for a successfull request.")
        elif response.status_code == 307:
            print("That\'s the code for a temporary redirect.")
        elif response.status_code == 400:
            print("That\'s the code for a bad request.")
        elif response.status_code == 403:
            print("403? - You don\'t have permission to that.")
        elif response.status_code == 404:
            print("That\'s the code for a site not found.")
        else:
            print("We received a code we can't recognize.")
    else:
        print("\nOkay, then. Re-run the script if you want if you want to try again.")

    # Print header information 
    print("And now.. your header information:\n")
    print(response.headers)

# Call our function
run_command()