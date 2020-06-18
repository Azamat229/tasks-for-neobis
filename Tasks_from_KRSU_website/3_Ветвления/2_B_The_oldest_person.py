a, b, c = map(int, input().split())


if a == b and b == c:
    print("Same age")
elif a >= b and a >= c:
    if a == b:
        print("Victor1")
    elif a == c:
        print("Boris")
    else:
        print("Anton")
elif b >= a and b >= c:
    if b == a:
        print("Victor2")
    elif b == c:
        print("Anton")
    else:
        print("Boris")
elif c >= b and c >= a:
    if c  == a:
        print("Boris")
    elif c == b:
        print("Anton")
    else:
        print("Victor3")

    # 3 2 2
    # 3 3 3
