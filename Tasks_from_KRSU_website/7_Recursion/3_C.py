def toBase(n, b):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        return ""
    else:
        return toBase(n // b, b) + digits[n % b]

n, b = map(int, input().split())
print(toBase(n, b))

           