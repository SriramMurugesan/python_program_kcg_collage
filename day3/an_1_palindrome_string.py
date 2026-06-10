# Palindrome string
text = "madam"
reversed_text = ""

# Build string backwards
for i in range(len(text) - 1, -1, -1):
    reversed_text = reversed_text + text[i]

if text == reversed_text:
    print("It is a Palindrome")
else:
    print("Not a Palindrome")
