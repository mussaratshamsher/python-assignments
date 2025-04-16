
# Problem Statement
# Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder)
# operator, %, should be helpful to you here.Call your function from main()!

# Solution

def ones_digit(num):
    print("The ones in digit is: ", num % 10)

def main():
    num = int(input("enter a number: "))
    ones_digit(num)

main()        

