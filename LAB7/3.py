n = int(input("Enter the number of elements: "))
my_list = []

# Dynamically populate the list
for i in range(n):
    my_list.append(int(input(f"Enter element {i+1}: ")))

# Sort the first 5 elements in descending order
my_list[:5] = sorted(my_list[:5], reverse=True)

# Display the updated list
print("Updated list:")
print(my_list)