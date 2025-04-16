
# Problem Statement
# Print 10 random numbers in the range 1 to 100.

# Solution

import random

def main():
    for _ in range(10):
        value = random.randint(1, 100)
        print(value)

main()
        