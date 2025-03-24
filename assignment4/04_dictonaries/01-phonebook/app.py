
# Problem Statement
# Write a program using dictionaries to keep track of information in a phonebook.

# solution

def read_phone_numbers():
    phonebook = {}
    while True:
        name = input("Name:")
        if name == "":
            break
        number = input("Number:")
        phonebook[name] = number
    return phonebook

def print_phonebook(phonebook):
   print("\nPhonebook:")
   for name in phonebook:
       print(f"{name}  : {phonebook[name]}")     

def lookup_numbers(phonebook):
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(f"{name} is not in the phonebook.")
        else:
            print(f"{name} : {phonebook[name]}") 

def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

main()
                