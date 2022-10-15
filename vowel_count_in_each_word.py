a=input()
arr=list(a.split())
vow=list("aeiouAEIOU")
for i in arr:
    c=0
    for j in i:
        if j in vow:
            c+=1
    print(c,end=" ")