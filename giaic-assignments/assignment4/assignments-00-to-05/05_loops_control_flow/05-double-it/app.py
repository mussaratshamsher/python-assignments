# Problem Statement
# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

# Solution

def main():
    user_num = int(input("Please enter a number less than or equal to 100: "))
    while user_num < 100:
        user_num *= 2
        print(user_num)             

main()       
