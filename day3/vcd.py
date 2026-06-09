s=input("enter the string")
vowels=0
consonants=0
digits=0
specials=0
for i in s:
    if i.isalpha():
        if i in "aeiouAEIOU":
            vowels+=1
        else:
            consonants+=1
    elif i.isdigit():
        digits+=1
    else:
        specials+=1
print("number of vowels",vowels)
print("number of consonants",consonants)
print("number of digits",digits)
print("number of specials",specials)
