# Invert Dictionary (Swap keys and values)
original_dict = {"apple": "red", "banana": "yellow", "grape": "purple"}

inverted_dict = {}

# Go through each key in the original dictionary
for key in original_dict:
    # Get the value
    value = original_dict[key]
    
    # Set the value as the new key, and the old key as the new value
    inverted_dict[value] = key

print("Original:", original_dict)
print("Inverted:", inverted_dict)
