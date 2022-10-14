a=input()
p=a.split()
c=0
vow="`~!@#$%^&*()_+-={}|[]\:;<>?,./"
a=list(a)
x1=sorted(a)
l=len(a)
x=[]
for j in range(len(x1)):
    if x1[j]!=' ' and x1[j] not in vow:
        x.append(x1[j])
le=len(x)
k=0
for j in range(0,l):
    if a[j]!=' ' and k<le and a[j] not in vow:
        a[j]=x[k]
        k+=1
print("".join(a))
