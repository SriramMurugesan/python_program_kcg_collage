# Find the union of two lists (all unique elements from both)
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

union_list = []

# Add everything from list1 (without duplicates)
for i in range(len(list1)):
    current_element = list1[i]
    
    already_added = False
    for j in range(len(union_list)):
        if union_list[j] == current_element:
            already_added = True
            break
            
    if already_added == False:
        union_list.append(current_element)

# Add everything from list2 (without duplicates)
for i in range(len(list2)):
    current_element = list2[i]
    
    already_added = False
    for j in range(len(union_list)):
        if union_list[j] == current_element:
            already_added = True
            break
            
    if already_added == False:
        union_list.append(current_element)

print("Union of lists:", union_list)
