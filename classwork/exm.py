try: 
    x = [1, 2, 3] 
    print(x[5]) 
except IndexError: 
    print("Index out of range")
#int("3.5") #value error
#print("a" + 5) type error
# len(5) type error
# x = unknown_var  name error
try:
    raise ValueError("Invalid value!") 
except ValueError as err: 
    print(err)
# print( "hello" + 5)    
# try: x = 10 / 0 
# except: print("Exception occurred") 
# else: print("No exception") 
# finally: print("Cleanup")
# try: raise Exception("Test") 
# except Exception as e: 
#        print(type(e).__name__)
# try: 1/0 
# except ZeroDivisionError: 
#      raise ValueError("Custom error") from None
try: 
    a = [1, 2, 3] 
    print(a[5]) 
except LookupError: 
    print("Caught LookupError")
try: 
    raise Exception("Outer") 
except Exception as e: 
    try: raise Exception("Inner") 
    except: print(e)    
try: open("nonexistent.txt") 
except OSError as err: 
    print(err.errno)
try: int("xyz") 
except ValueError as e: 
    print(str(e).upper())
# def func(): 
#     try: return 1 
#     finally: return 2 
# print(func())    
try: 
    print("A") 
    raise Exception("Oops")
    print("B")
except: 
    print("C") 
finally: 
    print("D")
try: x = "2" + 3 
except TypeError as e: 
    print("Error:", e.args[0])    
# def nested(): 
#     try: 
#         try: 
#             raise ValueError("Inner") 
#         finally: 
#             print("Inner finally") 
#     except ValueError: print("Caught") 
# nested()    
# try: raise KeyError("Oops") 
# except KeyError as e: 
#     raise ValueError("Another") from e
# try: 
#     raise KeyboardInterrupt 
# except Exception: print("Handled")
# def nested(): 
#     try: 
#         try: raise ValueError("Inner") 
#         finally: 
#             print("Inner finally") 
#     except ValueError: 
#      print("Caught") 
# nested()
# try: raise KeyError("Oops") 
# except KeyError as e: 
#     raise ValueError("Another") from e
try: 
    raise ValueError("Invalid") 
except ValueError: 
    print("Caught") 
else: 
    print("No error") 
finally: 
    print("Always")
def example(): 
    try: 
        return "Try" 
    finally: 
        return "Finally" 
print(example())    
try: 
    a = [1, 2, 3] 
    print(a[5]) 
except IndexError: 
    print("Index Error") 
except: 
    print("Some other error")
str="hello"
print(str[:2])
help(id) 
print(0.1+0.2)
print(0.1+0.2==0.3)
print(3 ^ 4)
a= not(10<20) and not(10>30)
print(a)
# x=56.236
# print("%.2f"%x)
# x=22.19
# print("%5.2f"%x)
# print("-%5d0",989)
X="san-foundry"
print("%56s",X)
x=456
print("%-06d"%x)
# x = ['ab', 'cd']
# for i in x:
#     i.upper()
# print(x)      
i = 1
while True:
    if i%0O7 == 0:
        break
    print(i)
    i += 1
i = 5
# while True:
#     if i%0O11 == 0:
#         break
#     print(i)
#     i += 1
x = "abcdef"
i = "i"
while i in x:
    print(i, end=" ")