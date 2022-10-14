a=input()
arr=list(a.split())
for i in range(len(arr)):
    mi=ma=arr[i][0]
    for j in arr[i]:
        if ord(j)<ord(mi):
            mi=j
        if ord(j)>ord(ma):
            ma=j
    print(abs(ord(mi)-ord(ma)),end=" ")