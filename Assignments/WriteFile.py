# Task 2: Write and Append Data to a File
# Problem Statement: Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.

# I used Files folder to save output.txt file for this assignment

from sys import argv
from os import path

from FileLibraries import validateFileName, readFileLineByLine

# Read the file and print the content line by line
def writeFile(file):

    try:
        if 'Files' not in file:
            file = 'Files/' + file
    
        validateFileName(file)

        isAbsolutPath = path.abspath(file)

        print(f"\nOpen file in Write mode: {file}")

        if not path.exists(isAbsolutPath):
            print("\nError: The is not exists")
            return False
        
        fpWrite = open(isAbsolutPath, "w")
        data = input("\nEnter text to write to the file: ")
        fpWrite.write(data + "\n")

        data = input("\nEnter additional text to append: ")
        fpWrite.write(data + "\n")
        
        fpWrite.close()

        # Read the file and print the content line by line
        readFileLineByLine(file, isAbsolutPath)

        return True
            
    except FileNotFoundError:
        print("\nError: The file not found or unable to open")
        return False;

# Main function
def main():
    print("\n=============== File Reading Script ===============")

    print("\nScript Name: ", argv[0])

    if len(argv) != 2:
        print("\nError: Invalid number of arguments")
        exit()
    
    if argv[1] == "-h" or argv[1] == "-H":
        print("\nHelp: This program is used to read a file and print its content line by line")
        exit()
    
    if argv[1] == "-u" or argv[1] == "-U":
        print("\nUsage: python ReadFile.py <file_name> for ex. output.txt")
        exit()
    
    if(writeFile(argv[1])):
        print("\nFile Operation is completed")
    else:
        print("\nError: Failed to open file")

if __name__ == "__main__":
    main()
    