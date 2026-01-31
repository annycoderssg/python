# Task 1: Calculate Factorial Using a Function 
# Problem Statement: Write a Python program that:
# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# 2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

def main():
    try:
        user_input = input("Enter a number: ")
        num = int(user_input)

        if num < 0:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            result = factorial(num)
            print(f"Factorial of {num} is: {result}")

    except ValueError:
        print("Invalid input! Please enter a whole number (e.g., 5).")

if __name__ == "__main__":
    main()