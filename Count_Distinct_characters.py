a=input()
arr=[]
for i in a:
    if i.isspace():
        continue
    else:
        if i.upper() not in arr and i.lower() not in arr:
            arr.append(i)
print(len(arr))