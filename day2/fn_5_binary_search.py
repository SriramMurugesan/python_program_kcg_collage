# Binary Search (Array must be sorted)
arr = [10, 20, 30, 40, 50]
target = 40

left = 0
right = len(arr) - 1
found_index = -1

while left <= right:
    mid = (left + right) // 2
    
    if arr[mid] == target:
        found_index = mid
        break
    elif arr[mid] < target:
        # Target is in the right half
        left = mid + 1
    else:
        # Target is in the left half
        right = mid - 1

print("Found at index:", found_index)
