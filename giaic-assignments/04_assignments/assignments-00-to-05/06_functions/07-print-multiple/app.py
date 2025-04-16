

# Problem Statement
# Fill out print_multiple(message, repeats), which takes as parameters a string message to print, and an integer repeats number of times to print message.

# Solution:

def multi_msg(msg: str, repeats: int):

    for i in range(repeats):
        print(msg)

def main():
    message = input("Please enter message to print: ")
    repeats = int(input("Enter number of repeats: ")) 
    multi_msg(message, repeats)

main()           
