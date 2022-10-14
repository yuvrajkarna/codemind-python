a=input()
arr=list(a.split())
l=len(arr)
for i in range(l):
    if i==l-1:
        print(arr[i][0])
        break