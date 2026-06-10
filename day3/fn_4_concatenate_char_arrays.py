# Concatenate two character arrays without using inbuilt functions
arr1 = ['h', 'i']
arr2 = [' ', 't', 'h', 'e', 'r', 'e']

result = []

for i in range(len(arr1)):
    result.append(arr1[i])

for i in range(len(arr2)):
    result.append(arr2[i])

print("Concatenated array:", result)
