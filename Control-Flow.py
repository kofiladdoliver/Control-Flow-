# Date: 2.3.20
# Greeting Function
# Global Varibles here

name = input("\nWhat is your name: ")

x = 15


# create Funtions here
def greeting():
    print("Hello " + name)
    print(name + " thats a cool name")
    print(x)

def printSomething():
    x = 3
    print(x)
# call function here

greeting()
printSomething()
print(x)