# Anagram check
word1 = "listen"
word2 = "silent"

is_anagram = True

if len(word1) != len(word2):
    is_anagram = False
else:
    # Convert to lists to sort
    arr1 = list(word1)
    arr2 = list(word2)
    
    # Sort arr1
    for i in range(len(arr1)):
        for j in range(len(arr1) - 1 - i):
            if arr1[j] > arr1[j + 1]:
                temp = arr1[j]
                arr1[j] = arr1[j + 1]
                arr1[j + 1] = temp
                
    # Sort arr2
    for i in range(len(arr2)):
        for j in range(len(arr2) - 1 - i):
            if arr2[j] > arr2[j + 1]:
                temp = arr2[j]
                arr2[j] = arr2[j + 1]
                arr2[j + 1] = temp
                
    # Compare sorted arrays
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            is_anagram = False
            break

if is_anagram == True:
    print("They are Anagrams")
else:
    print("Not Anagrams")
