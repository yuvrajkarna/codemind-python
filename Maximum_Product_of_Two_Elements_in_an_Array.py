li=list(map(int,input().split()))
l=len(li)
gre=0
mul=0
for i in range(l):
    mul=0
    for j in range(i+1,l):
        mul=(li[i]-1)*(li[j]-1)
        if(mul>gre):
            gre=mul
            
print(gre)