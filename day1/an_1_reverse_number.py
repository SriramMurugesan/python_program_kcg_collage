# Reverse a given number
num = 12345
reversed_num = 0

while num > 0:
    last_digit = num % 10
    reversed_num = (reversed_num * 10) + last_digit
    # Remove the last digit from num
    num = num // 10

print("Reversed number:", reversed_num)
