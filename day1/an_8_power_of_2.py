# Determine whether a number is a power of 2
num = 16

# Keep dividing by 2 as long as it is an even number
while num > 1:
    if num % 2 != 0:
        break
    num = num // 2

if num == 1:
    print("Power of 2")
else:
    print("Not a Power of 2")
