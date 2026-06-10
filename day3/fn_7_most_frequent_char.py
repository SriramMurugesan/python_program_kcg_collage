# Find the most frequent character
text = "success"

unique_chars = []
counts = []

for i in range(len(text)):
    char = text[i]
    found = False
    for j in range(len(unique_chars)):
        if unique_chars[j] == char:
            counts[j] = counts[j] + 1
            found = True
            break
            
    if found == False:
        unique_chars.append(char)
        counts.append(1)

max_count = 0
most_frequent = ''

for i in range(len(unique_chars)):
    if counts[i] > max_count:
        max_count = counts[i]
        most_frequent = unique_chars[i]

print("Most frequent character:", most_frequent)
