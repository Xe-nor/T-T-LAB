def sort_dict_by_key(d):

    # Create a list of tuples from the dictionary items
    items = d.items()
    
    # Sort the list of tuples based on the first element of each tuple (i.e., the key)
    sorted_items = sorted(items)
    
    # Create a new dictionary from the sorted list of tuples
    sorted_dict = dict(sorted_items)
    
    return sorted_dict

# Testing the function
d1 = {'c': 1, 'b': 2, 'a': 3}
sorted_dict = sort_dict_by_key(d1)
print(sorted_dict)  # Output: {'a': 3, 'b': 2, 'c': 1}