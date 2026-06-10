# Print an inverted pyramid
n = 5
for i in range(n, 0, -1):
    spaces = n - i
    print(" " * spaces + "* " * i)
