
n = int(input())
aId = list()
aScore = list()
k = n
while k:
    a, b = map(int, input().split())
    aId.append(a)
    aScore.append(b)
    k-=1



for i in range (0, len(aScore)):
    m = i
    for j in range(i + 1, len(aId)):
        if aScore[j] > aScore[m]:
            m = j
        elif aScore[j] == aScore[m]:
            if aId[j] < aId[m]:
                m = j
    temp = aId[i]
    aId[i] = aId[m]
    aId[m] = temp
    
    temp = aScore[i]
    aScore[i] = aScore[m]
    aScore[m] = temp

for i in range(0, n):
    print(aId[i], aScore[i])
