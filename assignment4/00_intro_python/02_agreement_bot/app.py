

# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

#Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

#What's your favorite animal? cow

# My favorite animal is also cow!

#solution

def main():
    print("🐾 What's your favourite animal?")
    animal: str = input(" ")

    print(f"🐄 My favourite animal is also {animal}!")

main()
