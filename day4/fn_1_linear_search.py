# Linear Search
arr = [10, 50, 30, 70, 80, 20, 90, 40]
target = 20

found_index = -1

for i in range(len(arr)):
    if arr[i] == target:
        found_index = i
        break

print("Found at index:", found_index)
