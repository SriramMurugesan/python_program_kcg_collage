# Search an element in an array (Linear Search)
arr = [10, 20, 30, 40, 50]
target = 30
found_index = -1

for i in range(len(arr)):
    if arr[i] == target:
        found_index = i
        break

print("Found at index:", found_index)
