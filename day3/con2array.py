a=["a","b","c","d","e"]
b=["f","g","h","i","j"]
res=[None]*(len(a)+len(b))
for i in range(len(a)):
    res[i]=a[i]
for i in range(len(b)):
    res[i+len(a)]=[b[i]]
print(res)
