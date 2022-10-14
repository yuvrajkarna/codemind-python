a=input()
arr=list(a.split())
l=len(arr)
mi=arr[0][0]
ma=arr[l-1][0]
for i in arr[0]:
    if ord(i)<ord(mi):
        mi=i
for i in arr[l-1]:
    if ord(i)>ord(ma):
        ma=i
print(mi,ma)