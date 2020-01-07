"""
Programmer: Commander Kofi
Date: 12.16.19
Program: Guess My Number
"""

sum = 10
how_many_numbers = int(input("How many numbers you want to sum: "))

for i in range(how_many_numbers):
    enter_a_number = int(input("\nEnter a number: "))
    sum = sum + enter_a_number

print("\nSum of your numbers is : " + str(sum))