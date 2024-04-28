#!/usr/bin/python3

# How to create a tuple - immutable - can't be changed
thistuple = ("apple", "banana", "cherry")
print("This is the tuple: " + str(thistuple))

# How to create a list
grocery_list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "bread"]
print("This is the list: " + str(grocery_list))

# Print the first item in the list
print("This is the first item in the list: " + grocery_list[0])

# Print the last iten in the list
print("This is the last item in the list: " + grocery_list[-1])

# Print a slice (range) of the list
# Print from the 3rd item to the 5th item of the list
print(grocery_list[2:5])

# Print from the beggining of the list up to a specific index
print(grocery_list[:4])

# How to add an item to the list
grocery_list.append("steak")
print(grocery_list)

grocery_list.insert(1, "butter")
print(grocery_list)

grocery_list.remove("butter")
print(grocery_list)

# Print a slice of items with a step value
print(grocery_list[1:8:2])