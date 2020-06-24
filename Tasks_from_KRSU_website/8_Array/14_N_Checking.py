Array = []
a = int(input())
if (a >= 2) and (a <= 1000):
    Arra = [int(i) for i in input().split()]

    Array = list(map(abs, Arra))
    ar = max(Array)
    if (ar <= 2000000000) and (len(Array) >= 2):
        small = Array[0]
        small2 = 0
        c = 0
        for i in range(len(Array)):
            if Array[i] < small:
                small = Array[i]
                c = c + 1


def second_smaller(arr):
    m1, m2 = float('inf'), float('inf')
    for x in Array:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2


print(small, second_smaller(Array))