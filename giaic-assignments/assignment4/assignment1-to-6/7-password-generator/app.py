

# Assignment : Password Generator

# Solution:

import random

print("Welcome to the Password Generator!")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_,.?0123456789"

number = int(input('Amount of passwords to generate: '))

length = int(input('Length of each password: '))

print('Password are following: \n')

for pswd in range(number): # loop for number of passwords
    passwords = '' # to store the password
    for c in range(length): # loop for length of password
        passwords += random.choice(chars) # to choose a random character from chars
    
    print(passwords)
