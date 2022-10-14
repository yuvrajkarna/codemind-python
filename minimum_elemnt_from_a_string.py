a=input()
arr=list(a.split())
mi=arr[len(arr)-1][0]
for i in arr[len(arr)-1]:
    if ord(i)<ord(mi):
        mi=i
if mi.lower() in arr[len(arr)-1]:
    print(mi.lower())
else:
    print(mi)
