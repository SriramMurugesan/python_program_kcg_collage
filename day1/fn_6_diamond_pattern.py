# Print a diamond pattern
n = 5
# Upper part
for i in range(1, n + 1):
    spaces = n - i
    print(" " * spaces + "* " * i)
# Lower part
for i in range(n - 1, 0, -1):
    spaces = n - i
    print(" " * spaces + "* " * i)
