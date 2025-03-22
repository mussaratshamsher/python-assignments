
# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# Prompt the user to enter the first number.

# Read the input and convert it to an integer.

# Prompt the user to enter the second number.

# Read the input and convert it to an integer.

# Calculate the sum of the two numbers.

# Print the total sum with an appropriate message.

#  ✅solution

def main():
     print("📌You can add two numbers here")
     num1: str = input("Enter the first number: ")
     num1 = int(num1)
     num2: str = input("Enter the second number: ") 
     num2 = int(num2)
     total: int = num1 + num2
     print(f"⭕The sum of given numbers are: {total}")
main()


