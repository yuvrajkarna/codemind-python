n=int(input())
m=list(map(int,input().split()))
k=int(input())
ma=max(m)
for i in range(n):
    if m[i]+k>=ma:
        print("True",end=" ")
    else:
        print("False",end=" ")