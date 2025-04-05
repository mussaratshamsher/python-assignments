 
# Assignment: 
# Write a python program that guesses a number set in program

# Solution:
import random

def com_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low            
        feedback = input(f'{guess} too high (h), too low (l), or correct (c)  ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback != 'c' and feedback != 'h' and feedback != 'l':
            print("Invalid input. Please enter 'h', 'l', or 'c'.")    
       
    print(f"Hurrah! The computer guessed your number, {guess}, correctly!")

com_guess(10)
