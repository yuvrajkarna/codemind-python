a,b=map(int,input().split())
arr=list(map(int,input().split()))
arr2=list(map(int,input().split()))
c=0
for i in range(a):
    for j in range(a):
        if i!=j:
            if arr[i]==arr[j] and arr[i]!=-1:
                arr[j]=-1
for i in range(b):
    for j in range(b):
        if i!=j:
            if arr2[i]==arr2[j] and arr2[i]!=-1:
                arr2[j]=-1
for i in arr:
    if i!=-1:
        if i not in arr2:
            c+=1
for i in arr2:
    if i!=-1:
        if i not in arr:
            c+=1
print(c)