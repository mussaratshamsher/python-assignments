
# Problem Statement
# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0

# Solution

def main():
    number: float = float(input("Enter a number to get its square: "))
    square:float = number * number
    print(f"The square of {number} is {square}")

main()    