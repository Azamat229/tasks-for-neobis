num = int(input())
array = list(map(int, input().split()))
search = int(input())
count = 0

for i in array:
    if i == search:
        count += 1
print(count)
