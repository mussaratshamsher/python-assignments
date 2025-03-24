# Problem Statement
# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.'

# Solution

MINIMUM_HEIGHT: int = 50

def main():
    height = float(input("How tall are you in cm?"))
    if height >= MINIMUM_HEIGHT:
        print("You are tall enough to ride.")
    else:
        print("you'r not tall enough to ride❗")  

main()          
