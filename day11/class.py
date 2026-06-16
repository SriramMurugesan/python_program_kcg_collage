# f = open("demo.txt", "w")
# f.write("Hello Students")
# f.close()
# f = open("demo.txt", "r")
# print(f.read())
# print(f.readline())    # one line
# print(f.readlines())   # list of lines
# f.close()
# f = open("demo.txt", "a")
# f.write("\nNew Line")
# f.close()
# f = open("demo.txt", "r")
# print(f.read(5))

# f.seek(10)
# print(f.read())

# f.seek(0)

# print(f.read())
# import csv

# with open("data.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Name", "Age"])
#     writer.writerow(["Sriram", 22])
# with open("data.csv", "r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
# import json

# data = {"name": "Sriram", "age": 22}

# with open("data.json", "w") as f:
#     json.dump(data, f)
# with open("data.json", "r") as f:
#     data = json.load(f)
#     print(data)
# try:
#     num = int("abc")


# except ValueError:
#     print("Invalid number")
# except:
#     print("Error")

# try:
#     print(10 / 0)
# finally:
#     print("Handled error")

# add exception handling to the following code
# a = int(input("Enter number: "))
# b = int(input("Enter number: "))

# print(a / b)

# find whats wrong with the following code
# try:
#     num = int("abc")
# except:
#     print("Error")

# except ValueError:
#     print("Invalid number")

# what should we add here to handle file 
# try:
#     f = open("data.txt", "r")
#     print(f.read())
# except FileNotFoundError:
#     print("File not found")

# if we didnt define num how can we handle num undefined error
# try:
#     num = int(input("Enter number: "))
# except ValueError:
#     print("Invalid input")

# print(num)

# is this valid
# try:
#     print(10 / 0)
# finally:
#     print("Handled error")

