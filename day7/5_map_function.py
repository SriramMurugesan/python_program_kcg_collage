"""
Map Function in Python
map(function, iterable) applies a given function to all items in an iterable (like a list) 
and returns a map object (which can be easily converted to a list or tuple).
"""

# Example 1: Basic mapping using a standard function
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
# Apply 'square' to every item in 'numbers'
squared_numbers = list(map(square, numbers))
print("1. Squared numbers:", squared_numbers)

print("-" * 30)

# Example 2: Using map with a lambda (anonymous) function (Very Common)
numbers2 = [10, 20, 30]
# lambda x: x / 2 is a quick way to write an inline function
halved = list(map(lambda x: x / 2, numbers2))
print("2. Halved numbers using lambda:", halved)

print("-" * 30)

# Example 3: Mapping over strings (Built-in string methods)
words = ["hello", "world", "python"]
uppercase_words = list(map(str.upper, words))
print("3. Uppercase words:", uppercase_words)

print("-" * 30)

# Example 4: Mapping multiple iterables simultaneously
# The function must take as many arguments as there are iterables
list1 = [1, 2, 3]
list2 = [10, 20, 30]
# Adds corresponding elements: 1+10, 2+20, 3+30
sums = list(map(lambda x, y: x + y, list1, list2))
print("4. Sum of multiple lists:", sums)

print("-" * 30)

# Example 5: Extracting specific data from a list of dictionaries
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 35}
]
# Extract just the names into a new list
names = list(map(lambda user: user["name"], users))
print("5. Extracted names:", names)
