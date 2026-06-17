"""
Default Arguments and 'self' in Python Classes
- Default Arguments: Provide a default value for a parameter if none is given.
- 'self': Refers to the specific instance of the class being created.
"""

# 1. Simple Default Arguments
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()          # Uses default: "Guest"
greet("Sriram")  # Uses provided: "Sriram"

print("-" * 30)

# 2. 'self' and Default Arguments in Classes
class Student:
    # 'self' must always be the first parameter in instance methods.
    # We can also have default arguments.
    def __init__(self, name, course="Python Basics"):
        self.name = name          # Instance variable
        self.course = course      # Instance variable (might use default)
        
    def display_info(self):
        print(f"Student: {self.name}, Course: {self.course}")

# Creating objects
student1 = Student("Alice")               # Uses default course
student2 = Student("Bob", "Data Science") # Overrides default course

student1.display_info()
student2.display_info()

print("-" * 30)

# 3. Pitfall: Mutable Default Arguments (Lists, Dictionaries)
# NEVER use an empty list or dictionary as a default argument directly like: def func(item_list=[])
def add_item(item, item_list=None): # Use None instead, then create a new list inside
    if item_list is None:
        item_list = []
    item_list.append(item)
    return item_list

print("List 1:", add_item("Apple"))
print("List 2:", add_item("Banana")) # Notice it creates a fresh list, avoiding bugs!
