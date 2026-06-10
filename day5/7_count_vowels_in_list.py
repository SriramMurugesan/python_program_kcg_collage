# Count vowels in a list of characters
char_list = ['a', 'b', 'e', 'z', 'i', 'x', 'o', 'U']

vowels = "aeiouAEIOU"
vowel_count = 0

for i in range(len(char_list)):
    current_char = char_list[i]
    
    # Check if the character is inside the vowels string
    is_vowel = False
    for j in range(len(vowels)):
        if current_char == vowels[j]:
            is_vowel = True
            break
            
    if is_vowel == True:
        vowel_count = vowel_count + 1

print("Total vowels in the list:", vowel_count)
