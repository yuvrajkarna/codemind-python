n=int(input())
l=list(map(int,input().split()))
k=int(input())
ma=max(l)
for i in range(n):
    if l[i]+k>=ma:
        print("True",end=" ")
    else:
        print("False",end=" ")