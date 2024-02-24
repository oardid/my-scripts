#!/bin/bash

# Script Name:                  ops201-challenge05-Loops
# Author:                       Omar Ardid
# Date of latest revision:      02/23/2024
# Purpose:                      Create a script that ask the user for a PID, then kills the process
# Resources: 



echo "Your current PID is: $$"
#Loops until user crtl+c
while true; do
    read -p "Enter your PID to kill the process or stay here forever. If you give up crtl+c to quit: " choice
    if [[ -z "$choice" ]]; then 
    # If crtl+c is entered, break out of loop
        break
    fi
    #Kill procces with PID
    echo "Killing process with PID: $$"
    kill "$$choice" 2>/dev/null || echo "Failed to kill process with PID: $choice"
done



