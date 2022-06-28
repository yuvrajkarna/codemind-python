n=int(input())
l=list(map(int,input().split()))
f=0
for i in range(n):
    c=0
    for j in range(n):
        if( l[i]==l[j]):
            c+=1

    if c==1:
        print(l[i],end=" ")
        f=1
if f==0:
    print("-1")