#!/bin/bash

# Script Name:                  ops301-challenge03
# Author:                       Omar Ardid
# Date of latest revision:      03/27/2024
# Purpose:                      Changing permissions in system files/directories

# Declaration of variables
curre=$(pwd)

directpath() {
    # Shows the user current directory path
    echo "Current directory: $curre"
    # Asking the user to input the directory path to change permission
    echo "Please enter full directory path to change permission:" 
    read -r input_dir
    # Asking the user to input the number 777 to change permission
    read -p "Enter permissions number '777' to perform a chmod 777: " perm
    # Change permissions
    chmod "$perm" "$input_dir" 
    # Navigate to the directory
    cd "$input_dir" 
    # See changes
    echo "New directory: $(pwd)"
    echo "Directory contents after permission change:"
    ls -als
}
directpath