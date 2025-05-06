# print(chr(‘97’))
# print(chr(97))
# print(complex())
# print(list(enumerate([2, 3, 4])))
# x= 3
# print(eval('x^2'))
# l=[2,3,4]
# print(list(reversed(l)))
# print(float('   -12345\n'))
# print(float('-infinity'))
# print(float('infinity'))
# print(hex(15))
# print(oct(7))
# print(oct('7'))
# x = 50
# def func(x):
#     print('x is', x)
#     x = 2
#     print('Changed local x to', x)
# func(x)
# print('x is now', x)
# def say(message, times = 1):
#     print(message * times)
# say('Hello')
# say('World', 5)
# def power(x, y=2):
#     r = 1
#     for i in range(y):
#        r = r * x
#     return r
# print(power(3))
# print( power(3, 3))
# def sum(*args):
#    '''Function returns the sum of all values'''
#    r = 0
#    for i in args:
#       r += i
#    return r
# print(sum.__doc__)
# print(sum(1, 2, 3))
# print(sum(1, 2, 3, 4, 5))
# i=0
# def change(i):
#    i=i+1
#    return i
# change(1)
# print(i)
# def a(b):
#     b = b + [5]
# c = [1, 2, 3, 4]
# a(c)
# print(len(c))
# a=10
# b=20
# def change():
#     global b
#     a=45
#     b=56
# change()
# print(a)
# print(b)
# def change(i = 1, j = 2):
#     i = i + j
#     j = j + 1
#     print(i, j)
# change(j = 1, i = 2)
# def change(one, *two):
#    print(type(two))
# change(1,2,3,4)
# def display(b, n):
#     while n > 0:
#         print(b,end="")
#         n=n-1
#display('z',3)
# def find(a, **b):
#    print(type(b))
# find('letters',A='1',B='2')
# def foo(k):
#     k[0] = 1
# q = [0]
# foo(q)
# print(q)
# def foo(fname, val):
#     print(fname(val))
# foo(max, [1, 2, 3])
# foo(min, [1, 2, 3])
# def foo():
#     return total + 1
# total = 0
# print(foo())
# def foo():
#     total += 1
#     return total
# total = 0
# print(foo())
# def foo(x):
#     x = ['def', 'abc']
#     return id(x)
# q = ['abc', 'def']
# print(id(q) == foo(q))
# def foo(i, x=[]):
#     x.append(i)
#     return x
# for i in range(3):
#     print(foo(i))
# def f1(x):
#     global x
#     x+=1
#     print(x)
# f1(15)
# print("hello")

# def f():
#     global a
#     print(a)
#     a = "hello"
#     print(a) 
# a = "world" 
# f()
# print(a)
# def f(x):
#     print("outer")
#     def f1(a):
#         print("inner")
#         print(a,x)
# f(3)
# x = 5 
# def f1():
#     global x
#     x = 4
# def f2(a,b):
#     global x
#     return a+b+x
# f1()
# total = f2(1,2)
# print(total)
# y, z = 1, 2
# def f():
#     global x
#     x = y+z
# print(globals())
# print(locals())
# e="butter"
# def f(a): 
#     print(a)+e
# a=10
# globals()['a']=25
# print(a)
# def f(): x=4
# x=1
# f()
# x
# l=[2, 3, [4, 5]]
# l2=l.copy()
# l2[0]=88
# print(l)
# print(l2)
# l1=[[10, 20], [30, 40], [50, 60]]
# l2=list(l1)
# print(l1)
# print(l2)
# l2[1] = [100, 200]
# print(l2)
# print(l1)
# l1[0][0] = 1000
# print(l1)
# print(l2)
# l1=[2, 4, 6, (8)]
# l2=[1,( 2), 3]
# l1=l2
# print(l1)
# print(l2)
# def check(n):
#     if n < 2:
#         return n % 2 == 0
#     return check(n - 2)
# print(check(11))
# a = [1, 2, 3, 4, 5]
# b = lambda x: (b (x[1:]) + x[:1] if x else []) 
# print(b (a))
# l=[n for n in range(5)]
# f=lambda x:bool(x%2)
# print(f(3), f(1))
# for i in range(len(l)):
#     if f(l[i]):
#         del l[i]
#         print(i)
# l=[1, 2, 3, 4, 5]
# def f1(x):
#     return x<0
# m1=filter(f1, l)
# print(list(m1))
import math
# for i in range(3):
#     print(i)
print(math.floor(6.7)) 
#it shows that math.floor() is used to round down the number to the nearest integer.






