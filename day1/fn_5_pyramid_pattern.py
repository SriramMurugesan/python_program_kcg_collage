# Print a pyramid pattern
n = 5
for i in range(1, n + 1):
    spaces = n - i
    print(" " * spaces + "* " * i)
