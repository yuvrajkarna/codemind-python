n=int(input())
a=list(map(int,input().split()))
c=0
m=0
l=[]
for i in range(n):
    c=0
    for j in range(n):
        if(a[i]==a[j] and i!=j):
            c+=1
    if(c==0):
        l.append(a[i])
        m+=1
if(m!=0):
    print(max(l))
else:
    print("-1")