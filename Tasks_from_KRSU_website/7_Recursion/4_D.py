def power(a, b, c):
    if b == c:
        print('1')
        return a ** b
    else:
        print("{}*".format(a), end = "")
    c += 1
    return power(a, b, c)


a, b = map(int, input().split())
print(power(a, b, 0))
