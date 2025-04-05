
# Problem Statement
# Implement the following function which takes in 3 integers as parameters:

# def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """
    
def  in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True
    else:
        return False

def main():
    n = int(input("Enter a nubmer: "))
    print(in_range(n, 10, 20))    

main()