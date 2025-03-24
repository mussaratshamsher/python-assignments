# Problem Statement
# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.
# Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:
# the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)
# the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)
# the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)
# Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.

# solution

PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():
    user_age = int(input("How old are you?"))

    if user_age >= PETURKSBOUIPO_AGE:
        print("You can vote in Peturksbouipo")
    else:
        print(f"You can't vote in Peturksbouipo where age limit is {PETURKSBOUIPO_AGE}")

    if user_age >= STANLAU_AGE:
        print("You can vote in Stanlau")
    else:
        print(f"you can't vote in Stanlau where age limit is {STANLAU_AGE}")

    if user_age >= MAYENGUA_AGE:
        print("You can vote in Mayengua.")
    else:
        print(f"You can't vote in Mayengua where age limit is {MAYENGUA_AGE}")

main()                       