# -*- coding:cp1251 -*-
n = int(input())
ans = ""
mod = n % 10
if mod == 1 and n != 11:
    print(u"���", n, u"���.")
elif mod >= 2 and mod <= 4 and n != 12 and n != 14 and n != 13:
    print(u"���", n, u"����.")
else:
    print(u"���", n, u"���.")
