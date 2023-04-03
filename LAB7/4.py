my_tuple = (2, 5, 8, 3, 6, 4, 1)

# element to be searched
search_element = 6

if search_element in my_tuple:
    index = my_tuple.index(search_element)
    print(f"The element {search_element} is found at position {index}.")
else:
    print("The element is not found.")