import re

# Validate the file name
# Function accepts the file name as argument
def validateFileName(file):
    if re.search(r'[^\w\s/.]', file):
        print("\nError: The file name contains special characters")
        exit()
    if re.search(r'\s', file):
        print("\nError: The file name contains spaces\n")
        exit()
    return True

# Read the file and print the content line by line
# Function accepts the file name and file path as arguments
def readFileLineByLine(fileName, filePath):
    
    print(f"\nOpen file in Reading mode: {fileName}\n")
    
    fpRead = open(filePath, "r")
    lines = fpRead.readlines()
    
    for line_number, line in enumerate(lines, start=1):
        print(f"Line {line_number}: {line}")

    fpRead.close()

    return True    
