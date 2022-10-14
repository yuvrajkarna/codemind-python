a=input()
arr=list(a.split())
ss=ls=0
for i in range(len(arr)):
    mi=ma=arr[i][0]
    for j in arr[i]:
        if ord(j)>ord(ma):
            ma=j
        if ord(j)<ord(mi):
            mi=j
    ss+=ord(mi)
    ls+=ord(ma)
print(abs(ss-ls))
 