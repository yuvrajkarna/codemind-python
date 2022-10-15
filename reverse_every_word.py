def rev(s):
    l=len(s)
    s1=""
    for i in range(l-1,-1,-1):
        s1+=s[i]
    return s1
a=input()
arr=list(a.split())
for i in arr:
    print(rev(i),end=" ")
