# Find the product of digits of a number
num = 1234
product = 1

while num > 0:
    last_digit = num % 10
    product = product * last_digit
    num = num // 10

print("Product of digits:", product)
