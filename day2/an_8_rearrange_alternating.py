# Rearrange array in alternating positive and negative numbers
arr = [3, 1, -2, -5, 2, -4]

positives = []
negatives = []

# Separate into positive and negative arrays
for i in range(len(arr)):
    if arr[i] > 0:
        positives.append(arr[i])
    elif arr[i] < 0:
        negatives.append(arr[i])

result = []
pos_index = 0
neg_index = 0

# Add them alternately
while pos_index < len(positives) and neg_index < len(negatives):
    result.append(positives[pos_index])
    pos_index = pos_index + 1
    
    result.append(negatives[neg_index])
    neg_index = neg_index + 1

# Add any remaining positive numbers
while pos_index < len(positives):
    result.append(positives[pos_index])
    pos_index = pos_index + 1

# Add any remaining negative numbers
while neg_index < len(negatives):
    result.append(negatives[neg_index])
    neg_index = neg_index + 1

print("Rearranged array:", result)
