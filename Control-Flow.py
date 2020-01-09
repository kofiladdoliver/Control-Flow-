"""
Programmer: Commander Kofi Ladd-Oliver
Date: 12.16.19
Program: Guess My Number
"""
total = 0
how_many_tests = int(input("How many tests would you like to average: "))
print("")

for i in range(how_many_tests):
    enter_a_score = int(input("Enter a score: "))
    total = total + enter_a_score
    avg = total / how_many_tests
print("\nAverage: " + str(round(avg, 2)))
