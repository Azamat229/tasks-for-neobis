num = int(input())

for i in range(num):
    a, b = map(int, input().split())
    if bool(a) != bool(b):
        print(1)
    else:
        print(0)
