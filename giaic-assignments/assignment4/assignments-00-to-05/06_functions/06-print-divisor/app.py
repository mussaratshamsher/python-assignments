
# Problem Statement
# Write the helper function print_divisors(num), which takes in a number and prints all of its divisors

# Solution:

def divisors(num: int):
    print(f"The divisors of {num} are:")
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print(curr_divisor)

def main():
    user_num = int(input("Enter a number: "))
    divisors(user_num)            

main()