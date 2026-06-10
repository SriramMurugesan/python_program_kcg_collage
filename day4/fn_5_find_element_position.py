# Find element position (first and last occurrence)
arr = [5, 7, 7, 8, 8, 10]
target = 8

first_pos = -1
last_pos = -1

for i in range(len(arr)):
    if arr[i] == target:
        if first_pos == -1:
            first_pos = i  # Mark the first time we see it
        last_pos = i       # Keep updating the last time we see it

print("First position:", first_pos)
print("Last position:", last_pos)
