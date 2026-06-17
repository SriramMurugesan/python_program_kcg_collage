"""
Closures in Python
A closure is a nested function that remembers the values from its enclosing (outer) function, 
even after the outer function has finished executing.
"""

def outer_function(message):
    # This is the enclosing function's variable
    
    def inner_function():
        # The inner function has access to the outer function's 'message' variable
        print(f"The hidden message is: {message}")
        
    # We return the inner function itself, not its result (no parenthesis)
    return inner_function

# Create a closure
my_closure = outer_function("Secret Code 123!")

# Even though outer_function has finished executing, 
# my_closure still remembers the 'message' variable.
my_closure()

print("-" * 30)

# Another example: A multiplier factory
def multiplier_of(n):
    def multiplier(number):
        return number * n
    return multiplier

# Create specific multiplier functions
multiply_by_5 = multiplier_of(5)
multiply_by_10 = multiplier_of(10)

print("5 * 10 =", multiply_by_5(10))
print("5 * 6 =", multiply_by_5(6))
print("10 * 6 =", multiply_by_10(6))
