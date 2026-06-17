# f=open("data.txt","w")
# f.write("Hello world")
# f=open("data.txt","r")
# print(f.read())
# f=open("data.txt","a")
# f.write("\nthis is new update")
# f.close()
# f=open("data.txt","r")
# print(f.read())
# f.close()
# with open("data.txt","w") as f:
#     f.write("Hello world")
# with open("data.txt","r") as f:
#     print(f.read())
# with open("data.txt","a") as f:
#     f.write("\nthis is new update")
#     f.writelines(["\n1st line","\n2nd line","\n3rd line"])
# with open("data.txt","r") as f:
#     print(f.read())
#     print(f.tell())
#     f.seek(0)
#     print(f.readline())
#     print(f.readlines())
# import csv
# with open("data.csv","w",newline="") as f:
#     writer=csv.writer(f)
#     writer.writerow(["name","age","city"])
#     writer.writerow(["sriram","20","chennai"])
#     writer.writerow(["ram","21","bangalore"])
#     writer.writerow(["kumar","22","hyderabad"])
# with open("data.csv","r") as f:
#     print(f.read())

import json
data={"name":"sriram","age":20,"city":"chennai"}
with open("data.json","w") as f:
    json.dump(data,f)
with open("data.json","r") as f:
    data1=json.load(f)
print(data1)