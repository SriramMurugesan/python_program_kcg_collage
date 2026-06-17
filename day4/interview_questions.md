# Day 4: Searching & Sorting

### Foundational
1. **Search Strategies:** When would you explicitly choose Linear Search over Binary Search? 
2. **Bubble Sort Basics:** Explain how Bubble Sort works. What is the time complexity in the worst case, and how can you optimize it to $O(N)$ for the best case?

### Deep & Tricky
3. **Binary Search Variations:** How do you use Binary Search to find the *first* or *last* occurrence of a target number in a sorted array that contains duplicates?
4. **Rotated Sorted Array:** A sorted array is rotated at an unknown pivot (e.g., `[4, 5, 6, 7, 0, 1, 2]`). How do you perform a search for a target element in $O(\log N)$ time?
5. **Frequency Sort:** Given an array, sort the elements based on their frequency. If two elements have the same frequency, sort them by their value. What data structures would you combine to do this efficiently?

### Placement-Level Problem Solving
6. **Aggressive Cows (Binary Search on Answer):** You have $N$ stalls and $C$ cows. You need to place the cows in the stalls such that the minimum distance between any two cows is maximized. Explain how to define the monotonic search space and apply Binary Search to find this answer.
7. **Insertion Position:** Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. Write the $O(\log N)$ solution.
