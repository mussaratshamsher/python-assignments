
# Problem: Planetary Weight Calculator
# Milestone #1: Mars Weight
# Write a Python program that prompts an Earthling to enter their weight on Earth and prints their calculated weight 
# on Mars.
# Milestone #2: 
# Write a Python program that prompts an Earthling to enter their weight on Earth and then to enter the name of a 
# planet in our solar system. The program should print the equivalent weight on that planet rounded to 2 decimal 
# places if necessary.

# Solution: Milestone 1:

MARS_MULTIPLE = 0.378

def main():

    #get numeric value & returns in string
    earth_weight = float(input('Enter a weight on the Earth: '))
    
    mars_weight = earth_weight * MARS_MULTIPLE
    rounded_mars_weight = round(mars_weight, 2)

    # Note the string concatenation!
    print('The equivalent weight on Mars: ' + str(rounded_mars_weight))

main()    

# Solution: Milestone 2:

MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378 
JUPITER_GRAVITY = 2.36 
SATURN_GRAVITY = 1.081 
URANUS_GRAVITY = 0.815 
NEPTUNE_GRAVITY = 1.14 
EARTH_GRAVITY = 1.0

def main2():
    earth_weight = float(input('Enter a weight on the Earth: '))
    planet = input('Enter the name of a planet: ').lower

    if planet == 'mercury':
        gravity_constant = MERCURY_GRAVITY
    elif planet == 'venus':
        gravity_constant = VENUS_GRAVITY
    elif planet == 'mars':
        gravity_constant = MARS_GRAVITY
    elif planet == 'jupiter':
        gravity_constant = JUPITER_GRAVITY
    elif planet == 'saturn':
        gravity_constant = SATURN_GRAVITY
    elif planet == 'uranus':
        gravity_constant = URANUS_GRAVITY
    elif planet == 'neptune':
        gravity_constant = NEPTUNE_GRAVITY
    else:
        gravity_constant = EARTH_GRAVITY

    planetary_weight = earth_weight * gravity_constant
    rounded_planetary_weight = round(planetary_weight, 2)

    print(f"The equivalent weight on {planet} is: {rounded_planetary_weight}")                           
           
main2()        
