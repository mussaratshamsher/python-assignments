
# Problem Statement
# Fill out the function count_even(lst) which
# first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),
# and then prints the number of even numbers in the list.

# Solution:

def count_even(lst):
    """Counts the number of even numbers in a list."""
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    print("Number of even numbers:", count)  

def get_list_of_int():
    """Prompts the user for integers until they press enter and returns a list of integers."""
    lst = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break  
        try:
            num = int(user_input)
            lst.append(num)
        except ValueError:
            print("Invalid input. Please enter an integer or press enter.")
    return lst

def main():
    """Main function to get the list and count even numbers."""
    lst = get_list_of_int()
    count_even(lst)

main()

