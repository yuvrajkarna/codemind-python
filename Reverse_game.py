def palin(n):
    t=n
    r=0
    s=0
    while n:
        r=n%10
        s=s*10+r
        n//=10
    
    return s
   
n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    print(palin(l[i]),end=" ")