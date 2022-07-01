n=int(input())
a=list(map(int,input().split()))
b=sorted(a)
b.reverse()
co=[]
ce=[]
for i in range(n):
    if i%2==0:
        ce.append(b[i])
    else:
        co.append(b[i])
k=[]
for i in range(len(co)):
    k.append(co[i])
    k.append(ce[i])
if len(co)!=len(ce):
    k.append(ce[-1])
for i in k:
    print(i,end=' ')
