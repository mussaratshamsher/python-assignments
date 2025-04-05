# Problem Statement
# Write a program to print terms in the Fibonacci sequence up to a maximum value.

# Solution

MAX_TERM_VALUE = 10000

def fibbonacci(max_value):
    a,b = 0 ,1
    while a<= max_value:
        print(a)
        a,b = b, a+b

fibbonacci(MAX_TERM_VALUE)       
