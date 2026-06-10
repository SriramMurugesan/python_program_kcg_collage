# Find the second smallest element in an array
arr = [10, 20, 5, 8, 90, 3]

# We need to sort it manually first using a simple bubble sort
for i in range(len(arr)):
    for j in range(len(arr) - 1 - i):
        if arr[j] > arr[j + 1]:
            # Swap elements
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

# Now the array is sorted, the second smallest is at index 1
print("Second smallest element:", arr[1])
