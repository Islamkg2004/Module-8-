# Name: Islam Syndanbekov
# Date: November 11, 2026
# Problem 2
# Check if the sum of two numbers is greater than,
# less than, or equal to 10.

def problem2():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    total = num1 + num2

    if total > 10:
        print("The sum is greater than 10.")
    elif total < 10:
        print("The sum is less than 10.")
    else:
        print("The sum is equal to 10.")