# Reverse the order of words in a string
sentence = "Hi hello"
words = []
current_word = ""

# Split sentence into words
for i in range(len(sentence)):
    char = sentence[i]
    if char == " ":
        if current_word != "":
            words.append(current_word)
        current_word = ""
    else:
        current_word = current_word + char
        
if current_word != "":
    words.append(current_word)

# Now combine the words backwards
result = ""
for i in range(len(words) - 1, -1, -1):
    result = result + words[i]
    # Add a space if it is not the last word we are adding
    if i > 0:
        result = result + " "

print("Reversed order:", result)
