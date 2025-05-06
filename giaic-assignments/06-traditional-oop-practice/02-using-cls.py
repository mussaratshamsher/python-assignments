
# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created.
# Use a class variable and a class method with cls to manage and display the count.

# Solution:
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return Counter.count

# Example usage:
counter1 = Counter()
counter2 = Counter()
counter3 = Counter()
counter4 = Counter()
counter5 = Counter()

print(Counter.get_count())  # Output: 3
