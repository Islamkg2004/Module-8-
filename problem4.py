# Your Name: Islam Syndanbekov
# Date: November 11, 2026
# Program: Module 8 - Lab Activity: Booleans
# Problem 4
# Check if a year is a leap year.

def problem4(year):

    if year % 400 == 0:
        print("True")
    elif year % 100 == 0:
        print("False")
    elif year % 4 == 0:
        print("True")
    else:
        print("False")


# Test
problem4(2024)
problem4(1900)
problem4(2000)
problem4(2023)
