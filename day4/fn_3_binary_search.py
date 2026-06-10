# Binary Search
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

left = 0
right = len(arr) - 1
found_index = -1

while left <= right:
    mid = (left + right) // 2
    
    if arr[mid] == target:
        found_index = mid
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

print("Found at index:", found_index)
