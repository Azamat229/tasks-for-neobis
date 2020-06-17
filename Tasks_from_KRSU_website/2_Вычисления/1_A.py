a, b, c = map(int, input().split())

print("{}+{}+{}={}".format(a, b, c, a + b + c))

print("{}*{}*{}={}".format(a, b, c, a * b * c))

average = (a + b + c) / 3

if int(a / 100) == 0 and int(a / 10) == 0:

    if int(average) == average:
        print("({}+{}+{})/3={}".format(a, b, c, int(average)))
    else:
        print("({}+{}+{})/3={}".format(a, b, c, round(average, 5)))

else:
    if int(average) == average:
        print("({}+{}+{})/3={}".format(a, b, c, int(average)))
    else:
        print("({}+{}+{})/3={}".format(a, b, c, round(average, 4)))
