#!/usr/bin/python3

# Script Name:                  ops301-challenge09
# Author:                       Omar Ardid
# Date of latest revision:      04/04/2024
# Purpose:                      Creating if statments using conditionals

# Variables definitions
number1 = input("Enter a number: ")
number2 = input("Enter a another number: ")
# If statement

# If number1 equals to number2
if number1 == number2:
    print(f"Number {number1} and {number2} both are equal!")
# If number1 is less than number 2
elif number1 < number2:
    print(f"Number {number1} is less than {number2}")
else:
# If number1 is greater than number2 
    print(f"{number1} is greater than {number2}" )
# If number1 is not equal to number2
if number1 != number2:
    print(f"Number {number1} is not equal to {number2}")
elif number1 <= number2:
# If number1 is less than or equal to number2
    print(f"Number {number1} is less than or equal to {number2}")
else:
# If number1 is greater than number2
    print(f"Number {number1} is greater than {number2}")