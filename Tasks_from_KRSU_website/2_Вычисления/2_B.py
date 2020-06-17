from math import sqrt

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

length = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
print(round(length, 3))

"""
input:
5.5 3.5
1.5 2
output:
4.272

"""
