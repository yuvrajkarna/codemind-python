storage=set(input().split())
N=int(input())
output=True
for i in range(N):
    storage2=set(input().split())
    if not storage2.issubset(storage):
        output=False
print(output)