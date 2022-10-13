a=input()
c=wc=0
l=len(a)
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if i!=j:
            if a[i]==a[j]:
                c+=1
    if c==0:
        wc+=1
    else:
        wc=0
        break
if wc==0:
    print("False")
else:
    if wc==l:
        print("True")
    else:
        print("False")