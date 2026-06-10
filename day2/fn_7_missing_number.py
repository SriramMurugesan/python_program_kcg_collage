# Find the missing number in an array of 1 to N
arr = [1, 2, 4, 5, 6]
n = 6

# Calculate expected sum from 1 to N using a loop
expected_sum = 0
for i in range(1, n + 1):
    expected_sum = expected_sum + i

# Calculate the actual sum of the array
actual_sum = 0
for i in range(len(arr)):
    actual_sum = actual_sum + arr[i]

missing_number = expected_sum - actual_sum
print("Missing number:", missing_number)
