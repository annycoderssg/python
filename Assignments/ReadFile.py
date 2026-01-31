# Task 1: Read a File and Handle Errors 
# Problem Statement:  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.

# I used Files folder to save sample.txt file for this assignment

from sys import argv
from os import path
from FileLibraries import validateFileName, readFileLineByLine

# Read the file and print the content line by line
def readFile(file):
    try:
        if 'Files' not in file:
            file = 'Files/' + file
    
        validateFileName(file)

        isAbsolutPath = path.abspath(file)

        print(f"\nOpen File in Read mode: {file}\n")

        if path.exists(isAbsolutPath):
            readFileLineByLine(file, isAbsolutPath)
            return True
        else:
            print("Error: The is not exists\n")
            return False
            
    except FileNotFoundError:
        print("Error: The file not found\n")
        return False;

# Main function
def main():
    print("\n=============== File Reading Script ===============")

    print("\nScript Name: ", argv[0])

    if len(argv) != 2:
        print("Error: Invalid number of arguments\n")
        exit()
    
    if argv[1] == "-h" or argv[1] == "-H":
        print("Help: This program is used to read a file and print its content line by line\n")
        exit()
    
    if argv[1] == "-u" or argv[1] == "-U":
        print("Usage: python ReadFile.py <file_name> for ex. sample.txt \n")
        exit()
    
    if(readFile(argv[1])):
        print("\nFile read successfully\n")
    else:
        print("\nError: Failed to read file\n")

if __name__ == "__main__":
    main()
    