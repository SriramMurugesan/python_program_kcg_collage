# Sort Characters in String
text = "python"

# Convert to list
arr = list(text)

# Sort using bubble sort
for i in range(len(arr)):
    for j in range(len(arr) - 1 - i):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

# Combine back into a string
result = ""
for i in range(len(arr)):
    result = result + arr[i]

print("Sorted characters:", result)
