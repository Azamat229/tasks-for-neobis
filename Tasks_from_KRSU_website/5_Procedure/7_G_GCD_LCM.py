def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

num1, num2 = map(int,input().split())

print("GCD",compute_gcd(num1, num2))
print("LCM",compute_lcm(num1, num2))
