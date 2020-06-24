num = int(input())
Array = list(map(int, input().split()))
lenn = len(Array)
mid = int(lenn / 2)

array_1 = []
array_2 = []
for i in range(lenn):
    if i+1 <= mid:
        array_1.append(Array[i])
    elif i+1 > mid:
        array_2.append(Array[i])
array_2.sort(reverse = True)
array_1.sort()
c = array_1 + array_2
for j in range(lenn):
    if j+1 != lenn:
        print("{} ".format(c[j]), end='')
    else:
        print("{}".format(c[j]), end='')


