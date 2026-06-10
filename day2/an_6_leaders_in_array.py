# Find all leaders in an array
# An element is a leader if it is greater than all elements to its right
arr = [16, 17, 4, 3, 5, 2]
leaders = []

for i in range(len(arr)):
    is_leader = True
    # Check elements to the right
    for j in range(i + 1, len(arr)):
        if arr[i] <= arr[j]:
            is_leader = False
            break
            
    if is_leader == True:
        leaders.append(arr[i])

print("Leaders:", leaders)
