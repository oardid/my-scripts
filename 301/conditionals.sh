#!/bin/bash

# Script Name:                  ops301-challenge04
# Author:                       Omar Ardid
# Date of latest revision:      03/28/2024
# Purpose:                      Create a bash script that launches a menu system
# Source:                       https://www.wikihow.com/Ping-in-Linux#Advanced-Ping-Examples 
# Declaration of variables


sysmenu(){
    while true; do 
        clear
        echo "System Menu"
        echo "1. Print 'Hello world' to the screen."
        echo "2. Ping yourself (pings this computer's loopback address)."
        echo "3. Ip Info."
        echo "4. Exit."
        read -p "Enter your choice: " choice
    
        if [[ $choice == 1 ]]; then
            echo "Hello World"
            read -p "Press enter to return to the main menu."
        elif [[ $choice == 2 ]]; then
            ping -c 4 127.0.0.1
            read -p "Press enter to return to the main menu."
        elif [[ $choice == 3 ]]; then
            ifconfig -a
            read -p "Press enter to return to the main menu."
        elif [[ $choice == 4 ]]; then
            exit 0
        else 
            echo "Invalid choice. Please enter a number from 1 to 4."
            read -p "Press enter to return to the main menu."
        fi
    done
}
sysmenu
