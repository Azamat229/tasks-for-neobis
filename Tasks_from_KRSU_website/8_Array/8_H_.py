num = int(input())
minn = []
for i in range(num):
    a, b = map(int, input().split())
    if a > b:
        minn.append(b)
    else:
        minn.append(a)
print(max(minn))
    
