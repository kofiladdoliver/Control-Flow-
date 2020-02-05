
# Date: 2.3.20
# Programmer; Kofi Ladd-Oliver
# Global Varibles here

name = input("\nWhat is your name: ")

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

# print multiplue Times
def printMultiplueTimes(string, times):
    for i in range(times):
        print(string)


# call function here...
print("\n----Greetings Funtion----\n")
greeting()

print("\n----Print Something Function----\n")
printSomething()

# print(x)
print("\n----Print Number Funtion----\n")
printNumber(28)
printNumber(38)

print("\n----Print Two Numbers Function----\n")
printTwoNumber(23, 78)

print("\n----Default Parameter Values Function----\n")
printTwoNumber(45)

print("\n----print Sum Function----\n")
printSum(1, 17)

print("\n----Print Multiplue Times Function----\n")
printMultiplueTimes("I love rocks", 2)

print("\n----Thanks for being a test dummy----")




