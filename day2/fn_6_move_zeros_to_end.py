# Move all zeros to the end
arr = [0, 1, 0, 3, 12]

# Create a new array to hold the result
result = []

# First, add all non-zero elements
for i in range(len(arr)):
    if arr[i] != 0:
        result.append(arr[i])

# Then, add zeros for the remaining spaces
while len(result) < len(arr):
    result.append(0)

print("Array after moving zeros:", result)
