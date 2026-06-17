"""
Decorators in Python
A decorator is a function that takes another function and extends its behavior 
without explicitly modifying it. It "decorates" the original function.
"""

# 1. Creating a simple decorator
def my_decorator(func):
    def wrapper():
        print("1. Something is happening BEFORE the function is called.")
        func() # Call the original function
        print("3. Something is happening AFTER the function is called.")
    return wrapper

# 2. Applying the decorator using the @ symbol
@my_decorator
def say_hello():
    print("2. Hello!")

say_hello()

print("-" * 30)

# 3. Decorator with arguments (using *args and **kwargs)
def timer_decorator(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        result = func(*args, **kwargs) # Execute actual function
        
        end_time = time.time()
        print(f"[{func.__name__}] took {end_time - start_time:.5f} seconds to run.")
        return result
    return wrapper

@timer_decorator
def calculate_sum(n):
    return sum(range(n))

# This will print the sum AND the time it took to calculate it
result = calculate_sum(1000000)
print(f"Result: {result}")
