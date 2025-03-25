# Problem Statement
# Guess My Number
# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high
# Enter a new number: 25 Your guess is too low
# Enter a new number: 40 Your guess is too low
# Enter a new number: 45 Your guess is too low
# Enter a new number: 48 Congrats! The number was: 48

#solution

import random

def main():
    secret_number = random.randint(1, 99)
    print("I am thinking of a number between 1 & 99...")

    while True: 
        guess = int(input("Enter your guessed number here: "))

        if guess > secret_number:
            print("❌ Your guess is too high!")
        elif guess < secret_number:
            print("❌ Your guess is too low!")
        else:
            print(f"✅ Congrats! {secret_number} is the correct number!")
            break 

main()
