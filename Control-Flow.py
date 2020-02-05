
name = input("\nWhat is your name: ")

# Greeting Function
def greeting():
    print("Hello " + name)
    print(name + " that's a cool name!!")

print("\n----Greetings Funtion----\n")
greeting()


#Programmer: Commander Kofi Ladd-Oliver
#Date: 12.16.19
#Program: Guess My Number

total = 0
how_many_tests = int(input("How many tests would you like to average: "))
print("")

for i in range(how_many_tests):
    enter_a_score = int(input("Enter a score: "))
    total = total + enter_a_score
    avg = total / how_many_tests
print("\nAverage: " + str(round(avg, 2)))

# programmer: Mr kofee
#date: 1-20-20
#program: Double For Loop

for i in range(3):
    print("Outer ForLoop" + str(i))
    for k in range(4):
        print("\tInner ForLoop" + str(k))

print("\n************************\n")
"""
Programmer: Kofee
Date: 1.23.20
program: While Loop nested inside of a ForLoop
"""

for i in range(4):
    print("ForLoop: "+ str(i))
    x = i
    while x >= 0:
        print("\tWhile Looop: "+ str(x))
        x = x - 1
        print()

# Date: 2.3.20
# Programmer; Kofi Ladd-Oliver
# Global Varibles here


x = 15


# create Functions here....



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

print("\n****Thank you****")





