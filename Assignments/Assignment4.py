# Sum of Integers from 1 to 50 Using a Loop
# Problem Statement: Write a Python program that:
# 1.   Uses a for loop to iterate over numbers from 1 to 50.
# 2.   Calculates the sum of all integers in this range.
# 3.   Displays the final sum.

def main():
    sum = 0
    limit = 51
    for i in range(1, limit):
        sum += i
    print(f"Sum of Integers from 1 to 50 is : {sum}")

if __name__ == "__main__":
    main()
