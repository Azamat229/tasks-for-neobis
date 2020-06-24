num = int(input())
array = []
for i in range(num):
    a = int(input())
    array.append(a)
    array.sort()
for j in range(num):
    print(array[j])
