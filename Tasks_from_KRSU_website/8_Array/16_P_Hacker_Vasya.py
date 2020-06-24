a, *b = map(int, input().split())
first = b[1-1]
last = b[-1]

for j in range(0, a):
    if b[j] > 3:
        b[j] = b[j] - 3



for i in range(len(b)):
    print(b[i], end=" ")

