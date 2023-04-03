n = int(input("Enter the number of elements to add: "))

# Create an empty set
my_set = set()

# Add n elements to the set
for i in range(n):
    element = input("Enter element {}: ".format(i+1))
    my_set.add(element)

# Display the set
print("The set is:", my_set)

# Display the last three elements of the set (based on insertion order)
if len(my_set) < 3:
    print("There are less than three elements in the set.")
else:
    last_three = list(my_set)[-3:]
    print("The last three elements of the set are:", last_three)