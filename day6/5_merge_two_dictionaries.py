# Merge Two Dictionaries
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "d": 4, "e": 5}

merged_dict = {}

# First, add everything from dict1
for key in dict1:
    merged_dict[key] = dict1[key]

# Next, add everything from dict2
for key in dict2:
    # If the key already exists (like "b"), it will be overwritten by dict2's value
    merged_dict[key] = dict2[key]

print("Dict 1:", dict1)
print("Dict 2:", dict2)
print("Merged Dict:", merged_dict)
