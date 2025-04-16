# Problem Statement
# Write a function that takes a list of numbers and returns the sum of those numbers.

# Solution

def add_many_num(numbers) -> int:
    """ takes in a list of numbers & returns the sum of those numbers.
    """
    total: int = 0
    for num in numbers:
        total += num
    return total

def main():
    numbers: list[int] = [1,2,3,4,5]
    print(add_many_num(numbers))

main()

