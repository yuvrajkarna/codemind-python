n=input()
p=0
z=0
for i in range(len(n)):
    c=0
    for j in range(len(n)):
        if(n[i]==n[j]and i!=j):
            c+=1
    if(c==0):
        p=i
        z+=1
        break
if(z==0):
    print("-1")
else:
    print(p)