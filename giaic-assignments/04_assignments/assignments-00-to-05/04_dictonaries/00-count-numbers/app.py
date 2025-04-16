# Problem Statement
# Write a  program that counts the number of times each number appears in a list.
#  It uses a dictionary to keep track of the information.
# The program should take input from the user.

# Solution

def count_number_occurrences(numbers):
    """
    Counts the number of times each number appears in a list.
    Args:numbers: A list of numbers.
    Returns:A dictionary where keys are the numbers and values are their counts.
    """
    counts = {}  # Initialize an empty dictionary to store counts

    for number in numbers:
        if number in counts:
            counts[number] += 1  # Increment count if number already exists
        else:
           counts[number] = 1  # Add number to dictionary with count 1 if it's new
    return counts

def get_number_list_from_user():
    user_numbers = []
    while True:
        user_input = input("Enter a number:")
        if user_input == "":
            break
        num = int(user_input)
        user_numbers.append(num)
    return user_numbers

def main():
    # Get the list of numbers from the user
    number_list = get_number_list_from_user()
    # Count the occurrences of each number
    occurrences = count_number_occurrences(number_list)
   
    print("\nNumber Occurrences:")
    for number, count in occurrences.items():
        print(f"{number} \t:  {count}")

main()

