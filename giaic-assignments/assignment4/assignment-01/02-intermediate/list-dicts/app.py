
#Problem #1: List Practice
# Print the length of the list.
# Add 'mango' at the end of the list. 
# Print the updated list.

# Problem #2: Index Game
# Create a Python program that helps you practice accessing and manipulating elements in a list. This exercise will help you get comfortable with indexing, slicing, and modifying list elements.
    
# Solution: List Practice

def main():
   fruit_lst = ['apple', 'banana', 'cherry', 'grapes'] 
   # length of list
   print("Length of the list: ", len(fruit_lst))
# adding mango at the end of list
   fruit_lst.append('mango')
   print(fruit_lst)

main()

# Solution 2: Index Game Solution

def access_element(lst, index):
   try:
      return lst[index]
   except IndexError:
      return "Index out of range."

def modify_element(lst, index, new_value):
   try:
      lst[index] = new_value
      return lst
   except IndexError:
      return "Index out of range."

def slice_list(lst, start, end):
   try:
      return lst[start:end]
   except IndexError:
      return "Invalid indices." \
      
def index_game():
   lst = [1, 2, 3, 4, 5]
   print("Origional list", lst)
   print('Choose an operation: access, modify, slice')
   operation = input("Enter an operation: ")
      
   if operation == "access":
       index = int(input("Enter index to access:"))
       print(access_element(lst, index))
   elif operation == "modify":
      index = int(input("Enter index to modify: "))
   elif operation == "slice":
      start = int(input("Enter start index: "))
      end = int(input("Enter end index: "))
      print(slice_list(lst, start, end))
   else:
      print("Invalid operation.")  

index_game()          
