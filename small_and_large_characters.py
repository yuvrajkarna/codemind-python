a=input()
arr=list(a.split())
for i in arr:
    mi=ma=i[0]
    for j in i:
        if ord(j)>ord(ma):
            ma=j
        if ord(j)<ord(mi):
            mi=j
    print(mi,ma,end=" ")