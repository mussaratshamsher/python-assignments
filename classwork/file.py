
# None = "a"
# print(None)

# x = 1
# del x
# print(x)

#is operator in python: 
# reutrns True if both variables have same values.
# is operator is used to compare the memory location of two objects.
# It returns True if both variables point to the same object, otherwise it returns False.
 
a = "a"
b = "u"

print(a is b)
print(not True)
print(not False)

#in operator in python:
# The in operator is used to check if a value exists in a sequence (string, list, tuple, set, dictionary).
# It returns True if the value is found in the sequence, otherwise it returns False.
 
# print(a)
# a = -b
print("5", 5 is 5.0)
print(5 == 5.0)
x = 10
y= 10
print("x=y", x is y)

text = "Python"
encoded_text = text.encode('utf-8')
print(type(encoded_text))
s = "Café"
encoded_s = s.encode('utf-8')
decoded_s = encoded_s.decode('utf-8')
print(decoded_s)
print("code", '\u03B1')

s = "Python Programming"
print(s.count('p'))

s = "apple,banana,orange"
print(s.split(',' , 1))
s = "Python Programming"
print(s[ 7: 18 : 2])
s = "Data Analysis"
print("-".join(s.split()))

s = "Computer Vision"
print(s.startswith("Comp"))
print('Python'.upper())
list= ['a ',  'b' ,  'c']
print('-'.join(['a', 'b', 'c']))

name = "Alice"
print("Hello, %s!" % name)
print("{1} {0}".format("World", "Hello"))
number = 255
print("Hex: {:x}".format(number))

a = 4
b= 6
print(a is b)
# == compares 
result = not False or False and True
print("result", result)
#print(“” and “hello world”) errror

# def hello():
#      for num in range(10, 0):
#         print(f"you are in range {num}")
# hello() 
# fruits = ["mango"," banana", "orange"]
# for fruit in fruits:
#         print(fruit, end="")     
# conditional = not [] and not ""
# while conditional:
#          print("inside the loop")  
# for i in range(1, 7):
#     if i % 2 == 0:
#         continue
#     if i > 4:
#         break
#     print(i, end="")   
for num in range(3):
         print(num, end="")
else:
     print("\n continue")            
word = "Quiz"
for letter in word:
      print(letter) 
for i in range(2, 11, 2):
         print(i)  
# x = 10
# while x == 10:
#        print("wait a second")      
# age = 17
# is_fasting = False
# if age >= 18 or (age >= 16 and is_ fasting):
#     print("Eligible, you can EAT 😁")
# else:
#     print("Not Eligible, Fast today")  
# 
# numbers = [2, 4, 6, 8]
# for n in numbers:
#     if n % 5 == 0:
#         print("Divisible by 5")
#         break
#     else:
#       print("No multiples of 5 found")
x = ""
if x or 0 or []:
    print("Truthy")
else:
    print("Falsy")
def f():
    print("f() executed")
    return True
if False and f():
    print("Inside if")
else:
    print("Inside else")   
x = 10
y = 20
result = (x < y and x != 0) or (y < x and y != 0)
print(result)
i = 1
while i < 10:
    if i % 7 == 0:
        break
    i += 1
else:
    print("Loop finished")
print("" and "hello world")   
                         