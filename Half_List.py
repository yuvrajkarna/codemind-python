n=int(input())
li=list(map(int,input().split()))

for i in range(n-1,(n//2)-1,-1):
    print(li[i],end=" ")
for i in range((n//2)):
    print(li[i],end=" ")
    