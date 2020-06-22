def xor(x, y):
    if x == y and x == 0:
        return 1
    else:
        return 0

n = int(input())
while n:
    x, y = map(int, input().split())
    print(xor(x, y))
    n -= 1
