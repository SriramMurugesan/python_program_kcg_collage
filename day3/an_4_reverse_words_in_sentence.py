# Reverse words in a sentence
sentence = "hello world"
words = []
current_word = ""

# First, split the sentence into words
for i in range(len(sentence)):
    char = sentence[i]
    if char == " ":
        if current_word != "":
            words.append(current_word)
        current_word = ""
    else:
        current_word = current_word + char
        
# Add the last word
if current_word != "":
    words.append(current_word)

# Now reverse each word
result = ""
for i in range(len(words)):
    word = words[i]
    reversed_word = ""
    
    # Reverse characters in this word
    for j in range(len(word) - 1, -1, -1):
        reversed_word = reversed_word + word[j]
        
    result = result + reversed_word
    
    # Add space between words
    if i < len(words) - 1:
        result = result + " "

print("Words reversed:", result)
