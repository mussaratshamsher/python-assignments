

# Problem Statement
# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with 
# decimal places!) and outputs the temperature converted to Celsius.

# Solution

def main():
    print("🌡️ Enter the temperature in Fahrenheit:")
    fahrenheit: str = input("") 
    fahrenheit = float(fahrenheit)
    celsius: float = (fahrenheit - 32) * 5/9
    print(f"🌡️ The temperature in Celsius is: {celsius}")

main()