# Find the sum of digits of a number
num = 1234
total_sum = 0

while num > 0:
    last_digit = num % 10
    total_sum = total_sum + last_digit
    num = num // 10

print("Sum of digits:", total_sum)
