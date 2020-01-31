
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
