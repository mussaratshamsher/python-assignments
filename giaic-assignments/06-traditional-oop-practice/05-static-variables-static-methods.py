
# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. 
# No class or instance variables should be used.

# Solution:

class MathUtils:
    @staticmethod
    def add(a, b):
        return a+b

print(MathUtils.add(5, 5)) 
print(MathUtils.add(10, 20))


