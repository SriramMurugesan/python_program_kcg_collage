# Find the intersection of two lists (common elements)
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

intersection = []

for i in range(len(list1)):
    current_element = list1[i]
    
    # Check if current_element is also in list2
    for j in range(len(list2)):
        if list2[j] == current_element:
            # We found a common element
            
            # Make sure we don't add duplicates to the intersection
            already_added = False
            for k in range(len(intersection)):
                if intersection[k] == current_element:
                    already_added = True
                    break
                    
            if already_added == False:
                intersection.append(current_element)
            break

print("Intersection of lists:", intersection)
