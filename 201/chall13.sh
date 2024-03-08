#!/bin/bash
# Script Name:                  ops201-challenge13- Domain Analyzer
# Author:                       Omar Ardid
# Date of latest revision:      03/06/2024
# Purpose:                      Create a script that ask user to type a domain, then displays information of the domain
# Resources:                    





#Asking user to input a domain
display_dom() {
    read -p "Enter a domian you want to display information about: " domain
    if [[ $domain != "" ]]; then
        whois $domain
    fi
    read -p "Do you want to run 'dig' command on the domain you just enter? (y/n) : " input 
    if [[ $input == "y" ]]; then
        dig $domain 
    fi
    read -p "Do you want to run 'host' command on the domain you just enter? (y/n): " input
    if [[ $input == "y" ]]; then 
        host $domain 
    fi
    read -p "Do you want to run 'nslookup' command on the domain you just enter? (y/n): " input
    if [[ $input == "y" ]]; then
        nslookup $domain 
    fi

    while true; do
        read -p "Do you want to save the information to txt file? (y/n): " save_input
        if [[ $save_input == "y" || $save_input == "n" ]]; then
            break
        fi
    done

    if [[ $save_input == "y" ]]; then
    while true; do
        read -p "Enter a filename to save the information: " filename
         if [[ $filename != "" && $filename != *" "* ]]; then
            {
                whois $domain
                dig $domain
                host $domain
                nslookup $domain
            } > $filename
            echo "$filename has been created"
            break
        else 
            echo "Filename cant contain any spaces. Try again."
        fi
    done
fi
}

display_dom
