def some(s):
    sm=0
    for i in s:
        sm+=ord(i)
    return sm
a=input()
arr=list(a.split())
for i in range(len(arr)):
    for j in range(len(arr)-1):
        if len(arr[j])>len(arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
        if len(arr[j])==len(arr[j+1]):
            if some(arr[j])>some(arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
for i in arr:
    print(i,end=" ")