"""
Programmer: Commander Kofi
Date: 12.16.19
Program: Guess My Number
"""

my_number = 10

# Ask the user to guess
guess = int(input("\nEnter a guess: "))

# Keep asking until the guess becomes equal to the secret number
while guess != my_number:
    print ("Your an idiot\n")
    guess = int(input("Try Again Stupid: "))
print ("\nLet me poop in your mouth")
