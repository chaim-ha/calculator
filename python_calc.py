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
 
    n = 5
    while n > 3:
        
        userInput = input("+ - / *\nChoice: ")

        if userInput == "+":
            a = int(input("Enter number: "))
            print(a+b)
            n = 1
        elif userInput == "-":
            a = int(input("Enter number: "))
            print(a-b)
            n = 1
        elif userInput == "/":
            a = int(input("Enter number: "))
            print(a/b)
            n = 1
        elif userInput == "*":
            a = int(input("Enter number: "))
            print(a*b)
            n = 1
        else:
            print("Invalid Input, please choose + - / or *")
            n = 5
main()
input("Press enter to close")