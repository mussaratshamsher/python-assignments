
# Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price.
#  Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

# Solution:

class Product:
    def __init__(self, price):
        self._price = price 

        # Getter method
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self._price = new_price

    @price.deleter
    def price(self):
        print("Price deleted")
        del self._price

product = Product(100)
print(product.price)  

product.price = 200
print(product.price)

del product.price

# print(product.price) throws error as price has been deleted


