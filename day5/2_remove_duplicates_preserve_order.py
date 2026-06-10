# Remove duplicates while preserving order
arr = [1, 2, 2, 3, 4, 4, 5, 1]

result = []

for i in range(len(arr)):
    current_element = arr[i]
    
    # Check if we already have it in the result
    is_duplicate = False
    for j in range(len(result)):
        if result[j] == current_element:
            is_duplicate = True
            break
            
    # If not a duplicate, add it to result
    if is_duplicate == False:
        result.append(current_element)

print("Original list:", arr)
print("List after removing duplicates:", result)
