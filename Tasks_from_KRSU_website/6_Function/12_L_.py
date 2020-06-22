def voting(a, b, c):
    if a == b or a == c:
        return a
    elif b == c or b == a:
        return b
    elif c == a or c == c:
        return c
    else:
        return a

n = int(input())

for i in range(n):
	a, b, c = map(int, input().split())
	print(voting(a, b, c))
