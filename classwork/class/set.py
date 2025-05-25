

a = {1 , 2 , 3}
b = {3 , 4 , 5}
print(a & b) #intersection
#print(a.clear())
a.add(4) #takes only one argument
print(a)
s = {10 , 20 , 30}
s.remove(20) 
print(s)
{1, 2, 3} # valid
{1,2, 'three'} # valid
#{ 1, [ 2, 3] } # TypeError: unhashable type: 'list'
# set{ [1, 2, 3] } # TypeError: unhashable type: 'list'
# set{ (1, 2, 3) } # valid
# set{ {1, 2, 3} } # TypeError: unhashable type: 'set'
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.symmetric_difference(s2))
a = {1 , 2 , 3}
b ={3 , 4 , 5}
#print(a | b)
a.discard(9)
print(a) # discard does not raise an error if the element is not found
s = {1, 2, 3, 3, 2} 
print(len(s)) # Output: 3 (duplicates are removed)

inter = {1, 2} - {2, 3} 
print(inter) # Output: {1}(
#fs = frozenset( [1, [2, 3] ] )
#print(fs) # TypeError: unhashable type: 'list
  
a = { frozenset( {1} ) : "value" }
print(a) #same output as above
print(bool("") ) #false
print(isinstance(3.14, int)) # false
print(2 + 3 * 4) # 2+12 = 14
x = "Hello"
print(x[::-1]) #:: shows the reverse of the string, -1 means reverse the string
for i in range(3):
    print(i)
s = {1, 2, 3, 3, 2} 
print(len(s))
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1.symmetric_difference(s2))
a = {1 , 2 , 3}
b = {3 , 4 , 5}
print(a & b)

def func() :
    print("Module 1 function")
   
if __name__ == "__main__" :
    print("Module 1 executed directly")
import math
print(math.__name__)   
import random 
import random as rnd 
rnd.choice = lambda lst: lst[0] 
print(random.choice([1, 2, 3]) , end=" ") 
print(rnd.choice([1, 2, 3]), end=" ")
try:
    square = math.sqrt(-1)
except ValueError as e:
    print(f" \nAn error occured! ({e})")
try:
    numbers = [1, 2, 3]
    result = numbers[1]  
except IndexError:
    print("Index out of range!")
else:
    print(f"Access successful! Value: {result}")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Finally done!") 
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older!")
    return "Age is valid"
try:
    result = check_age(15)
except ValueError as e:
    print(f"Error: {e}") 

from typing import NoReturn

def error_function() -> NoReturn:
    return 1 / 0
try:
    error_function()
except Exception as e:
    print("Error:", e) 
import sys
def terminate_program() -> None:
    sys.exit("Program terminated")
try:
    terminate_program()
except SystemExit as e:
    print("Error:", e) 
def divide_numbers(a, b):
    try:
        result = a / b  
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Invalid input type. Numbers required.")
    else:
        print(f"Division successful. Result: {result}")
    finally:
        print("Operation complete.")

divide_numbers(10, "2") 
print(2 ** 3 ** 2) # 2**9 = 512 
a = int(5.8) + float(3) # 5 + 3.0 = 8.0
print(a)
print( True and False or True)
print(True and not False)
print(not (False or False))
print(1 and 0 or 1)
print(bool(0) and bool(1))
print(5 == 5.0)
print(5 != 5)
#print("5" > 2) # TypeError: '>' not supported between instances of 'str' and 'int'
print( 5 is 5)
print([] == [] )
print("Python" < "Java") # False
print("script: ", "Typescript" > "Javascript")
#f = x =// 3 print(f)
#What does x &= y do? = x = y = 3 it tells the interpreter to take the value of x and assign it to y, then assign the value of y to x.
print(-3 ** 2)
print(True or False and False)
print("Python"[2:5] )
print("hello world".find("world"))
print(int(10.99))
print( bool(-5))
print(float(5))
print(bool([]))
print(int('10') + float('5.5'))
print(bool(0.0))
print(isinstance(10.5, float))
print('result: ',int(True) + int(False))
print(bool('False'))
print(int('10'))
print(type(10/5))
print(int(3.9) + float(2))
#print( int('3.5')) #value error
for i in range(1, 6, 3): 
    print("i: ", i)
for i in range(5, 1, -1):
    print("i", i)
def foo(x=[]): 
    x.append(1) 
    return x 
print(foo(), foo())  
@staticmethod 
def greet():
  print("Hello")
def fact(n): 
    if n == 0: return 1 
    else: return n * fact(n-1)
print(fact(3))
def test(a, b, c=3): 
    return a + b + c 
print("params: ", test( 1, 2))
def a(): 
    pass 
print(a())
print(sum(map(lambda x: x * 2, [1, 2, 3])) )
 # Output: 12 = 1*2 + 2*2 + 3*2
print((lambda x: x ** 2)(3))
def f(x, y): 
    return x + y 
print(f("2", "3")) #concatenation
print(f(2, 3)) #addition

