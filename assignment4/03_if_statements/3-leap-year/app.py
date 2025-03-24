# Problem Statement
# Write a program that reads a year from the user and tells whether a given year is a leap year or not.

# Solution

def main():
    year = int(input('Please input a year: '))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"✅That's a leap year.")
            else:
                print(f"❌That's not a leap year!")
        else:
            print(f"❌That's a leap year!")
    else:
        print(f"❌That's not a leap year!")

main()                    
