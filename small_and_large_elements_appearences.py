a=input()
mi=ma=a[0]
for i in a:
    if i.isupper() or i.islower():
        if ord(mi)>ord(i):
            mi=i
        if ord(ma)<ord(i):
            ma=i
mic=mac=0
for i in a:
    if i.isupper() or i.islower():
        if i==mi:
            mic+=1
        if i==ma:
            mac+=1
print(mi,mic,ma,mac)
