# Find First Non-Repeating Character
text = "swiss"

# We will use a dictionary to count how many times each character appears
char_counts = {}

# Count each character
for i in range(len(text)):
    char = text[i]
    if char in char_counts:
        char_counts[char] = char_counts[char] + 1
    else:
        char_counts[char] = 1

# Now go through the string again to find the first one with a count of 1
first_unique = ""

for i in range(len(text)):
    char = text[i]
    if char_counts[char] == 1:
        first_unique = char
        break

if first_unique != "":
    print("First non-repeating character is:", first_unique)
else:
    print("No non-repeating character found")
