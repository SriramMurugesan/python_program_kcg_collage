# Day 7: Functions, Scope, Decorators, Map

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
