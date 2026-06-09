s=input("enter a string")
fq={}
for i in s:
    if i in fq:
        fq[i]+=1
    else:
        fq[i]=1
print(fq)