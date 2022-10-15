a=input()
f=f1=0
vow="aeiou"
for i in vow:
    if i in a:
        f=1
    else:
        f=0
        break
if f==1:
    print("True")
else:
    print("False")