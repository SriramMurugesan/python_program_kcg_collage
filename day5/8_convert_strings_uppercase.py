# Convert a list of strings to uppercase
words = ["hello", "world", "python", "code"]
uppercase_words = []

for i in range(len(words)):
    current_word = words[i]
    new_word = ""
    
    # Go through each character
    for j in range(len(current_word)):
        char = current_word[j]
        
        # If the character is lowercase, convert it
        if char >= 'a' and char <= 'z':
            # Find the ASCII value and subtract 32 to get uppercase
            ascii_value = ord(char)
            uppercase_char = chr(ascii_value - 32)
            new_word = new_word + uppercase_char
        else:
            # If it's not lowercase, just add it as is
            new_word = new_word + char
            
    uppercase_words.append(new_word)

print("Original strings:", words)
print("Uppercase strings:", uppercase_words)
