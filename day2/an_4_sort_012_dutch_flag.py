# Sort an array of 0s, 1s, and 2s
arr = [2, 0, 2, 1, 1, 0]

count_0 = 0
count_1 = 0
count_2 = 0

# Count the occurrences of each number
for i in range(len(arr)):
    if arr[i] == 0:
        count_0 = count_0 + 1
    elif arr[i] == 1:
        count_1 = count_1 + 1
    elif arr[i] == 2:
        count_2 = count_2 + 1

# Overwrite the original array
index = 0

# Add all 0s
for i in range(count_0):
    arr[index] = 0
    index = index + 1
    
# Add all 1s
for i in range(count_1):
    arr[index] = 1
    index = index + 1
    
# Add all 2s
for i in range(count_2):
    arr[index] = 2
    index = index + 1

print("Sorted array:", arr)
