amount = int(input())

corners = list(map(int, input().split()))
summ = 0
zore = 0
fun = 180 * (amount - 2)

for i in corners:
    summ += i
    if i == 0:
        zore = 1
print(summ)
if zore > 0 or summ != fun:
    print("NO")
else:
    print("YES")

"""
"""
