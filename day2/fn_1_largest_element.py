# Find the largest element in an array
arr = [10, 20, 5, 8, 90, 3]

# Start by assuming the first element is the largest
largest = arr[0]

for i in range(len(arr)):
    current_element = arr[i]
    if current_element > largest:
        largest = current_element

print("Largest element:", largest)
