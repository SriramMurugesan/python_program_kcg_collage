# Day 1: Basic Math, Loops, and Pattern Printing

### Foundational
1. **Modulo Operator:** How does modulo division work for extracting the last digit of a number? Write a script to continuously sum the digits of a number until a single digit remains.
2. **Loop Flow:** Explain the exact differences between `break`, `continue`, and `pass` statements within a loop. Provide an example where `pass` is strictly necessary.
3. **Pattern Logic:** What is the standard algorithmic approach to printing any symmetrical star pattern (e.g., pyramids, diamonds)? Explain the relationship between rows, spaces, and stars.

### Deep & Tricky
4. **Float Precision in Loops:** Why is it dangerous to use floating-point numbers as loop counters or for exact equality checks (e.g., `while x != 1.0`)? 
5. **Factorial Zeros:** How would you calculate the number of trailing zeros in the factorial of a large number (like $100!$) *without* actually computing the factorial? Explain the prime factorization logic behind this.
6. **Negative Palindromes:** When checking if an integer is a palindrome, how do you handle negative numbers? Are they considered palindromes by standard definitions?

### Placement-Level Problem Solving
7. **Bitwise Power of 2:** Write an $O(1)$ time complexity approach to check if a given integer is a power of 2 using bitwise operators. Explain why `(n & (n - 1)) == 0` works.
8. **Optimal Divisors:** What is the most optimal way to find all divisors of a number $N$? Explain why iterating up to $\sqrt{N}$ is sufficient and how you extract the corresponding pair for each divisor.
9. **Pattern Optimization:** How do you dynamically center a complex diamond pattern for an arbitrary size $N$ using optimal nested loops and minimal print statements?
