# Find the largest and second largest number
arr = [10, 20, 4, 45, 99, 99, 3]

largest = arr[0]
second_largest = arr[0]

# First find the largest
for i in range(len(arr)):
    if arr[i] > largest:
        largest = arr[i]

# Now find the second largest (must be less than largest)
# Let's initialize second_largest to a very small number or the first valid element
found_second = False
for i in range(len(arr)):
    if arr[i] < largest:
        if found_second == False:
            second_largest = arr[i]
            found_second = True
        elif arr[i] > second_largest:
            second_largest = arr[i]

print("Largest number:", largest)
print("Second largest number:", second_largest)
