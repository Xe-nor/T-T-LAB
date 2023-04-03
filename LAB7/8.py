# Function to check whether two strings are equal
def check_strings_equal(str1, str2):
    if str1 == str2:
        print("Both strings are equal")
    else:
        print("Both strings are not equal")

# Function to find a substring from a string using negative indexing
def find_substring(str1, index):
    substr = str1[index:]
    print("Substring:", substr)

# Testing the functions
str1 = "Hello World"
str2 = "Hello World"
check_strings_equal(str1, str2)

str3 = "Hello"
str4 = "World"
check_strings_equal(str3, str4)

str5 = "Hello World"
find_substring(str5, -5)