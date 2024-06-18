#!/usr/bin/python3

# Script Name:                  ops401-challenge37
# Author:                       Omar Ardid
# Date of latest revision:      06/18/2024
# Purpose:                      Capture a cookie and send it back out to the site in order to receive a valid response in HTTP text
# Resources:                    https://github.com/codefellows/seattle-cybersecurity-401d12/blob/main/class-37/challenges/DEMO.md

import requests, subprocess

def get_target_site():
    """
    Get the target site from the user.

    Returns:
        str: The target site URL.
    """
    while True:
        # Ask the user for the target site, or 'q' to quit
        #targetsite = input("Enter target site (or 'q' to quit): ")
        targetsite = "http://www.whatarecookies.com/cookietest.asp"  # Comment this out if you're using the line above
        if targetsite.lower() == 'q':
            print("Goodbye!")
            exit()
        return targetsite

def bring_forth_cookie_monster():
    """
    Bring forth the cookie monster.

    No returns.
    """
    print('''
              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

def main():
    """
    Main function.

    No returns.
    """
    try:
        # Get the target site from the user
        targetsite = get_target_site()
        # Bring forth the cookie monster
        bring_forth_cookie_monster()
        # Send a GET request to the target site and capture the response
        response = requests.get(targetsite)
        cookie = response.cookies

        # Print the target site and captured cookie
        print("Target site is " + targetsite)
        print(cookie)

        # Send a new GET request to the target site with the captured cookie and capture the new response
        new_response = requests.get(targetsite, cookies=cookie)
        new_cookie = new_response.cookies

        # Save the new response to a file called response.html
        with open("response.html", "w") as file:
            file.write(new_response.text)

        # Print a message indicating that the response was saved and open it in a web browser (for Linux)
        print("Response saved to response.html")
        subprocess.call(['xdg-open', 'response.html'])  

    except Exception as e:
        # If an error occurs, print an error message with details of the error
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    """
    Run the main function if this script is run as a standalone program.
    """
    main()