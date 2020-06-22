## fale
def compute_gcd(x, y):

    while(y):
       x, y = y, x % y
    if x == 1:
        a = "YES"
    else:
        a = "NO"
    return a

num1, num2 = map(int,input().split())

print(compute_gcd(num1, num2))
