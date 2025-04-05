# Problem Statement
# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

# Solution

inches_in_foot:int = 12

def main():
    feet: float = float(input("Enter feet to cenvert in inches: "))
    inches: float = feet * inches_in_foot
    print(f"{feet} Feet is equal to {inches} inches.")

main()    
