#!/bin/usr/python3

# Declare a function
def make_a_sandwich(user_name):

    print(f"Hi {user_name}")

    # Prompt the user to enter sandwich ingredients
    bread = input("What bread do you want on your sandwich?")
    cheese = input("What cheese do you want on your sandwich?")
    meat = input("What meat do you want on your sandwich?")
    vegetables = input("What vegetables do you want on your sandwich?")
    condiments = input("What condiments do you want on your sandwich?")

    # Initialize a tuple with the sandwich ingredients
    sandwich_ingredients = (bread, cheese, meat, vegetables, condiments)

    print(f"\nThis is {user_name}'s ultimate snadwich: ")
    print("======")

    # Unpack the tuple in a for loop and print each ingredients
    for ingredients in (sandwich_ingredients):
        print(ingredients)
    print("======")

user = input("What is your name: ")
make_a_sandwich(user)

user_friend = input("What is your friend's name")
make_a_sandwich(user_friend)
