import math

depth = float(input())
pi = math.pi
v = 1 / 6 * pi * (depth ** 3)
# print(round(v, 3))
print("%.3f" % v)
