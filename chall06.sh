#!/bin/bash
# Script Name:                  ops201-challenge06-Conditionals
# Author:                       Omar Ardid
# Date of latest revision:      02/26/2024
# Purpose:                      Create a script that detects if a directory exists, then creates it if it does not exist
# Resources: 

dir_list=()

check_and_add() {
    search="dir"
    
    while true; do 
        read -p "Enter directory to see if it exists or add it (or 'done' to finish): " input
        if [[ $input == "done" ]]; then
            break
        fi
 
        if [ -d "$input" ]; then
            echo "Directory '$input' exists."
        else
            read -p "Directory '$input' does not exist. Do you want to add it? (y/n): " create_dir
            if [[ $create_dir == "y" ]]; then
            mkdir -p "$input" && echo "Directory '$input' has been created." || echo "Failed to create directory '$input'."
        else 
            echo "Directory '$input' not created."
            continue    
        fi 
    fi
        found=1
        for i in "${dir_list[@]}"; do
            if [ "$i" == "$input" ]; then  
                found=0
                break
            fi
        done

        if [[ $found -eq 0 ]]; then
            echo "'$input' is already in the list."
        else 
            dir_list+=("$input")
            echo "'$input' added to the list."
        fi
    done 

    read -p "Do you want to display directory list? (y/n): " display
    if [[ $display == "y" ]]; then
        echo "Directory list content: ${dir_list[@]}"
    else
        echo "Directory list display skipped."
    fi
}

check_and_add
