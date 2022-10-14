a,b=map(int,input().split())
arr=list(map(int,input().split()))
arr2=list(map(int,input().split()))
for i in range(a):
    for j in range(a):
        if i!=j:
            if arr[i]==arr[j] and arr[i]!=-1:
                arr[j]=-1
for i in arr:
    if i!=-1:
        if i in arr2:
            print(i,end=" ")