"""
Python calculator
calculator written in python
by chaim hayes
"""
#Open ended while loop for testing code, "CTRL+C" to exit
#inf=1
#while inf==1:

userInput = input("For Addition: 1\nFor Subtraction: 2\nChoice: ")

if userInput == "1":
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    print(a+b)
elif userInput == "2":
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    print(a-b)
else:
    print("Invalid Input")