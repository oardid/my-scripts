#!/usr/bin/python3

# Script Name:                  ops301-challenge08
# Author:                       Omar Ardid
# Date of latest revision:      04/03/2024
# Purpose:                      Working with lists in Python

# Variable list of ten string elements
print("")
foods = ["Pizza", "Hotdog", "Corn", "Chicken", "Burger", "Waffles", "Salads", "Pasta", "Sandwich", "Eggs"]
print("Food list: " + str(foods))

# Printing the fourth item in the list
print("Fourth item in the list: " + foods[3])

# Print the sixth trough tenth item in the list
print("Sixth item trough tenth item in the list: " + foods[5:10])

# Changing the value of the seventh item to onion
foods[6] = "Onion"
print(foods)
print("Replaced 'Salads' to 'Onion' from food list: " + foods[6])
