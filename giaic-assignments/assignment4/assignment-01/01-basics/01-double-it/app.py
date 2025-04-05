
# Problem Statement
# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. 
# It will repeat that process until the value is 100 or greater.

# Solution

def double_number(curr_number):
    """ Doubles a number repeatedly until it's greater than 100, printing each doubled value. """
    while curr_number < 100:  
        curr_number = curr_number * 2
        if curr_number >= 100:
            break
        print(curr_number)

def main():
    """ Gets user input and calls double_number. """
    input_number = int(input("Enter a number: "))
    double_number(input_number)

main()

