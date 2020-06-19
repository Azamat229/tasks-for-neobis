a, b = map(int, input().split())
summ = 0
for i in range(0, abs(a)):
    summ += abs(b)

if a < 0 and b < 0:
    print("({})*({})={}".format(a, b, summ))
elif a < 0 or b < 0:
    summ = -summ
    if a < 0 : print("({})*{}={}".format(a, b, summ))
    else : print("{}*({})={}".format(a, b, summ))
else:
    print("{}*{}={}".format(a, b, summ))
