n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    ma=-1
    for j in range(i+1,n):
        if(ma<l[j]):
            ma=l[j]
    print(ma,end=" ")