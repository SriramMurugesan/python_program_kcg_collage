# Count vowels, consonants, digits, and special characters
text = "Hello World! 123"

vowels_count = 0
consonants_count = 0
digits_count = 0
special_count = 0

vowels = "aeiouAEIOU"

for i in range(len(text)):
    char = text[i]
    
    # Check if alphabet
    if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
        # Check if vowel
        is_vowel = False
        for v in vowels:
            if char == v:
                is_vowel = True
                break
                
        if is_vowel == True:
            vowels_count = vowels_count + 1
        else:
            consonants_count = consonants_count + 1
            
    # Check if digit
    elif char >= '0' and char <= '9':
        digits_count = digits_count + 1
        
    # Check if special character (excluding spaces)
    elif char != ' ':
        special_count = special_count + 1

print("Vowels:", vowels_count)
print("Consonants:", consonants_count)
print("Digits:", digits_count)
print("Special Characters:", special_count)
