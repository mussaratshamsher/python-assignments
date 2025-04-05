

# Problem Statement
# Guess My Number
# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Solution: 

import random

import random

def main():
    secret_number: int = random.randint(0, 99)

    print("I am thinking of a number b/w 0 & 99...")

    guess = int(input("Enter a guess: "))
    while guess != secret_number:
        if guess > secret_number:
            print("Your guess is too high!")
        else:
            print("Your guess is too low..")
        guess = int(input("Enter a guess: "))  # Get a new guess inside the loop

    print("Correct answer!")  # Moved outside the loop

main()
                
    

