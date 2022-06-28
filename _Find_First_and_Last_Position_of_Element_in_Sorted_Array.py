n=int(input())
l=list(map(int,input().split()))
k=int(input())
f=0
for i in range(n):
    if(l[i]==k):
        print(i,end=" ")
        f=1
        break
f=0
for i in range(n-1,-1,-1):
    if(l[i]==k):
        print(i,end=" ")
        f=1
        break
if f==0:
    print("-1 " + "-1")
    