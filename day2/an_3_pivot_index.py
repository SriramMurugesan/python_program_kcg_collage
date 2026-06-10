# Find the pivot index (where left sum equals right sum)
arr = [1, 7, 3, 6, 5, 6]
pivot_index = -1

for i in range(len(arr)):
    left_sum = 0
    right_sum = 0
    
    # Calculate sum to the left of i
    for j in range(0, i):
        left_sum = left_sum + arr[j]
        
    # Calculate sum to the right of i
    for k in range(i + 1, len(arr)):
        right_sum = right_sum + arr[k]
        
    # Check if they are equal
    if left_sum == right_sum:
        pivot_index = i
        break

print("Pivot index:", pivot_index)
