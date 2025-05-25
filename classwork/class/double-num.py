import time
#print list in a way that each number should become square of parent
# nums = [2, 4, 8, 16] result = [4, 16, 64, 256]
nums = [2, 4, 8, 16]
#method 1
result = []
for num in nums:
    result.append(num ** 2)
print(result)
#method 2
print([x ** 2 for x in nums])
print([a ** 3 for a in nums])

# find sum of same list
print("sum", [x + x for x in nums])

# Generator Functions:
def greet():
    yield "Hello World!"
    yield "Hello Python" 
    time.sleep(2)
    yield "Hello Generator"   
message = greet()
# print(next(message)) 
# print(next(message)) 
# print(next(message)) 

# def chatbot_simulator():
#     for char in text:
#         yield char
#         time.sleep(0.1)
# print("Chatbot Simulator:", next(chatbot_simulator()))   

def chatbot_typing_simulator(text):
    for char in chatbot_typing_simulator("Hello typescript"):
      print(char, end="", flush=True)
      time.sleep(0.1)


