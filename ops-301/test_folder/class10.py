#!/bin/python3

# Import libraries
import os 

# Objectives
# Create a new .txt file
# Opening with write permissions will overwrite the entire file 
new_file = open("testfileV2.txt", "w")
new_file.write("This is my new test file.")
new_file.write("This is the second line.")
new_file.close()

# Append three lines
new_file = open("testfileV2.txt", "a")
new_file.write("\n")
new_file.write("This is the line that I appended to the file.")
new_file.write("\n")
new_file.write("This is the third line.")
new_file.write("\n")
new_file.write("This is the fourth line.")
new_file.close()
# Print only the first line to the screen 
read_file = open("testfileV2.txt", "r")
# For loop to print one line at a time
for line in read_file:
    # Print only the first line of the file
    print(line)
# Delete .txt file
os.rename("testfileV2.txt", "testfileV3.txt")
os.remove("testfileV2.txt")
