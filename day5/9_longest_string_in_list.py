# Find the longest string in a list
words = ["apple", "banana", "strawberry", "kiwi", "grape"]

longest_word = words[0]
max_length = len(words[0])

for i in range(len(words)):
    current_word = words[i]
    current_length = 0
    
    # Manually count the length of the string
    for char in current_word:
        current_length = current_length + 1
        
    if current_length > max_length:
        longest_word = current_word
        max_length = current_length

print("The longest string is:", longest_word)
