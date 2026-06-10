# Find correct insertion position
arr = [1, 3, 5, 6]
target = 5

insertion_position = len(arr)

for i in range(len(arr)):
    if arr[i] >= target:
        insertion_position = i
        break

print("Correct insertion position:", insertion_position)
