#Resursive function examples

# a.Factorial Function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)    
print("Factorial: ",factorial(4))  # Output: 24
# F(n) == n * F(n-1)
# F(0) = 1
# F(1) = 1
# F(2) = 2 *F(1) = 2
# F(3) = 3 * F(2) = 3 * 2 = 6
# F(4) = 4 * F(3) = 4 * 6 = 24 

# b.Fibonacci Sequence
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print("Fibonacci: ",fibonacci(4)) #Output = 3
# F(n) = F(n-1) + F(n-2)
# F(0) = 0
# F(1) = 1
# F(2) = F(1) + F(0) = 1 + 0 = 1
# F(3) = F(2) + F(1) = 1+ 1 = 2
# F(4) = F(3) + F(2) = 2 +1 = 3 

# c.Sum of Digits: if numbers are not known
def sum_of_objects(*n):
   
   total = 0
   for num in n:
        total += num
   return total
print("sum_of_objects",sum_of_objects(1,2,3)) #Output: 6
print("sum_of_objects", sum_of_objects(1,2,3,4,5))  #Output: 15




