def palin(n):
    t=n
    r=0
    s=0
    while n:
        r=n%10
        s=s*10+r
        n//=10
    if t==s:
        return 1
    else:
        return 0
        
n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    if(palin(l[i])):
        c+=1
print(c)