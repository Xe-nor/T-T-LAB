

# Create a frozenset with some elements
my_fset = frozenset([1, 2, 3, 4])

# Try to add a new element to the frozenset
try:
    my_fset.add(5)
except AttributeError:
    print("Error: 'frozenset' object has no attribute 'add'")

# Display the frozenset
print("The frozenset is:", my_fset)