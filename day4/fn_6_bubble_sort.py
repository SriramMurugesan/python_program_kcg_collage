# Bubble Sort
arr = [64, 34, 25, 12, 22, 11, 90]

for i in range(len(arr)):
    for j in range(len(arr) - 1 - i):
        # Swap if current is greater than next
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print("Bubble Sort Result:", arr)
