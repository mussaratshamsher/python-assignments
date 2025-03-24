
# Mutable data types

# Solution

def add_three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)


def main():
    message = input("Enter a message to copy:")
    my_list = []
    print("list before:", my_list)
    add_three_copies(my_list, message) 
    print("List after:", my_list)
    
main()
        