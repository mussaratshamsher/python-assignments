# Problem Statement
# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, '
# 'you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were'
# ' available and how much one of each fruit costs.
# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit 
# they want to buy, and then prints out the total combined cost of all of the fruits.

# Solution

def main():
    fruits = {'apple': 20, 'kiwi': 15, 'guava': 4.5, 'orange': 6.5, 'grapes': 30}

    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input(f"How many {fruit_name} do you want to buy?"))
        total_cost += (price * amount_bought)

    print("You will pay $", total_cost) 

main()       
