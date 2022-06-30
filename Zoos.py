a=b=0
for i in input():
    if i=='z':
        a+=1
    elif i=='o':
        b+=1
if a*2==b:
    print("Yes")
else:
    print("No")