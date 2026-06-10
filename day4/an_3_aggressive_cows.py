# Aggressive Cows (Simplest readable logic)
# Given positions of stalls, place cows such that minimum distance between them is as large as possible.
stalls = [1, 2, 4, 8, 9]
cows = 3

# Make sure stalls are sorted first
for i in range(len(stalls)):
    for j in range(len(stalls) - 1 - i):
        if stalls[j] > stalls[j + 1]:
            temp = stalls[j]
            stalls[j] = stalls[j + 1]
            stalls[j + 1] = temp

# Try all possible distances starting from 1
max_distance = 0
distance_to_check = 1
max_possible_distance = stalls[-1] - stalls[0]

while distance_to_check <= max_possible_distance:
    cows_placed = 1
    last_position = stalls[0]
    
    # Try to place all cows
    for i in range(1, len(stalls)):
        current_stall = stalls[i]
        if current_stall - last_position >= distance_to_check:
            cows_placed = cows_placed + 1
            last_position = current_stall
            
    # Check if we successfully placed all cows
    if cows_placed >= cows:
        max_distance = distance_to_check
        distance_to_check = distance_to_check + 1
    else:
        # If we can't place them with this distance, we can't with a larger distance either
        break

print("Largest minimum distance:", max_distance)
