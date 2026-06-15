# Ultimate Placement Preparation Guide: Python & Data Structures

This document provides a highly comprehensive, day-wise breakdown of placement-level interview questions. It is designed to take you from foundational understanding to deep, edge-case technical knowledge. It covers everything from Day 1 to Day 11 of your curriculum. 

If you master the "Deep & Tricky" and "Placement-Level" sections, you will be exceptionally well-prepared for any rigorous technical interview.

---

## Day 1: Basic Math, Loops, and Pattern Printing

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

---

## Day 2: Arrays (Basic Algorithms)

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

---

## Day 3: Strings & Character Arrays

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

---

## Day 4: Searching & Sorting

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

---

## Day 5: Python Lists and Deep Data Structures

### Foundational
1. **Dynamic Arrays:** Explain how a Python List works under the hood. What does it mean that it is dynamically resized?
2. **CRUD Operations:** What is the time complexity of `append()`, `insert(0, val)`, `pop()`, and `remove(val)`? Why is inserting at the beginning of a list computationally expensive?

### Deep & Tricky
3. **Amortized Analysis:** If a Python list is full, adding a new element requires allocating a new memory block and copying old elements. Why do we still say `append()` operates in $O(1)$ amortized time?
4. **Deep vs. Shallow Copy:** Explain the exact difference between `list_b = list_a[:]`, `list_b = list(list_a)`, and `list_b = copy.deepcopy(list_a)`. Give a code scenario where shallow copy causes an unintended bug.
5. **Advanced Slicing:** Explain what happens when you use negative strides in list slicing: `my_list[::-1]`. What does `my_list[-5:-1:-1]` return and why?

### Placement-Level Problem Solving
6. **List Comprehension Complexities:** Convert a nested `for` loop containing an `if/else` condition into a single-line list comprehension. What are the memory advantages of doing this? When is a generator expression `()` preferred over list comprehension `[]`?
7. **Flattening:** Write a robust function to flatten a deeply nested list of unknown depth (e.g., `[1, [2, [3, 4], 5], 6]`) without using external libraries.

---

## Day 6: Tuples, Sets, Dictionaries

### Foundational
1. **Tuples:** Why do Tuples exist if Lists do everything Tuples do and more? What are the performance and safety benefits of immutability?
2. **Sets:** What is the underlying data structure of a Python Set? What is the average time complexity for checking if an item exists in a Set?

### Deep & Tricky
3. **Dictionary Ordering:** Prior to Python 3.7, dictionaries were unordered. How does modern Python maintain the insertion order of dictionaries internally?
4. **Hashability:** What makes an object "hashable" in Python? Can you use a Tuple as a dictionary key? Can you use a List? Explain why.
5. **Hash Collisions:** What happens internally when two different keys in a dictionary evaluate to the exact same hash value? How does Python handle this collision?

### Placement-Level Problem Solving
6. **Dictionary Sorting:** Given a list of dictionaries representing students (keys: `name`, `age`, `marks`), write code to sort the list primarily by `marks` (descending) and secondarily by `name` (alphabetical).
7. **Set Operations in Practice:** You have two massive datasets of user IDs. How do you optimally find users who exist in Dataset A but NOT in Dataset B, without using loops?

---

## Day 7: Functions, Scope, Decorators, Map

### Foundational
1. **LEGB Rule:** Explain the Scope Resolution (LEGB: Local, Enclosing, Global, Built-in) in Python. 
2. **First-Class Citizens:** What does it mean when we say "Functions are first-class citizens in Python"? How does this enable features like `map()` and `filter()`?

### Deep & Tricky
3. **Mutable Default Arguments:** Explain why this code is a classic Python trap:
   ```python
   def add_item(item, my_list=[]):
       my_list.append(item)
       return my_list
   ```
   How do you correctly implement a default empty list argument?
4. **Closures:** What exactly is a closure? Write a closure function that acts as a counter, remembering its state between calls without using global variables.

### Placement-Level Problem Solving
5. **Custom Decorators:** Write a Python decorator `@execution_time` that calculates and prints the exact time taken by the decorated function to execute.
6. **Decorator Chaining:** What happens when you apply two decorators to a single function? Explain the order of execution.
7. **Map and Filter with Lambda:** Given a list of strings, use `map` and `filter` with `lambda` functions in a single line to return the lengths of only the strings that start with a vowel.

---

## Day 8: Classes, Objects, Inheritance

