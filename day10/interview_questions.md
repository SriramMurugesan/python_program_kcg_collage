# Day 10: Abstract Classes and Iterators

### Foundational
1. **Abstract Base Classes (ABC):** What is an abstract class? Why would an architecture require you to use the `abc` module to define one instead of just a regular parent class?
2. **Instantiation:** Why does Python throw an error if you attempt to instantiate an Abstract Class? 

### Deep & Tricky
3. **Iterables vs. Iterators:** What is the technical difference between an Iterable (like a list) and an Iterator? Explain how the `__iter__()` and `__next__()` methods work together.
4. **Generators:** How does the `yield` keyword turn a normal function into a Generator? Why is a generator considered an elegant way to create custom iterators?

### Placement-Level Problem Solving
5. **Abstract Properties:** How do you enforce that a child class MUST implement a specific property variable using `@abstractproperty` (or `@property` stacked with `@abstractmethod`)?
6. **Infinite Streams:** Write a generator function that yields prime numbers indefinitely. How does this demonstrate the extreme memory efficiency of generators over lists for large data processing?
