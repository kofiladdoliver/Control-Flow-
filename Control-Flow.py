
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
