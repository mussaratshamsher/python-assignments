
# Assignment: Mad libs game

def mad_libs():
    """
    Generates a Mad Libs story based on user input.
    """
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb (present tense): ")
    adjective2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")
    verb2 = input("Enter another verb (past tense): ")
    noun3 = input("Enter one more noun: ")

    madlib = f"The {adjective1} {noun1} decided to {verb1} through the forest. It was a very {adjective2} day. Suddenly, a giant {noun2} appeared and {verb2} towards the {noun3}!"

    print(madlib)

mad_libs()

