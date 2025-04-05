# Problem Statement
# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements

# Solution

def main2():
    """Prints the first 20 even numbers using a loop and step in range."""
    for i in range(2, 21, 2): # start at 2, go up to (but not including) 21, step by 2
        print(i)
main2()        
         
