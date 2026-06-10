# Find first element > target
arr = [2, 3, 5, 9, 14, 16, 18]
target = 9

answer = -1

for i in range(len(arr)):
    if arr[i] > target:
        answer = arr[i]
        break

print("First element > target:", answer)
