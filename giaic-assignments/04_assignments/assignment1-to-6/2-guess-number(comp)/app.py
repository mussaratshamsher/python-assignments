

# Assignment: gess number game(computer)
# Write a python program that generates a random number and user guess it till did not guess the 
#  correct number

# Solution:

import random

random_num = random.randint(0, 10)

def guess_num():
    guess = 0
    while guess != random_num:
        guess = int(input("Guess the number between 0 and 10: "))
        if guess > random_num:
            print("you guessed too high number")
        elif guess < random_num:
            print("Your guess is too low.")
        else: 
            print("Congratulations! You guessed the correct number.")
        
guess_num()


