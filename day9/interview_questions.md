# Day 9: Polymorphism, Encapsulation, Access Modifiers

### Foundational
1. **Polymorphism in Python:** Python does not natively support "Method Overloading" (having multiple functions with the same name but different signatures). How do you achieve overloading behavior using default arguments or `*args`/`**kwargs`?
2. **Access Modifiers:** Does Python have true `private` variables? Explain what single underscore (`_var`) and double underscore (`__var`) conventions mean.

### Deep & Tricky
3. **Name Mangling:** What is Name Mangling? If you create a variable `__balance` inside a `Bank` class, can a user still access and modify it from outside the class? If yes, how?
4. **Duck Typing:** "If it walks like a duck and quacks like a duck, it must be a duck." Explain this concept with Python code. How does this provide dynamic polymorphism?

### Placement-Level Problem Solving
5. **The `@property` Decorator:** Why are getters and setters considered un-Pythonic when used directly? Rewrite a class with private variables using `@property`, `@attribute.setter`, and `@attribute.deleter` to encapsulate the data cleanly.
6. **Encapsulation Pitfalls:** What are the actual architectural problems with strictly enforcing Encapsulation in a dynamically typed language like Python compared to Java?
