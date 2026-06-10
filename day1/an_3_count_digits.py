# Count the number of digits in a given number
num = 98765
count = 0

while num > 0:
    count = count + 1
    num = num // 10

print("Number of digits:", count)
