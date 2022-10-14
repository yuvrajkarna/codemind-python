def word(s):
    s1=""
    for i in s:
        s1+=i.lower()
    return s1
a=input()
b=input()
a1=list(a.split())
b1=list(b.split())
wa1=[]
for i in a1:
    if word(i) not in wa1:
        wa1.append(word(i))
wb1=[]
for i in b1:
    if word(i) not in wb1:
        wb1.append(word(i))
c=0
if len(wa1)>len(wb1):
    for i in wb1:
        if i in wa1:
            c+=1
elif len(wa1)<len(wb1):
    for i in wa1:
        if i in wb1:
            c+=1
else:
    for i in wa1:
        if i in wb1:
            c+=1
print(c)