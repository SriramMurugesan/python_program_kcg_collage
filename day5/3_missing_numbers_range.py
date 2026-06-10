# Find missing numbers from a range 1 to 10
arr = [1, 2, 4, 6, 7, 9, 10]

print("Missing numbers:")

for i in range(1, 11):
    found = False
    # Check if 'i' is inside the array
    for j in range(len(arr)):
        if arr[j] == i:
            found = True
            break
            
    # If 'i' was not found in the array, it is missing
    if found == False:
        print(i)
