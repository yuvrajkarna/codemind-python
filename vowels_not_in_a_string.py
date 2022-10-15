a=input()
vow="aeiou"
c=0
for i in vow:
    if i not in a:
        print(i,end=" ")
        c+=1
if c==0:
    print(0)