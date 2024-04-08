

# Import libraries
import os

# Use os.walk() function from the os library
# os.walk() needs to eb enclosed in a function
def first_python_function(dir_name):
    for (root,dirs,files) in os.walk(dir_name):
        # Add a print command to print root
        print("====Root====")
        print(root)
        print("")
        
        # Add a print command to print dirs
        print("====Dirs====")
        print(dirs)
        print("")

        # Add a print command to print files
        print("====Files====")
        print(files)
        print("")


# Ask the user for a file path and save it in a variable
user_input = input("Type in the absolute path of the directory from the home folder: ")

# Call the function and pass the bariable provided by the user
first_python_function(user_input)