# OOPs in Python

# class
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
# # p1 = Person("Gokul", 25)
# # p2 = Person("Sriram", 27)
# # p1.display()
# # p2.display()
# # inheritance
# # single inheritance
# class Student(Person):
#     def __init__(self,name,age,grade):
#         super().__init__(name,age)
#         self.grade = grade
#     def display(self):
#         super().display()
#         print("Grade:", self.grade)
# # s1 = Student("Gokul", 25, "A")
# # s1.display()
# # multiple inheritance
# class A:
#     def show(self):
#         print("Method A")
# class B:
#     def show(self):
#         print("Method B")
# class C(B,A):
#     pass
#     # def show(self):
#     #     print("Method C")
# c1 = C()
# c1.show()
# print(C.mro()) 
# # create a class that take length and breadth as input and it should return the area of the rectangle
# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         return self.length * self.breadth
# r1 = Rectangle(5,10)
# x=r1.area()
# print(x)

# class counter:
#     count = 0
#     def __init__(self):
#         counter.count += 1
# c1 = counter()
# c2 = counter()
# c3 = counter()
# print(counter.count)

# Bank Account with savings account, current account and loan account and it should have methods like deposit, withdraw and display balance , each child should have different interest rate and it should calculate the interest based on the balance and the interest rate
class BankAccount:
    def __init__(self,name,acc_number, balance):
        self.name = name
        self.acc_number = acc_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")
    def display_balance(self):
        print("Name:", self.name)
        print("Account Number:", self.acc_number)
        print("Balance:", self.balance)
class SavingsAccount(BankAccount):
    def __init__(self,name,acc_number,balance):
        super().__init__(name,acc_number, balance)
    def calculate_interest(self):
        return self.balance * 3/ 100
    def principal_amount(self):
        return self.balance + self.calculate_interest()
# s1 = SavingsAccount("Gokul", "1234567890", 10000, 5)
# s1.deposit(5000)
# s1.withdraw(2000)
# s1.display_balance()
# s1.calculate_interest()
# print(s1.principal_amount())
class CurrentAccount(BankAccount):
    def __init__(self,name,acc_number,balance):
        super().__init__(name,acc_number, balance)
    def calculate_interest(self):
        return self.balance * 0
    def principal_amount(self):
        return self.balance + self.calculate_interest()
# c1 = CurrentAccount("Sriram", "0987654321", 20000, 0)
# c1.deposit(10000)
# c1.withdraw(5000)
# c1.calculate_interest()
# print(c1.principal_amount())
class LoanAccount(BankAccount):
    def __init__(self,name,acc_number,balance):
        super().__init__(name,acc_number, balance)
    def calculate_interest(self):
        return self.balance * 9 / 100
    def total_amount(self):
        return self.balance + self.calculate_interest()
    def repay_loan(self, amount):
        if amount >= self.total_amount():
            self.balance = 0
            print("Loan repaid successfully")
        else:
            self.balance -= amount
            print("Partial payment made, remaining balance:", self.balance)
# l1 = LoanAccount("Gokul", "1122334455", 50000)

# create class for product with discount price it should calc disc and return the final price after discount
class Product:
    def __init__(self,price,discount):
        self.price = price
        self.discount = discount
    def final_price(self):
        return self.price - (self.price * self.discount / 100)
p1 = Product(1000, 10)
print(p1.final_price())

#single inheritance
# create class employee with name and salary and create class manager that inherits employee and it should have a method to calculate bonus based on salary
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
class Manager(Employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus = bonus
    def calculate_bonus(self):
        return self.bonus
    def total_salary(self):
        return self.salary + self.calculate_bonus()