#!/bin/bash

# Script Name:                  ops301-challenge05
# Author:                       Omar Ardid
# Date of latest revision:      03/29/2024
# Purpose:                      Create a bash script that clears log files for you
# Source:                       https://github.com/codefellows/seattle-ops-301d12/blob/main/class-05/challenges/DEMO.md

# Variables
BACKUP_DIR="backups"
LOG_FILES=("/var/log/syslog" "/var/log/wtmp")

menu(){
    while true; do
        clear
        echo "~~~ Log Menu ~~~"
        echo "1. Copy, compress, and compare /syslog and /wtmp files."
        echo "2. Clear the contents of a log file."
        echo "3. Exit."
        read -p "Enter your choice: " choice

        if [[ $choice == 1 ]]; then
            echo "Creating a backup directory."
            mkdir -p "$BACKUP_DIR" # Creates the backup directory if it doesn't exist
            echo "Copying and compressing log files..."
            echo " "
            TIMESTAMP=$(date +%Y-%m-%d~%H:%M:%S)
            for file in "${LOG_FILES[@]}"; do
                FILE_SIZE=$(wc -c "$file" | awk '{print $1}') 
                FILE_NAME=$(basename "$file")
                zip -r "$BACKUP_DIR/$FILE_NAME-$TIMESTAMP.zip" "$file" 
                echo "Compressed $file to $BACKUP_DIR/$FILE_NAME-$TIMESTAMP.zip"
                ORIGINAL_SIZE=$(wc -c "$file" | awk '{print $1}')
                COMPRESSED_SIZE=$(wc -c "$BACKUP_DIR/$FILE_NAME-$TIMESTAMP.zip" | awk '{print $1}')
                echo "File: $file, Original size: $ORIGINAL_SIZE, Compressed size: $COMPRESSED_SIZE"
                if [[ $FILE_SIZE -gt $COMPRESSED_FILE_SIZE ]]; then
                    echo "Compression successful: Compressed file size is smaller than original file size!"
                    echo " "
                else
                    echo "Compression unsuccessful: Compressed file size is larger than original file size!"
                fi
            done
            read -p "Press Enter to continue."
        elif [[ $choice == 2 ]]; then
            read -p "Enter the log file you want to clear: " file
            cat /dev/null > "$file" 
            echo "Log $file has been cleared."
            read -p "Press Enter to continue."
        elif [[ $choice == 3 ]]; then
            exit 0 
        else    
            echo "Invalid input. Please enter a number from 1 to 3."
            read -p "Press Enter to continue."
        fi
    done
}
menu
