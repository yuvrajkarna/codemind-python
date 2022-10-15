def rev(s):
    s1=""
    l=len(s)
    for i in range(l-1,-1,-1):
        s1+=s[i]
    return s1
a=input()
arr=list(a.split())
for i in range(len(arr)):
    if i%2==0:
        print(rev(arr[i]),end=" ")
    else:
        print(arr[i],end=" ")