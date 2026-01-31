# 1.  Takes two numbers as input from the user.
# 2.  Performs the basic mathematical operations on these two numbers:
#   -	Addition
#   -	Subtraction
#   -	Multiplication
#   -	Division
# 3.  Displays the results of each operation on the screen.

Add = lambda num1, num2 : num1 + num2
Subtract = lambda num1, num2 : num1 - num2 if num1 > num2 else num2 - num1
Multiply = lambda num1, num2 : num1 * num2
Divide = lambda num1, num2 : num1 / num2 if num2 != 0 else "Invalid Input"

def validateNumbers(num1, num2):
    if num1 < 0 and num2 < 0:
        return False
    else:
        return True

def main():
    num1 = int(input("Enter the First Number: "))
    num2 = int(input("Enter the Second Number: "))

    if not validateNumbers(num1, num2):
        print("Number Should be Positive")
        return
    
    addition = Add(num1, num2)
    print("Addition : ", addition)

    subtraction = Subtract(num1, num2)
    print("Subtraction : ", subtraction)

    multiplication = Multiply(num1, num2)
    print("Multiplication : ", multiplication)

    division = Divide(num1, num2)
    print("Division : ", division)

if __name__ == "__main__":
    main()