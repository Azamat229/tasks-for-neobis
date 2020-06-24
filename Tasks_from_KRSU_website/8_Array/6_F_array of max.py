num = int(input())
Array = list(map(int, input().split()))
maxx = max(Array)
count = 0
for i in range(len(Array)):
    if Array[i] == maxx:
        count += 1

print("{} {}".format(maxx, count))
