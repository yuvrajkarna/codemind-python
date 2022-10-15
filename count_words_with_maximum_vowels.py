a=input()
arr=list(a.split())
vow=list("aeiouAEIOU")
ma=0
for i in arr:
    c=0
    for j in i:
        if j in vow:
            c+=1
    if ma<c:
        ma=c
wc=0
for i in arr:
    c=0
    for j in i:
        if j in vow:
            c+=1
    if c==ma:
        wc+=1
print(wc)