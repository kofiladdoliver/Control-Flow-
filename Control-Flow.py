
# Date: 2.3.20
# Programmer; Kofi Ladd-Oliver
# Global Varibles here

# name = input("\nWhat is your name: ")

x = 15


# create Functions here....

# Greeting Function
def greeting():
    print("Hello " + name)
    print(name + " that's a cool name")

    # Functions & Local Variable x
def printSomething():
    x = 3
    print(x)

# Functions & Parameters
def printNumber(age): # Function name = printNumber with a Parameter of age
    print(age)

# Default Parameter Value
def printTwoNumber(x, y = 71):
    print("First Parameter: " + str(x))
    print("Second Parameter: " + str(y))

# Print Sum
def printSum(x, y):
    print(x + y)

# call function here...

# greeting()
# printSomething()
# print(x)
# printNumber(28)
# printNumber(38)
# printTwoNumber(23, 78)
# printTwoNumber(45)
printSum(1, 17)





