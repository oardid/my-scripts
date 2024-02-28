#!/bin/bash 
# Script Name:                  ops201-challenge07-System Information
# Author:                       Omar Ardid
# Date of latest revision:      02/27/2024
# Purpose:                      Create a script that uses lshw to display system information
# Resources:                    



sys_info(){
    read -p "Do you want to display Computer name? (y/n) : " answer
    if [[ $answer == "y" ]]; then 
    echo "Name of computer: "$(lshw | grep "" -m1)
    fi
    read -p "Do you want to display CPU? (y/n) : " answer
    if [[ $answer == "y" ]]; then
    echo "CPU: "$(lshw | grep "*-cpu" -A 6)
    fi
    read -p "Do you want to display RAM? (y/n) : " answer
    if [[ $answer == "y" ]]; then
    echo "RAM:"$(lshw -class memory | grep -E 'description:|physical id:|size:')
    fi
    read -p "Do you want to display 'Display adapter'? (y/n) : " answer
    if [[ $answer == "y" ]]; then
    echo "Display adapter: "$(lshw -class display | grep -A 10 "display")
    fi
    read -p "Do you want to display Network adapter? (y/n) : " answer
    if [[ $answer == "y" ]]; then
    echo "Network adapter: "$(lshw -class network | grep -A 15 "network")
    fi
    
}
sys_info

