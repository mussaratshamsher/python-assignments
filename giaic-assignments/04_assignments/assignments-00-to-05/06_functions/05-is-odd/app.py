

# Problem Statement
# Check out odd numbers

# Solution:

def is_odd(value: int):
    remainder = value %2
    return remainder == 1

def main():
    for i in range(10):
        if is_odd(i):
            print(i ,": Odd Number")
        else:
            print(i, ": Even Number")
                

main()     
    