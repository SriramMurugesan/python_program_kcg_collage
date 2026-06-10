# Count the total divisors of a number
num = 12
count = 0

for i in range(1, num + 1):
    # If the remainder is 0, it is a divisor
    if num % i == 0:
        count = count + 1

print("Total divisors:", count)
