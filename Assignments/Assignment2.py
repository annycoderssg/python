# Write a Python program that:
# 1.  Takes a user's first name and last name as input.
# 2.  Concatenates the first name and last name into a full name.
# 3.  Prints a personalized greeting message using the full name.

def main():
    firstName = input("Enter a your first name: ")
    lastName = input("Enter a your last name: ")
    print("Hello, " + firstName + " " + lastName + "! Welcome to Python Program.")

if __name__ == "__main__":
    main()