# Group Words by Length
words = ["cat", "dog", "apple", "bat", "banana", "kiwi"]

grouped_words = {}

for i in range(len(words)):
    word = words[i]
    
    # Manually count the length of the word
    word_length = 0
    for char in word:
        word_length = word_length + 1
        
    # Check if this length is already a key in our dictionary
    if word_length in grouped_words:
        # If it is, append the word to the existing list
        grouped_words[word_length].append(word)
    else:
        # If it's a new length, create a new list with this word
        grouped_words[word_length] = [word]

print("Words grouped by length:")
for length in grouped_words:
    print("Length", length, ":", grouped_words[length])
