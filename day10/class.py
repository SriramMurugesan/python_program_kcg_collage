# Create abstract class Shape with method area()
# from abc import ABC,abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class circle(shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return  3.14*self.radius*self.radius
# cir=circle(10)
# print(cir.area())


# class A(ABC):
#     @abstractmethod
#     def show(self):
#         pass

# class B(A):
#     def show(self):
#         print("show")

# obj = B()
#     @abstractmethod
#     def show(self):
#         pass

# class B(A):
#     def show(self):
#         print("show")

# obj = B()
# Add one normal method in abstract class

# Force subclass to define salary

# Print numbers from 1 to 30 using custom iterator it should increment by 3

# All payment methods must follow same rules → use abstract class
# Scenario:

# Company has:

# FullTime employees
# Freelancers

# Salary calculation differs

# Design:

# Force all employees to implement calculate_salary()
class Company(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmployee(Company):
    def __init__(self,salary,allowance):
        self.salary=salary
        self.allowance=allowance
    def calculate_salary(self):
        return self.salary+self.allowance
class Freelancer(Company):
    def __init__(self,days,rate):
        self.days=days
        self.rate=rate
    def calculate_salary(self):
        return self.days*self.rate



# Scenario:

# App sends notifications via:

# Email
# SMS

# Design:

# Force all to implement send()

# Scenario:

# Every user must have role

# Design:

# Force property definition

from abc import ABC, abstractmethod

# class vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
#     def stop(self):
#         print("vehicle stopped")
# class car(vehicle):
#     def start(self):
#         print("car started")
# class bike(vehicle):
#     def start(self):
#         print("bike started")
    

# # c=vehicle()
# v=car()
# b=bike()
# v.start()
# v.stop()
# b.start()
# b.stop()
# abstract properties

class user(ABC):
    @property
    @abstractmethod
    def role(self):
        pass
class admin(user):
    @property
    def role(self):
        return "admin"
x=admin()
# print(x.role())
print(x.role)

# class user(ABC):
#     @property
#     @abstractmethod
#     def role(self):
#         pass
# class admin(user):
#     @property
#     def role(self):
#         return "admin"
# class user(user):
#     @property
#     def role(self):
#         return "user"


# u=admin()
# u1=user()
# print(u.role)
# print(u1.role)
# print(u2.role)

# iterator
class count:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        self.start+=1
        if self.start>self.end:
            raise StopIteration
        return self.start

c1=count(0,10)
print(c1)
for i in c1:
    print(i)

nums=[1,2,3,4,5]
it=iter(nums)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))