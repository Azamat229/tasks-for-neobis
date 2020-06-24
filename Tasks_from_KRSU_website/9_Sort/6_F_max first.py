
n = int(input())
arr = list(map(int, input().split()))
m, pos = map(int, input().split())

arr.append(m)
j = len(arr) - 1
for i in range(pos - 1, len(arr)):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

for i in arr:
    print(i, end = " ")
