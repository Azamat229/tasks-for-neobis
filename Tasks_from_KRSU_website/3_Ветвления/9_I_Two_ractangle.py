import math
x1, y1, x2, y2, x3, y3 = map(int, input().split())

ab = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
bc = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
ac = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)

x1, y1, x2, y2, x3, y3 = map(int, input().split())

ab1 = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
bc1 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
ac1 = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)

if ab == ab1 :
    if bc == bc1 and ac == ac1:
        if math.sqrt(ab ** 2 + bc ** 2) == ac or math.sqrt(bc ** 2 + ac ** 2) == ab or math.sqrt(ab ** 2 + ac ** 2) == bc:
            print("YES")
        else:
            print("NO")
    elif bc == ac1 and ac == bc1:
        if math.sqrt(ab ** 2 + bc ** 2) == ac or math.sqrt(bc ** 2 + ac ** 2) == ab or math.sqrt(ab ** 2 + ac ** 2) == bc:
                print("YES")
        else:
                print("NO")
    else: print("NO")
elif ab == bc1 :
    if bc == ac1 and ca == ab1:
        if math.sqrt(ab ** 2 + bc ** 2) == ac or math.sqrt(bc ** 2 + ac ** 2) == ab or math.sqrt(ab ** 2 + ac ** 2) == bc:
                print("YES")
        else:
                print("NO")
    elif bc == ab1 and ac == ac1:
        if math.sqrt(ab ** 2 + bc ** 2) == ac or math.sqrt(bc ** 2 + ac ** 2) == ab or math.sqrt(ab ** 2 + ac ** 2) == bc:
                print("YES")
        else:
                print("NO")
    else:
            print("NO")
elif ab == ac1 :
    if bc == ab1 and ac == bc1:
        if math.sqrt(ab ** 2 + bc ** 2) == ac or math.sqrt(bc ** 2 + ac ** 2) == ab or math.sqrt(ab ** 2 + ac ** 2) == bc:
                print("YES")
        else:
                print("NO")
    elif bc == bc1 and ac == ab1:
        if math.sqrt(ab ** 2 + bc ** 2) == ac or math.sqrt(bc ** 2 + ac ** 2) == ab or math.sqrt(ab ** 2 + ac ** 2) == bc:
                print("YES")
        else:
                print("NO")
    else: print("NO")
else: print("NO")



# from math import sqrt
#
# x1, y1, x2, y2, x3, y3 = map(int, input().split())
#
# ab = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
# bc = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
# ac = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
#
# x1, y1, x2, y2, x3, y3 = map(int, input().split())
#
# ab1 = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
# bc1 = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
# ac1 = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
#
# max1 = max(ab, bc, ac)
# max2 = max(ab1, bc1, ac1)
#
# if max2 == max1:
#     print("YES")
# else:
#     print("NO")
#
# # 0 0 10 0 0 12
# # 10 10 22 10 10 20
