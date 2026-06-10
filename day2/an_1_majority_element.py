# Find the majority element (appears more than n/2 times)
arr = [2, 2, 1, 1, 1, 2, 2]
n = len(arr)

majority_element = -1

for i in range(n):
    current_element = arr[i]
    count = 0
    
    # Count how many times current_element appears
    for j in range(n):
        if arr[j] == current_element:
            count = count + 1
            
    # Check if it is the majority
    if count > n // 2:
        majority_element = current_element
        break

print("Majority element:", majority_element)
