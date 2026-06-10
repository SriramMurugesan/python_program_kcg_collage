# Copy one character array to another without using inbuilt functions
source = ['h', 'e', 'l', 'l', 'o']
destination = []

for i in range(len(source)):
    char = source[i]
    destination.append(char)

print("Copied array:", destination)
