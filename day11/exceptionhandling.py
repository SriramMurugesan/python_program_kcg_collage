# while True:
#     try:
#         num=int(input("enter a number"))
#         if num<0:
#             print(0)
#     except ValueError:
#         print("Invalid input")
#     except:
#         print("Error")
    
# x=int(input("enter a value"))
# print(x)

# try:
#     print(1/10)
#     num=int(input("enter a number"))
# except ZeroDivisionError:
#     print("zerodivisionerror")
# except ValueError:
#     print("valueerror")
# else:
#     print("no error")

# try:
#     f=open("data.txt","r")
# except FileNotFoundError:
#     print("filenotfound")
# else:
#     print(f.read())
# finally:
#     f.close()

# def checkage(age):
#     if age<18:
#         raise ValueError("not eligible")
#     else:
#         print("eligible")

# try:
#     checkage(17)
# except ValueError as e:
#     print(e)

# custom exception
# class MyException(Exception):
#     pass
# try:
#     num=int(input("enter a number"))
#     if num<0:
#         raise MyException("negative number not allowed")
#     else:
#         print(num)
# except MyException as e:
#     print(e)