### Foundational
1. **OOP Core:** Define Classes, Objects, Instance Variables, and Class Variables. How do you define a class variable, and when should you use it?
2. **Constructors:** What is the purpose of the `__init__` method? What happens if you forget to include `self` as the first parameter?

### Deep & Tricky
3. **The `super()` Function:** How does `super()` work? In the context of inheritance, why is `super().__init__()` preferred over calling `ParentClass.__init__(self)` explicitly?
4. **Method Resolution Order (MRO):** In Multiple Inheritance, what is the "Diamond Problem"? How does Python's C3 Linearization algorithm resolve MRO to prevent infinite loops and ambiguity?

### Placement-Level Problem Solving
5. **Banking System Architecture:** Design a basic Banking System using OOP. Create a `BankAccount` base class and `SavingsAccount` / `CurrentAccount` subclasses. Demonstrate how overriding is used to apply different interest rate logics.
6. **Magic / Dunder Methods:** How would you allow two `BankAccount` objects to be added together using the `+` operator? Implement the `__add__` dunder method to return the sum of their balances.

---

## Day 9: Polymorphism, Encapsulation, Access Modifiers

### Foundational
1. **Polymorphism in Python:** Python does not natively support "Method Overloading" (having multiple functions with the same name but different signatures). How do you achieve overloading behavior using default arguments or `*args`/`**kwargs`?
2. **Access Modifiers:** Does Python have true `private` variables? Explain what single underscore (`_var`) and double underscore (`__var`) conventions mean.

### Deep & Tricky
3. **Name Mangling:** What is Name Mangling? If you create a variable `__balance` inside a `Bank` class, can a user still access and modify it from outside the class? If yes, how?
4. **Duck Typing:** "If it walks like a duck and quacks like a duck, it must be a duck." Explain this concept with Python code. How does this provide dynamic polymorphism?

### Placement-Level Problem Solving
5. **The `@property` Decorator:** Why are getters and setters considered un-Pythonic when used directly? Rewrite a class with private variables using `@property`, `@attribute.setter`, and `@attribute.deleter` to encapsulate the data cleanly.
6. **Encapsulation Pitfalls:** What are the actual architectural problems with strictly enforcing Encapsulation in a dynamically typed language like Python compared to Java?

---

## Day 10: Abstract Classes and Iterators

### Foundational
1. **Abstract Base Classes (ABC):** What is an abstract class? Why would an architecture require you to use the `abc` module to define one instead of just a regular parent class?
2. **Instantiation:** Why does Python throw an error if you attempt to instantiate an Abstract Class? 

### Deep & Tricky
3. **Iterables vs. Iterators:** What is the technical difference between an Iterable (like a list) and an Iterator? Explain how the `__iter__()` and `__next__()` methods work together.
4. **Generators:** How does the `yield` keyword turn a normal function into a Generator? Why is a generator considered an elegant way to create custom iterators?

### Placement-Level Problem Solving
5. **Abstract Properties:** How do you enforce that a child class MUST implement a specific property variable using `@abstractproperty` (or `@property` stacked with `@abstractmethod`)?
6. **Infinite Streams:** Write a generator function that yields prime numbers indefinitely. How does this demonstrate the extreme memory efficiency of generators over lists for large data processing?

---

## Day 11: File Management, Exceptions, and Leetcode Setup

### Foundational
1. **File I/O:** Explain the differences between the `r`, `w`, `a`, `r+`, and `a+` file opening modes. Why is the `with open(...) as f:` syntax considered the industry standard?
2. **Exception Hierarchy:** What is the base class for all exceptions in Python? Why is having a bare `except:` block considered bad practice?

### Deep & Tricky
3. **Try-Except-Else-Finally:** Explain the precise execution flow of a complete `try-except-else-finally` block. If the `try` block hits a `return` statement, will the `finally` block still execute?
4. **Custom Exceptions:** How do you create and raise a custom `InsufficientBalanceError` exception class inherited from Python's base `Exception`?

### Placement-Level Problem Solving
5. **Large File Processing:** You need to process a 10GB CSV file on a machine with 2GB of RAM. How do you do this using Python file management or generators to prevent a MemoryError?
6. **Robust Data Ingestion Pipeline:** Write a mock script that attempts to read data from `data.csv`. Implement robust exception handling that specifically catches `FileNotFoundError`, catches `ValueError` for type casting issues within the data, and logs any other unknown errors to a separate `error.log` file, ensuring the script does not crash the server.
