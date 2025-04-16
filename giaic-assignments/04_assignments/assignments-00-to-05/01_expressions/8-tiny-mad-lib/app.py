# Problem Statement
# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!
    
# solution

sentence_start: str = "Panaversity is fun. I learned to program and used Python to make my"

def main():
    # 3 inputs from the user to make the madlib
    adjective: str =input("Type an adjective & press enter: ")
    noun: str = input("Tpye a noun & press enter: ")
    verb: str = input("Type a verb & press enter: ")
    print(f"{sentence_start} {adjective} {noun} {verb} ❗")

main()