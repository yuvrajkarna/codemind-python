a=input()
arr=[]
for i in a:
    if i.isspace():
        continue
    else:
        if i.lower() not in arr:
            arr.append(i.lower())
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
for i in arr:
    print(i,end="")