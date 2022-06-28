n=int(input())
li=list(map(int,input().split()))
c=0
ma=0
t=li[0]
for i in range(n):
    c=0
    for j in range(i,n):
        if(li[i]==li[j]):
            c+=1
        
    if(c>=ma):
        if ma==c:
            if t>li[i]:
                t=li[i]
        else:
            t=li[i]
        ma=c

print(t)