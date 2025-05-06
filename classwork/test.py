# print('b' in 'alphabet')
# a = [1,2]
# b = [1,2]
# # print(a == b, a is b)
# print('b'.isidentifier())
# print('a@ 1,'.islower())
# print('11'.isnumeric())
# print('1.1'.isnumeric())
# print(' \n  '.isspace())
# print('''\tfoo'''.lstrip())
# print('xyzxxyyxyy'.lstrip('xyy'))
# print('xyxxyyzxxy'.lstrip('xyy'))
# print('abcdefcdgh'.partition('cd'))
# print('abcd'.partition('cd'))
# print('abcdefcdghcd'.split('cd', 2))
# print('ab\ncd\nef'.splitlines())
# print('Ab!2'.swapcase())
# print('ab cd-ef'.title())
# print('abcd'.translate('a'.maketrans('abc', 'bcd')))
# print('abcd'.translate({97: 98, 98: 99, 99: 100}))
# import random
# print('ab'.zfill(5))
# print('+99'.zfill(5))
# # list1 = list()
# list1 = ['h','e','l','l','o']
# print(len(list1))
# print(list1[0])
# list2 = [2445,133,12454,123]
# print(max(list2))
# print(min(list2))
# print(sum(list2))
# print(random.shuffle(list2))
# list3 = [4, 2, 2, 4, 5, 2, 1, 0]
# print(list3[:1])
# names = ['Amir', 'Bear', 'Charlton', 'Daman']
# print(names[-1][-1])
#list3 = [4, 2, 2, 4, 5, 2, 1, 0]
#print(list3.reverse())
# print(list3.pop(1))
# print(list3)
#print("Welcome".split())
#print(list("a#,-b-c#d".split('#')))
# myList = [1, 2, 3, 4, 5, 6]
# for i in range(1, 6):
#     myList[i - 1] = myList[i]    
# for i in range(0, 6): 
#     print(myList[i], end = " ")
# list1 = [1, 3]
# list2 = list1
# list1[0] = 4
# print(list2)
# def f(values):
#     values[1] = 44 
# v = [1, 2, 3]
# f(v)
# print(v)
# def f(i, values = []):
#     values.append(i)
#     return values 
# f(1)
# f(2)
# v = f(3)
# print(v)
# names1 = ['Amir', 'Bala', 'Chales'] 
# if 'amir' in names1:
#     print(1)
# else:
#     print(2)
# names1 = ['Amir', 'Bala', 'Charlie']
# names2 = [name.lower() for name in names1] 
# print(names2[2][0])
# numbers = [1, 2, 3, 4]
# numbers.append([5,6,7,8]) 
# print(len(numbers))
# print(numbers)
# def addItem(listParam):
#     listParam += [1] 
# mylist = [1, 2, 3, 4]
# addItem(mylist)
# print(len(mylist))
# print(mylist)
# def increment_items(L, increment):
#     i = 0
#     while i < len(L):
#         L[i] = L[i] + increment
#         i = i + 1 
# values = [1, 2, 3]
# print(increment_items(values, 2))
# print(values)
# def example(L):
#     i = 0
#     result = []
#     while i < len(L):
#         result.append(L[i])
#         i = i + 3
#     return result
# veggies = ['carrot', 'broccoli', 'potato', 'asparagus']
# veggies.insert(veggies.index('broccoli'), 'celery')
# print(veggies)
# m = [[x, x + 1, x + 2] 
# for x in range(0, 3)]
# m = [[x, y] 
#      for x in range(0, 3) 
#      for y in range(0, 3)]
# print(m)
# values = [[3, 4, 5, 1], [33, 6, 1, 2]] 
# v = values[0][0]
# for row in range(0, len(values)):
#     for column in range(0, len(values[row])):
#         if v < values[row][column]:
#            v = values[row][column] 
# print(v)
# values = [[3, 4, 5, 1 ], [33, 6, 1, 2]]
# for row in values:
#     row.sort()
#     for element in row:
#         print(element, end = " ")
#     print()
# data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
# print(data[1][0][0])
# a=[14,52,7]
# b=a.copy()
# print(b is a)
# a=[13,56,17]
# a.append([87])
# a.extend([45,67])
# print(a)
# a=list((45,)*4)
# print((45)*4)
# print(a)
# lst=[[1,2],[3,4]]
# print(sum(lst,[]))
# word1="Apple"
# word2="Apple"
# list1=[1,2,3]
# list2=[1,2,3]
# print(word1 is word2)
# print(list1 is list2)
# def unpack(a,b,c,d):
#     print(a+d)
# x = [1,2,3,4]
# unpack(*x)
# x=[[1],[2]]
# print(" ".join(list(map(str,x))))
# a= [1, 2, 3, 4, 5]
# for i in range(1, 5):
#     a[i-1] = a[i]
# for i in range(0, 5): 
#     print(a[i],end = " ")
# def change(var, lst):
#     var = 1
#     lst[0] = 44
# k = 3
# a = [1, 2, 3]
# change(k, a)
# print(k)
# print(a)
# a=["Apple","Ball","Cobra"]
# a.sort(key=len)
# print(a)
# num = ['One', 'Two', 'Three']
# for i, x in enumerate(num):
#     print('{}: {}'.format(i, x),end=" ")
# k = [print(i) for i in my_string if i not in "aeiou"]    
# my_string = "hello world"
# k = [(i.upper(), len(i)) for i in my_string]
# print(k)
# x = [i**+1 for i in range(3)]; 
# print(x);
# print([i.lower() for i in "HELLO"])
# print([[i+j for i in "abc"] for j in "def"])
# print(list(map(lambda x: x**-1, [1, 2, 3])))
# l=[1,2,3,4,5]
# [x&1 for x in l]
# print([ord(ch) for ch in 'abc'])
# t=32.00
# print([round((x-32)*5/9) for x in t])
# l=["good", "oh!", "excellent!", "#450"]
# print([n for n in l if n.isalpha() or n.isdigit()])
# t = (1, 2, 4, 3, 8, 9)
# print([t[i] for i in range(0, len(t), 2)])
# t = (1, 2)
# print(3 * t)
# t1 = (1, 2, 4, 3)
# t2 = (1, 2, 3, 4)
# print(t1 > t2)
# my_tuple = (1, 2, 3, 4)
# my_tuple.append( (5, 6, 7) )
# print(len(my_tuple))
# numberGames = {}
# numberGames[(1,2,4)] = 8
# numberGames[(4,2,1)] = 10
# numberGames[(1,2)] = 12
# sum = 0
# for k in numberGames:
#     sum += numberGames[k]
# print(len(numberGames) + sum)
# a=(1,2,(4,5))
# b=(1,2,(3,4))
# print(a<b)
# print(("Check")*3)
# a=(2,3,4)
# print(sum(a))
# a=(1,2,3,4)
# del a[0]
# print(a)
a=(0,1,2,3,4)
b=slice(0,2)
print(a[b])
a=(1,2,3)
b=('A','B','C')
c=tuple(zip(a,b)) #Explanation: Zip function combines individual elements of two iterables into tuples.
print(c)
