"""
Python calculator
calculator written in python
by chaim hayes
"""
#Open ended while loop for testing code, "CTRL+C" to exit3
#inf=1
#while inf==1:

def main():

    b = int(input("Enter number: "))
    a = int(input("Enter number: "))

    userInput = input("1 for Addition\n2 for Subtraction\n3 for Division\n4 for Multiplication\nChoice: ")
    
    if userInput == "1":
        print(a+b)
    elif userInput == "2":
        print(a-b)
    elif userInput == "3":
        print(a/b)
    elif userInput == "4":
        print(a*b)
    else:
        print("Invalid Input, please choose 1 2 3 or 4")

main()