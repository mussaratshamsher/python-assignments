# Problem Statement
# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!
# consider a right triangle ABC, with the right angle located at C. According to the Pythagorean theorem:

# BC ** 2 = AB ** 2 + AC ** 2    

# solution
import math

def main():
    ab:float = float(input("enter the length of side of AB: "))
    ac:float = float(input("Enter the length of side of AC:"))

    # Calculating the length of BC(hypotenuse)
    bc:float = math.sqrt(ab**2 + ac**2) 
    print(f"The length of BC (hypotenuse) is {bc}")

main()    
