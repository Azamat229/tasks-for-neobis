def gcd(x, y):

   while(y):
       x, y = y, x % y

   return x

def rat(m, n):
    print("{}/{}".format(m // gcd(m, n),n //gcd(m, n) ))


m, n = map(int, input().split())

rat(m, n)
