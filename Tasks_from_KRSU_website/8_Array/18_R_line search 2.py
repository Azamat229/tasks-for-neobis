num = int(input())
array = list(map(int, input().split()))
search = int(input())

for i in range(len(array)):
    if array[i] ==  search:
        print("YES")
        break
    elif i+1 == len(array) and array[i] != search:
        print("NO")
