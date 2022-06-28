
n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    for j in range(n):
        if(l[i]>l[j]):
            c+=1
    print(c,end=" ")
    c=0
        