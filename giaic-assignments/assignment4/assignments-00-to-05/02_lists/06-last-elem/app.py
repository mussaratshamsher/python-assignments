# Problem Statement
# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints
# the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

# Solution

def get_last_element(lst):
    """
    Prints the last element of a non-empty list.
    Args:
        lst: A non-empty list.
    """
    print(lst[-1])

# Example Usage 
my_list = [1, 2, 3, 4, 5]
get_last_element(my_list)  # Output: 5

my_list2 = ["a", "b", "c", "d"]
get_last_element(my_list2) # Output: d

