#!/usr/bin/python3

# Define a function in python
def my_first_function():

    print("This is inside the function.")

# Define a second function
def function_with_parameters(name):
    print(f"Your name is: {name}")

# Calling our function
my_first_function()
#function_with_parameters("Omar")

# Ask the user for their name
username = input("Enter your username")
function_with_parameters(username)