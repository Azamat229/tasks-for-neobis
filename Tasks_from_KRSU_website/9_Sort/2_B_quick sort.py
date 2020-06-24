num = int(input())
Array = list(map(int, input().split()))
lenn = len(Array)

Array.sort()
sett = set(Array)
print(len(sett))
for i in range(len(Array)):
    if i+1 != lenn:
        print(Array[i], end=" ")
    else:
        print(Array[i], end="")
