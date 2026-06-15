# polymorphism
# print(len("kjdbcjkbcj"))
# print(len([1,2,3,4]))
# class Animal:
#     def sound(self):
#         return "Sound"
# class  Dog(Animal):
#     def sound(self):
#         return "Woof"
# class Cat(Animal):
#     def sound(self):
#         return "Meow"
# animal=Animal()
# dog=Dog()
# cat=Cat()
# print(animal.sound())
# print(dog.sound())
# print(cat.sound())

# polymorphism with function 
# class Dog:
#     def sound(self):
#         print("Woof")
# class Cat:
#     def sound(self):
#         print("Meow")
# def animal_sound(animal):
#     animal.sound()
# animal_sound(Dog())
# animal_sound(Cat())
# #Encapsulation
# class Student:
#     def __init__(self,name,age,marks):
#         self.name = name   # public variable
#         self._age = age   # protected variable
#         self.__marks = marks # private variable
#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self._age)
#         print("Marks:", self.__marks)
#     def set_marks(self,marks):
#         if 0 <= marks <= 100:
#             self.__marks = marks
#         else:
#             print("Marks should be between 0 and 100")
#     def get_marks(self):
#         return self.__marks
# s1 = Student("Gokul", 25, 100)
# s1.set_marks(150)
# print(s1.get_marks())
# s1._Student__marks=30
# # print(s1.__marks)
# print(s1.get_marks())

# Create a class Employee:
# Private variable: __salary
# Methods:
# set_salary(salary) → only if salary > 0
# get_salary()

#  Try invalid input also

# Create BankAccount:

    # Private: __balance
    # Methods:
    # deposit(amount)
    # withdraw(amount)
    # get_balance()

    #  Conditions:

    # Cannot withdraw more than balance
    # Cannot deposit negative


# student Managemant system
# add student
# view student
# search student
# delete student
# exit
# class StudentManager:
#     def __init__(self):
#         self.students=[]
#     def add_student(self):
#         student_id=int(input("enter student id:"))
#         name=input("Enter Name:")
#         subjects=("Maths","Science","English")
#         marks=[]
#         print("enter marks:")
#         for sub in subjects:
#             mark=int(input(f"{sub}: "))
#             marks.append(mark)
#         student = {
#             "id":student_id,
#             "Name":name,
#             "Subjects":subjects,
#             "marks":marks
#         }
#         self.students.append(student)
#     def view_student(self):
#         if not self.students:
#             print("No students found/")
#             print(self.students)
#             return
#         for s in self.students:
#             print(f"ID:{s['id']},Name:{s['Name']}")
#             print("Subjects:",s["Subjects"])
#             print("Marks:",s["marks"])
#             print("--------------------------")
#     def search_student(self):
#         name=input("Enter student name to search:")
#         for s in self.students:
#             if name.lower()==s["Name"].lower():
#                     print("found",s)
#                     return
#         print("Student not found")
#     def delete_student(self):
#         id = int(input("enter the student_id to delete"))
#         for s in self.students:
#             if id==s["id"]:
#                 self.students.remove(s)
#                 print("Deleted Successfully")
#                 return
#         print("Student not found")

# def main():
#     system=StudentManager()
#     while True:
#         print("1.add student")
#         print("2.view student")
#         print("3.search student")
#         print("4.delete student")
#         print("5.Exitting")
        
#         choice = int(input("Enter your choice:"))
#         if choice ==1:
#             #add student
#             system.add_student()
#         elif choice==2:
#             #view student
#             system.view_student()
#         elif choice==3:
#             #search student
#             system.search_student()
#         elif choice==4:
#             # delete student
#             system.delete_student()
#         elif choice==5:
#             #exit
#             print("exitting...")
#             break
#         else:
#             #enter valid input
#             print("invalid option enter valid option")
# main() 


