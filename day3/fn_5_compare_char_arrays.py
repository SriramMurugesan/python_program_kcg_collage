# Compare two character arrays without using inbuilt functions
arr1 = ['h', 'e', 'l', 'l', 'o']
arr2 = ['h', 'e', 'l', 'l', 'o']

are_equal = True

# First check if lengths are different
if len(arr1) != len(arr2):
    are_equal = False
else:
    # Check character by character
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            are_equal = False
            break

if are_equal == True:
    print("Arrays are equal")
else:
    print("Arrays are not equal")
