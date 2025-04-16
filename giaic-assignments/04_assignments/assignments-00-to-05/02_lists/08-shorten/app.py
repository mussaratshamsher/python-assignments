# Problem Statement
# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and 
# prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH 
# you should leave it unchanged.

# Solution

MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(last_elem)

def get_lst():
    """ Prompts the user to enter one element of the list at a time & return resulting list.
    """        
    lst = []

    elem = input("Please enter one element of the list: ")
    while elem != "":
       lst.append(elem)
       elem = input("Please enter one element of the list or press enter to see result: ")

    return lst

def main():
    lst = get_lst()
    shorten(lst)

main()
