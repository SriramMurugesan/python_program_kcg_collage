# Find the maximum and minimum element
arr = [10, 5, 20, 8, 90]

max_val = arr[0]
min_val = arr[0]

for i in range(len(arr)):
    if arr[i] > max_val:
        max_val = arr[i]
    if arr[i] < min_val:
        min_val = arr[i]

print("Maximum:", max_val)
print("Minimum:", min_val)
