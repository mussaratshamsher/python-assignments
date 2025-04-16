# Problem Statement
# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

# Solution

def main():
    list = [] # stores values

    val = input("Enter a value: ")
    while val:
         list.append(val)
         val = input("Enter a vlaue: ")
    print(" Here's the list:", list)  

main()
        
