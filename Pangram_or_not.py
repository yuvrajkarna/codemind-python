a=input()
arr=list("abcdefghijklmnopqrstuvwxyz")
f=0
for i in arr:
    if i in a or i.upper() in a:
        f=1
    else:
        f=0
        break
if f==1:
    print("True")
else:
    print("False")