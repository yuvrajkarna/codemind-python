a=input()
c=co=0
for i in a:
    c=0
    if i==" ":
        continue
    else:
        for j in a:
            if i==j or i==j.upper() or i==j.lower():
                c+=1
        if c==1:
            co+=1
print(co)