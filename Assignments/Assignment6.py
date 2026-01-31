# Task 2: Using the Math Module for Calculations
 
# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
#   -   Square root of the number
#   -   Natural logarithm (log base e) of the number
#   -   Sine of the number (in radians)
# 3.   Displays the calculated results.

import math

def main():
    num = int(input("Enter a number: "))
    print(f"Square root : {math.sqrt(num)}")
    print(f"Logarithm: {math.log(num)}")
    print(f"Sine: {math.sin(num)}")

if __name__ == "__main__":
    main()
