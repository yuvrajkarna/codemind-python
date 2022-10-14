a=list(input().split())
c=0
l=len(a)
vow="aeiouAEIOU"
for i in range(l):
    x1=[]
    x1=sorted(a[i])
    k=0
    c=0
    x=[]
    for j in range(len(x1)):
        if x1[j] not in vow:
            x.append(x1[j])
            k+=1
    le=len(x)
    p=[]
    p=list(a[i])
    k=0
    for j in range(0,len(p)):
        if  p[j] not in vow and k<le:
            if x[k ] not in vow:
                p[j]=x[k]
            k+=1
    p="".join(p)
    a[i]=p
print(" ".join(a))