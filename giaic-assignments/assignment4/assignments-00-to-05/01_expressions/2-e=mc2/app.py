# Problem Statement
# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:
# You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.
# E = m * c**2

#solution

C:int = 299792458 # speed of light in m/s

def main():
    mass:float = float(input("Enter mass in kilograms: "))
    energy:float = mass * C ** 2

    # displays work to the user
    print("e = mc^2..")
    print("m =" + str(mass) +" kg")
    print("C =" + str(C) + "m/s")
    print(str(energy) + "joules")
    print(f"energy = {energy} joules" )

main()    

