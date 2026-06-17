# Day 6: Tuples, Sets, Dictionaries

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
