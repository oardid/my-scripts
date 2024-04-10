#!/bin/python3

# Script Name:                  ops301-challenge12
# Author:                       Omar Ardid
# Date of latest revision:      04/09/2024
# Purpose:                      Performing HTTP GET requests using the requests Python library
# Resource:                     https://www.youtube.com/watch?v=63nw00JqHo0 https://www.geeksforgeeks.org/10-most-common-http-status-codes/#

# Import libraries
import requests

# Define variables

# Define functions
def user_menu():
    # Prompt the user to type a string input as the variable for the URL
    url = input("Type your destination URL: ")
    # Figure out how to add 'http://' at the beginning if user not inputed
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'https://' + url  
        # Prompt the user to pick an HTTP method 
        print("~~~~ HTTP METHODS MENU ~~~~")
        print("1. GET")
        print("2. POST")
        print("3. PUT")
        print("4. DELETE")
        print("5. HEAD")
        print("6. PATCH")
        print("7. OPTIONS")
        option = int(input("Enter the number you want to select a HTTP Method: "))
        return option, url

def send_request(option, url):
    methods = {1: 'GET', 2: 'POST', 3: 'PUT', 4: 'DELETE', 5: 'HEAD', 6: 'PATCH', 7: 'OPTIONS'}
    if option not in methods:
        print("Invalid option!")
        return
    try:
        # Constructing the request
        request_method = methods[option]
        request = requests.Request(request_method, url)
        prepared_request = request.prepare()
        
        # Print out the entire request to the screen
        print("~~~~ Entire request ~~~~")
        print(f"Method: {request_method}")
        print(f"URL: {url}")
        for header, value in prepared_request.headers.items():
            print(f"{header}: {value}")
        
        # Ask the user to confirm before sending it
        confirm = input("Do you want to send this request? (yes/no): ")
        if confirm.lower() == 'yes':
            print("Sending request...")
            
            # Sending the request
            response = requests.Session().send(prepared_request)
            
            # Translate the HTTP status code for the user
            status_code_translation = {
                200: 'OK',
                201: 'Created',
                204: 'No Content',
                400: 'Bad Request',
                401: 'Unauthorized',
                403: 'Forbidden',
                404: 'Not Found',
                405: 'Method Not Allowed',
                500: 'Internal Server Error',
                502: 'Bad Gateway',
                503: 'Service Unavailable'
            }
            translated_status = status_code_translation.get(response.status_code, 'Unknown')
            print("Response Code:", translated_status)
            
            # Print out the response headers
            print("Response Headers:")
            for header, value in response.headers.items():
                print(f"{header}: {value}")
            
            return response
        else:
            print("Request canceled.")
    except requests.RequestException as e:
        print("An error occurred:", e)

# Call the user_menu function to start the script
option, url = user_menu()
response = send_request(option, url)

