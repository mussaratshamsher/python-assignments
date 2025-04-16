# Problem Statement
# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the 
# first element in the list. The list is guaranteed to be non-empty. 

# solution

def get_first_element(lst):
    """
    Prints the first element of a non-empty list.
    Args:
        lst: A non-empty list.
    """
    print(lst[0])

# Example Usage 
my_list = [1, 2, 3, 4, 5]
get_first_element(my_list)  # Output: 1

my_list2 = ["apple", "banana", "cherry"]
get_first_element(my_list2) # Output: apple
