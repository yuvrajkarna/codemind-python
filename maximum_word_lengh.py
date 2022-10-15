a=input()
arr=list(a.split())
ma=0
for i in arr:
    c=0
    for j in i:
        c+=1
    if c>ma:
        ma=c
print(ma)