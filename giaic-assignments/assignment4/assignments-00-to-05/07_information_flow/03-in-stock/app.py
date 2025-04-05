# Problem Statement
# Sophia has a fruit store. She has written a function num_in_stock which takes a string fruit as a parameter and returns how many of that fruit are in her inventory. Write code in main() which will:

# Prompt the user to enter a fruit ("Enter a fruit: ")

# Call num_in_stock(fruit) to get the number of that fruit that Sophia has in stock

# Print the number which are in stock if Sophia has that fruit in her inventory (there are more than 0 in stock)

# Print "This fruit is not in stock." if Sophia has none of that fruit in her inventory.

# Solution

def num_in_stock(fruit):
    if fruit == "banana":
        return 12
    elif fruit == "apple":
        return 0
    elif fruit == "orange":
        return 40
    elif fruit == "pear":
        return 10
    elif fruit == "grapes":
        return 20

def main():

    print("banana, apple, orange, pear, grapes")
    fruit = input("Enter fruit from the list to check stock:  ")
    
    print(num_in_stock(fruit))


main()