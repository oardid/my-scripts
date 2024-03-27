#!/bin/bash

# Script Name:                  ops301-challenge02
# Author:                       Omar Ardid
# Date of latest revision:      03/27/2024
# Purpose:                      Appends the current date and time to the filename

# Declaration of variables

today=$(date +%m-%d-%Y~%H:%M:%S)

# Copying system logs and adding today date on the file name
cp /var/log/syslog ./syslog.$today
