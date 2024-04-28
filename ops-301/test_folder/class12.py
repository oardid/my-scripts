#!/bin/python3

# Import libraries
from requests import get 

# Do a get request using the requests library and assign 
response = get('https://google.com')

print(response.text)