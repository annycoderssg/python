Add = lambda num1, num2 : num1 + num2
Subtract = lambda num1, num2 : num1 - num2 if num1 > num2 else num2 - num1
Multiply = lambda num1, num2 : num1 * num2
Divide = lambda num1, num2 : num1 / num2 if num2 != 0 else "Invalid Input"

def main():
    num1 = int(input("Enter the First Number: "))
    num2 = int(input("Enter the Second Number: "))
    
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