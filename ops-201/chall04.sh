#!/bin/bash

# Script Name:                  ops201-challenge04-Arrays
# Author:                       Omar Ardid
# Date of latest revision:      02/22/2024
# Purpose:                      Create a script that creates four directories and create a new .txt file in each directory
# Resources:                    




directories(){
    dir=("dir1" "dir2" "dir3" "dir4")
    files=("file1" "file2" "file3" "file4")
    echo "Creating directory ${dir[0]} with .txt ${files[0]} inside" 
    mkdir dir1
    cd ./dir1/
    touch file1
    echo "Creating directory ${dir[1]} with .txt ${files[1]} inside"
    cd ..
    mkdir dir2
    cd ./dir2/
    touch file2
    echo "Creating directory ${dir[2]} with .txt ${files[2]} inside"
    cd ..
    mkdir dir3
    cd ./dir3/
    touch file3
    echo "Creating directory ${dir[3]} with .txt ${files[3]} inside"
    cd ..
    mkdir dir4
    cd ./dir4/
    touch file4
}
directories 

