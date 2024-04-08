#!/usr/bin/python3

# Assign a variable a list of ten string elements
parks_list = ["Yosemite", "Yellowstone", "Glacier", "Grand Canyon", "Zion", "Grand Tetons", "Bryce", "Arches", "Rocky Mountain", "Haleakala" ]
#print(type(parks_list[1]))
print(parks_list[1])
# Print the fourth item on the list
print("Print Fourth item: ")
print(parks_list[3])

# Print the sixth through tenth item on list
print("Elements 6-10 only: ")
print(parks_list[:5])

# Change the value of the seventh item to "onion"
parks_list[6] = "Onion"
print(parks_list)