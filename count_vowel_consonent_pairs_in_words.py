a=input()
arr=list(a.split())
c=0
vow="aeiouAEIOU"
for i in arr:
    l=len(i)
    mid=l//2
    for j in range(mid-1,-1,-1):
        if i[j] in vow and i[l-j-1] not in vow:
            c+=1
        if i[j] not in vow and i[l-j-1] in vow:
            c+=1
print(c)
