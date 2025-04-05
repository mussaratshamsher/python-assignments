
#Problem Statement
# There are times where you are working with lots of different data within a function that you want to return.
#  While generally, we want to keep functions to have a precise purpose, sometimes that purpose just deals with
#  multiple bits of data.
# To practice this, imagine we are working on a program where the user needs to enters data to sign up for a website.
#  Fill out the get_user_data() function which:

# Asks the user for their first name and stores it in a variable
# Asks the user for their last name and stores it in a variable
# Asks the user for their email address and stores it in a variable
# Returns all three of these pieces of data in the order it was asked

# Solution

def user_data():
    first_name = input("Enter your first name: __")
    last_name = input("Enter your last name: -__")
    email_address = input("Enter your email address: __")

    return first_name, last_name, email_address

def main():
    print(user_data())

main()    


