def convert(a1, b1):
    aa = int(a1, 2)
    bb = int(b1, 8)
    summ = aa + bb
    return int(summ)

a, b = map(str, input().split())
print(convert(a, b))
