#!/bin/python

# Script Name:                  ops301-challenge07
# Author:                       Omar Ardid
# Date of latest revision:      04/02/2024
# Purpose:                      Generates all directories, sub-directories and files for a user-provided directory path

# Import libraries
import os

# Declaration of variables

### Read user input here into a variable
path = input("Enter the full file path: ")

# Declaration of functions

### Declare a function here
def directs(file_path):
    for (root, dirs, files) in os.walk(file_path):
        ### Add a print command here to print ==root==
        print(root)
        ### Add a print command here to print ==dirs==
        print(dirs)
        ### Add a print command here to print ==files==
        print(files)

# Main

### Pass the variable into the function here
directs(path)
# End
