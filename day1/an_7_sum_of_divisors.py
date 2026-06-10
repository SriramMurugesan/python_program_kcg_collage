# Find the sum of all divisors of a number
num = 12
total_sum = 0

for i in range(1, num + 1):
    if num % i == 0:
        total_sum = total_sum + i

print("Sum of divisors:", total_sum)
