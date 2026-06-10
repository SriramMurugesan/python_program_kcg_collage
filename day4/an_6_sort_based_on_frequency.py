# Sort Based on Frequency
arr = [2, 5, 2, 8, 5, 6, 8, 8]

# First, find frequencies
unique_nums = []
counts = []

for i in range(len(arr)):
    num = arr[i]
    found = False
    for j in range(len(unique_nums)):
        if unique_nums[j] == num:
            counts[j] = counts[j] + 1
            found = True
            break
            
    if found == False:
        unique_nums.append(num)
        counts.append(1)

# Sort the unique arrays based on count (Bubble Sort)
for i in range(len(unique_nums)):
    for j in range(len(unique_nums) - 1 - i):
        # Sort by frequency ascending
        if counts[j] > counts[j + 1]:
            # Swap counts
            temp_count = counts[j]
            counts[j] = counts[j + 1]
            counts[j + 1] = temp_count
            
            # Swap numbers to keep them aligned with counts
            temp_num = unique_nums[j]
            unique_nums[j] = unique_nums[j + 1]
            unique_nums[j + 1] = temp_num

# Build final result array based on sorted frequencies
result = []
for i in range(len(unique_nums)):
    num = unique_nums[i]
    frequency = counts[i]
    # Add the number 'frequency' times
    for k in range(frequency):
        result.append(num)

print("Sorted by frequency:", result)
