n=int(input())
l=list(map(int,input().split()))
su=0
t=0
for i in range(n):
    c=0
    for j in range(i+1,n):
        if l[i]==l[j]:
            c+=1
    t= c%2
    su+=t
print(su)