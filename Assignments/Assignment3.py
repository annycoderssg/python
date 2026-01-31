# Task 1: Check if a Number is Even or Odd
# Problem Statement:  Write a Python program that:
# 1. 	Takes an integer input from the user.
# 2. 	Checks whether the number is even or odd using an if-else statement.
# 3. 	Displays the result accordingly.

def main():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is an Even Number")
    else:
        print(f"{num} is an Odd Number")

if __name__ == "__main__":
    main()
