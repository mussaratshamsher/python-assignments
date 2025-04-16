
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
fruits = [“mango”, “banana”, “orange”]
    
    for fruit in fruits:
     print(fruit, end=” ”)
                    