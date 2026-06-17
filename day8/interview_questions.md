# Day 8: Classes, Objects, Inheritance

### Foundational
1. **OOP Core:** Define Classes, Objects, Instance Variables, and Class Variables. How do you define a class variable, and when should you use it?
2. **Constructors:** What is the purpose of the `__init__` method? What happens if you forget to include `self` as the first parameter?

### Deep & Tricky
3. **The `super()` Function:** How does `super()` work? In the context of inheritance, why is `super().__init__()` preferred over calling `ParentClass.__init__(self)` explicitly?
4. **Method Resolution Order (MRO):** In Multiple Inheritance, what is the "Diamond Problem"? How does Python's C3 Linearization algorithm resolve MRO to prevent infinite loops and ambiguity?

### Placement-Level Problem Solving
5. **Banking System Architecture:** Design a basic Banking System using OOP. Create a `BankAccount` base class and `SavingsAccount` / `CurrentAccount` subclasses. Demonstrate how overriding is used to apply different interest rate logics.
6. **Magic / Dunder Methods:** How would you allow two `BankAccount` objects to be added together using the `+` operator? Implement the `__add__` dunder method to return the sum of their balances.
