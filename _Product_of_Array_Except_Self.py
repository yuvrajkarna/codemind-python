n=int(input())

l=list(map(int,input().split()))
m=1
for i in range(n):
    m=1
    for j in range(n):
        if(j!=i):
            m=m*l[j]
    print(m,end=" ")