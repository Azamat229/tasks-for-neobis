def gcd(m, n):
    if m <= 0 or n <= 0:
        return m + n
    if m > n:
        m -= n
        print("GCD({},{})".format(n, m))
        return gcd(m, n)
    else:
        n -= m
        print("GCD({},{})".format(n ,m))
        return gcd(m, n)


m, n = map(int, input().split())
print("GCD({},{})={}".format(m, n, gcd(m, n)))