# Day 5: Python Lists and Deep Data Structures

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
