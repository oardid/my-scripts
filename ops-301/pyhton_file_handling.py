#!/bin/pyhton3

# Script Name:                  ops301-challenge010
# Author:                       Omar Ardid
# Date of latest revision:      04/05/2024
# Purpose:                      Using file handling commands 

import os 

# Created a new file named "filehandling.txt"
filehandling_path = "filehandling.txt"

# Open file with write permission
with open(filehandling_path, "w") as file:
  # Write some lines (data) to the notebook
  file.write("Hello!\n")
  file.write("How's your day going?\n")
 
  # Append a new line 
with open(filehandling_path, "a") as file:
  file.write("Lets go to the park!")
  file.write("It's going good today!")
  file.write("It's sunny outside!") 

# Prints to the screeen the first line
with open(filehandling_path, "r") as file:
        first_line = file.readline()
        print("First Line:", first_line.strip())

# Close the file
file.close()

# Remove the file)
os.remove(filehandling_path)
