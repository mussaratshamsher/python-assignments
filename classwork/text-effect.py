import time

# Generator Function:
def chatbot_typing_simulator(text):
    """
    Simulates a typing effect for the given text.
    :param text: The text to be displayed with typing effect.
    """
    for char in text:
        yield char
for char in chatbot_typing_simulator("Hello Python....."):
    print(char, end='' , flush=True)
    time.sleep(.1)
                  
   
    
