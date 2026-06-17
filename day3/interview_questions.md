# Day 3: Strings & Character Arrays

### Foundational
1. **Immutability:** Strings in Python are immutable. What does this mean for memory allocation when you repeatedly concatenate strings in a loop? What is the efficient alternative?
2. **ASCII & Unicode:** What is the difference between ASCII and Unicode? How do `ord()` and `chr()` functions work in Python?

### Deep & Tricky
3. **Anagram Checking:** Compare three ways to check if two strings are anagrams: 
    - Using `sorted()`
    - Using `collections.Counter`
    - Using an integer array of size 26 (for lowercase English letters). 
    Discuss the time and space complexities of each. Which is preferred for massive strings?
4. **In-Place Reversal:** How do you reverse a character array in-place? Explain the two-pointer swapping approach.

### Placement-Level Problem Solving
5. **Reverse Words without Built-ins:** Given a sentence, reverse the order of the words without using Python's built-in `.split()` or `.reverse()`. (Hint: Reverse the whole string, then reverse each individual word).
6. **Longest Palindromic Substring:** What is the "Expand Around Center" approach to finding the longest palindromic substring? Why is it better than the brute-force $O(N^3)$ approach?
7. **String Compression:** Write an algorithm to compress a string (e.g., "aabcccccaaa" becomes "a2b1c5a3"). If the compressed string isn't smaller than the original, return the original.
