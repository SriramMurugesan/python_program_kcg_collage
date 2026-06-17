# Day 2: Arrays (Basic Algorithms)

### Foundational
1. **Array vs List:** In Python, lists are often treated as arrays. What is the fundamental difference between a true fixed-size Array (like in C/Java or Python's `array` module) and a Python List?
2. **Basic Searches:** What are the time and space complexities of finding the maximum and minimum elements in an unsorted array simultaneously? Can it be done in fewer than $2N$ comparisons?

### Deep & Tricky
3. **Dutch National Flag:** You are given an array containing only 0s, 1s, and 2s. How do you sort this array in a single pass ($O(N)$ time) with $O(1)$ extra space? Explain the 3-pointer approach.
4. **Pivot Index:** Explain how to find the "pivot index" (equilibrium index) of an array where the sum of elements to the left equals the sum of elements to the right. How can you optimize this from $O(N^2)$ to $O(N)$?
5. **Missing Number Math:** Given an array containing $N$ distinct numbers taken from $0, 1, 2, ..., N$, find the one missing from the array. Can you do this using XOR to prevent integer overflow issues?

### Placement-Level Problem Solving
6. **Moore's Voting Algorithm:** Explain the logic behind finding the Majority Element (an element appearing more than $\lfloor N/2 \rfloor$ times) in $O(N)$ time and $O(1)$ space. Prove why the algorithm is guaranteed to work if a majority element exists.
7. **Stock Buy and Sell (Variations):** 
    - *Variation 1:* You can only buy once and sell once. Find the max profit.
    - *Variation 2:* You can buy and sell multiple times to maximize profit. Explain the greedy approach to solve this.
