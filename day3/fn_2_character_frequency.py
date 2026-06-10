# Find the frequency of each character
text = "hello"

# We will use two arrays to track characters and their counts
unique_chars = []
counts = []

for i in range(len(text)):
    char = text[i]
    
    # Check if we already saw this character
    found = False
    for j in range(len(unique_chars)):
        if unique_chars[j] == char:
            counts[j] = counts[j] + 1
            found = True
            break
            
    # If it is a new character
    if found == False:
        unique_chars.append(char)
        counts.append(1)

for i in range(len(unique_chars)):
    print("Character", unique_chars[i], "appears", counts[i], "times")
