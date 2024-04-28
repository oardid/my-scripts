#!/bin/usr/phyton3





#greeting = Welcome to Python!

# Call the variable
#print(greeting)

# Import a library / modules
#from os import system

#system("ls")

import os

#list = os.system("ls")
#user = os.system("whoami")

# Executing command but redirecting output to a txt file
os.system("ls > list.txt")
os.system("whoami > user.txt")

# For loop
for file in ["list.txt", "user.txt"]:
    with open(file, "r") as f:
        output = f.read()
        #print(output)
        # Print out the contents using f-string
        #print(f"Command output: {output}")
        print("Command output: " + output)

        os.remove(file)
        print(f"Deleted {file} file! \n")
