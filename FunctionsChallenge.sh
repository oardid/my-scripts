#!/bin/bash

# Script Name:                  ops201-challenge03-Functions
# Author:                       Omar Ardid
# Date of latest revision:      02/21/2024
# Purpose:                      A function that prints the login history of users on this computer
# Resources:                    https://www.youtube.com/watch?v=ZQrdg32omEk

# Declaration of variables

welcome="This is the login history"

# Declaration of functions
Three_times () {
    last # Terminal command to view history of all logged users
    echo $welcome 
}

# Main

Three_times

# End