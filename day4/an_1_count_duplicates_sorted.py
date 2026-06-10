# Count duplicates in sorted array
arr = [1, 1, 2, 2, 2, 3, 4, 4]
target = 2

count = 0

for i in range(len(arr)):
    if arr[i] == target:
        count = count + 1

print("Count of duplicates:", count)
