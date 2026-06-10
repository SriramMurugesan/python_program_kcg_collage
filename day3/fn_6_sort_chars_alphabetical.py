# Sort characters in alphabetical order
arr = ['d', 'a', 'c', 'b']

for i in range(len(arr)):
    for j in range(len(arr) - 1 - i):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print("Sorted characters:", arr)
