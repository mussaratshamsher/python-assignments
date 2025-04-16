

# Problem Statement
# write a helper function for you called greet(name) which takes as input a string name and prints a greeting. 
# Write some code in main() to get the user's name and then greet them, being sure to call the greet(name) helper function.

 # Solution:

def greet(name):
    print(f"Hello! {name} how are you?")

def main():
    name = input("Write down name here: ") 
    greet(name)


main()       


