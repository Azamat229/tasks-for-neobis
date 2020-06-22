## false
def fromBase(s):
    digits = "0123456789ABCDEF"
    r = 0
    for i in s:
        p = digits.find(i)
        r = 2 * r + p

    return r

def toBase(n):
    digits = "0123456789ABCDEF"
    r = ""
    while n != 0:
        r += digits[n % 2]
        n //= 2
    
    return ''.join(reversed(r))

x, y = map(str, input().split())
prod = fromBase(x) * fromBase(y)

print(toBase(prod))
