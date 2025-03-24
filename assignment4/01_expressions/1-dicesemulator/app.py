# Problem Statement
# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

#solution

import random

num_sides = 6

def roll_dice():
    """Rolling two dice and return their face values."""
    die1: int = random.randint(1, num_sides)
    die2: int = random.randint(1, num_sides)
    total: int = die1 + die2
    print("Total of two dice is ", total)

def main():
    die1: int = 10
    print("die1 in main() starts as:" +str(die1))
    roll_dice()
    roll_dice()
    roll_dice()
    print("die1 in main() is now:" +str(die1))

main()

