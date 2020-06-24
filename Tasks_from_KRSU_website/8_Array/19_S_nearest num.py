##num = int(input())
##array = list(map(int, input().split()))
##search = int(input())
##start = array[0]
##stop = array[-1]
##
##for i in range(len(array)):
##    mid = int(len(array) / 2)
##    if mid > search:
##        stop = mid
##        start = start
##    else:
##        start = mid
##        stop = stop
##print(start, stop)
##
n = int(input())
arr = list(map(int, input().split()))
m = int(input())
min = 100000
minI = 0
c = 0
ar = list()
for i in range(0, len(arr)):
    ar.append(abs(arr[i] - m))
for i in range(0, len(ar)):
    if ar[i] < min:
        min = ar[i]
        minI = i

print(arr[minI])
