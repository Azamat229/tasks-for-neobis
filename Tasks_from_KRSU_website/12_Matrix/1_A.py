a = []
n = int(input())
for i in range(n):
    a.append([int(i) for i in input().split()])
sum = 0
array_sum =0
for i in a:
    sum = 0
    for j in range(len(i)):
        sum += i[j]
    array_sum +=sum
for i in range(n):
    for j in range(n):
        tem = a[i][j]
        avg = array_sum//(n**2)
        if a[i][j] < avg:
            a[i][j] = 0
        else:
            a[i][j] = 225
        print(a[i][j], end = " ") if j != len(a[i]) - 1 else print(a[i][j])

