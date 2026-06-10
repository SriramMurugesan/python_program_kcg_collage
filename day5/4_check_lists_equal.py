# Check if two lists are equal
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]

are_equal = True

if len(list1) != len(list2):
    are_equal = False
else:
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            are_equal = False
            break

if are_equal == True:
    print("The lists are equal")
else:
    print("The lists are NOT equal")
