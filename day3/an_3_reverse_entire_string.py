# Reverse entire string
text = "hello"
reversed_text = ""

# Start from the end and go to 0
for i in range(len(text) - 1, -1, -1):
    reversed_text = reversed_text + text[i]

print("Reversed string:", reversed_text)
