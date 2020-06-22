def rev(n):
    
    m = 0
    while n > 0:
        m = n % 10 + m * 10
        n //= 10
    return m

n = int(input())
print(rev(n))
