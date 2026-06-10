# Flatten dictionary
# We will convert a nested dictionary into a flat one by joining keys with an underscore
nested_dict = {
    "User1": {
        "name": "Alice",
        "age": 25
    },
    "User2": {
        "name": "Bob",
        "age": 30
    }
}

flat_dict = {}

# Loop through the outer dictionary
for outer_key in nested_dict:
    # The value is an inner dictionary
    inner_dict = nested_dict[outer_key]
    
    # Loop through the inner dictionary
    for inner_key in inner_dict:
        inner_value = inner_dict[inner_key]
        
        # Combine the outer key and inner key (e.g., "User1_name")
        combined_key = outer_key + "_" + inner_key
        
        # Add to the flat dictionary
        flat_dict[combined_key] = inner_value

print("Nested Dictionary:", nested_dict)
print("Flattened Dictionary:", flat_dict)
