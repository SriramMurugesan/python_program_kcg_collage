"""
Global and Local Scope in Python
- Local Scope: Variables defined inside a function. They can only be used inside that function.
- Global Scope: Variables defined outside any function. They can be accessed anywhere in the file.
"""

# 1. Global Variable
message = "I am global"

def show_scopes():
    # 2. Local Variable
    local_message = "I am local"
    print("Inside function:")
    print("- Accessing local:", local_message)
    print("- Accessing global:", message)

show_scopes()
print("\nOutside function:")
print("- Accessing global:", message)
# print(local_message)  # This would cause an Error because local_message is not available globally

print("-" * 30)

# 3. Modifying a Global Variable from inside a function
counter = 0

def increment():
    global counter  # Must use 'global' keyword to modify a global variable inside a function
    counter += 1
    print("Counter is now:", counter)

increment()
increment()
