n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))
if n < m: arr = arr1
else: arr = arr2
if n > m: arrm = arr1
else: arrm = arr2

count = 0
for i in range (0, len(arr1)):
    if arr[i] in arrm:
        count += 1
print(count)
print("YES") if count == len(arr) else print("NO")
