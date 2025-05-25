
# An expanded Magic Toy Catalog implementation demonstrating key special methods in action:

class MagicToyCatalog:
    def __init__(self):
       self.toys = {}
       self._secret_offer = "Free gift bag with every purchase!"

    def __setitem__(self, name, details):
        """Set the details of a toy in the catalog."""
        self.toys[name] = details   
    
    def __getitem__(self, name):
        """Get the details of a toy from the catalog."""
        return self.toys.get(name, "Toy not found.")
    
    def __delitem__(self, name):
        """Delete a toy from the catalog."""
        if name in self.toys:
            del self.toys[name]
            print(f"{name} has been removed from the catalog.") 
        else:
            print("Toy not found.")

    def __contains__(self, name):
        """Check existence in the catalog."""
        return name in self.toys 

    def __len__(self):
        """Get the number of toys in the catalog."""
        return len(self.toys)

    def __iter__(self):
        """Iterate over the toys in the catalog."""
        return iter(self.toys.items()) 

    def __add__(self, other):
        """Combine two catalogs."""
        combined = MagicToyCatalog()
        combined.toys = {**self.toys, **other.toys} 
        return combined

    def __str__(self):
        """User fruendly display of the catalog."""
        header = "Magic Toy Catalog:\n"
        items = "\n".join([f"{name}: ${price} ({desc})"
                           for name, (price, desc) in self.toys.items()])
        return header + (items if items else "Not available.") 

    def __repr__(self):
        """Developer representation of the catalog."""
        return f""

    def __call__(self, discount=0):
        """Activate a special offer."""
        return "\n".join([f"{name}: ${price * (1 - discount/100):.2f}"
                          for name, (price, desc) in self.toys.items()]) 

class MagicToyError(Exception):
    """Custom exception for the Magic Toy Catalog."""
    pass

# Example Usage:
# Catalog
catalog = MagicToyCatalog()
collector_edition = MagicToyCatalog()

# Adding toys to the catalog
catalog["RoboDog"] = (29.99, "A robotic dog that barks and wags its tail.")
catalog["MagicCar"] = (49.99, "A car that can be controlled with a magic wand.")
collector_edition["MagicKit"] = (99.99, "A kit that includes a magic wand and a spell book.")

#Combine catalogs using __add__
combined_catalog = catalog + collector_edition

#Access items with _getitem__
print(combined_catalog["RoboDog"]) # (29.99, "A robotic dog that barks and wags its tail.")

#Check existence with __contains__
print("MagicCar" in combined_catalog) # True

# Get count with __len__
print(f"Total toys:{len(combined_catalog)}") # 3

# Iterate over items with __iter__
for name, details in combined_catalog:
    print(f"{name}: {details[1]}") # prints each toy's name & details

# String representation with __str__ 
print(combined_catalog) # prints the catalog in a user-friendly format

# Callable discount with __call__
print("\n 🔥 FLASH SALE 🔥")
print(combined_catalog(20)) # prints the catalog with a 20% discount

# Remove item with __delitem__
del combined_catalog["RoboDog"]


