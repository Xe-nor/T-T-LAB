my_list = [2, 5, 8, 3, 6, 4, 1, 3, 7, 3]

# element whose frequency is to be found
search_element = 3

count = 0
for element in my_list:
    if element == search_element:
        count += 1

print(f"The element {search_element} occurs {count} times in the list.")