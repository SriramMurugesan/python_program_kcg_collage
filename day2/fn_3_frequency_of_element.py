# Find the frequency of an element
arr = [1, 2, 2, 3, 2, 4]
target = 2
count = 0

for i in range(len(arr)):
    if arr[i] == target:
        count = count + 1

print("Frequency of", target, "is", count)
