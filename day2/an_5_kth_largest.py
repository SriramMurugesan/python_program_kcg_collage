# Kth largest number
arr = [3, 2, 1, 5, 6, 4]
k = 2

# Sort the array manually in descending order
for i in range(len(arr)):
    for j in range(len(arr) - 1 - i):
        if arr[j] < arr[j + 1]: # notice the < for descending
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

# Since it is sorted descending, the kth largest is at index k - 1
kth_largest = arr[k - 1]
print(k, "th largest number:", kth_largest)
