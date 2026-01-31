# Problem Statement: Write a Python program that:
# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list

def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Original list: ", nums)
    print("Extracted first five elements: ", nums[0:5])
    print("Reversed extracted elements: ", nums[::-1])
    print("\n")

if __name__ == "__main__":
    main()