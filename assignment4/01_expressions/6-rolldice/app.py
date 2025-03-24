# Problem Statement
# Simulate rolling two dice, and prints results of each roll as well as the total.

# Solution

import random
num_sides = 6

def main():
    die1: int = random.randint(1, num_sides)
    die2:int = random.randint(1, num_sides)
    total:int = die1 + die2
    print(f"Dice have {num_sides} sides.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice is {total}")

main()    
