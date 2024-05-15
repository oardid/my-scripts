import sys
import time
import random

def hacking_animation(text):
    while True:
        for i in range(len(text)):
            sys.stdout.write("\b \b" * len(text))  # Clear the text
            sys.stdout.write(text[i:] + text[:i])  # Rotate the text
            sys.stdout.flush()
            time.sleep(random.uniform(0.01, 0.1))  # Random delay between characters

def main():
    menu_items = ["Option 1", "Option 2", "Option 3"]

    # Display the menu
    for item in menu_items:
        print(item)

    # Display the animated text above the menu
    animated_text = "run as super user"
    sys.stdout.write(animated_text)
    sys.stdout.flush()

    # Apply the hacking animation to the displayed text
    hacking_animation(animated_text)

if __name__ == "__main__":
    main()

