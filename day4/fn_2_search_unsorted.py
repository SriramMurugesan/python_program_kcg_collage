# Search an element in an unsorted array
arr = [15, 2, 4, 8, 9, 5, 10, 23]
target = 8

found_index = -1

for i in range(len(arr)):
    if arr[i] == target:
        found_index = i
        break

print("Found at index:", found_index)
