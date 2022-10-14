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
    #if word(i) not in wa1:
        wa1.append(word(i))
wb1=[]
for i in b1:
    #if word(i) not in wb1:
        wb1.append(word(i))
array=[]
brray=[]
for i in a1:
    count=0
    for j in a1:
        if i==j:
            count+=1
    if count==1:
        array.append(i)
for i in b1:
    count=0
    for j in b1:
        if i==j:
            count+=1
    if count==1:
        brray.append(i)
        
c=0
if len(array)>len(brray):
    for i in brray:
        if i in array:
            c+=1
elif len(array)<len(brray):
    for i in array:
        if i in brray:
            c+=1
else:
    for i in array:
        if i in brray:
            c+=1
print(c)