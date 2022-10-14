a=input()
c=0
l=len(a)
vow="aeiouAEIOU"
mid=len(a)//2
for i in range(mid):
    if a[i].isspace() or a[l-i-1].isspace():
        continue
    if a[i] in vow and a[l-i-1] not in vow:
        c+=1
    if a[i] not in vow and a[l-i-1] in vow:
        c+=1
print(c)

