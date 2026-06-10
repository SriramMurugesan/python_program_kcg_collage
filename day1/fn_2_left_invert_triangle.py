# Print a left aligned right angle triangle
n = 5
for i in range(1, n + 1):
    # Calculate spaces needed
    spaces = n - i
    print(" " * spaces + "*" * i)
