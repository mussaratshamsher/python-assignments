# Problem statement
# Write a program that doubles each element in a list of numbers. For example, if you start with this list:
# numbers = [1, 2, 3, 4]
# You should end with this list:
# numbers = [2, 4, 6, 8]

# Solution
def main(): 
    numbers = [1,2,3,4,5]

    for i in range(len(numbers)):
      numbers[i] = numbers[i]* 2
    print(numbers)

main()