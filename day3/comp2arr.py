a=["a","b","c"]
b=["a","b","c"]
if len(a)!=len(b):
    print("arrays are not of same length")
else:
    equal=True
    for i in range(len(a)):
        if a[i]!=b[i]:
            equal=False
            break
    if equal:
        print("arrays are equal")
    else:
        print("arrays are not equal")