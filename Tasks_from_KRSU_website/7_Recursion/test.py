def summ(a, lenn):
    if lenn == 0:
        summm = 0
        print(a[lenn])
        for i in range(len(a)):
            summm = summm + int(a[i])
        return summm
    elif lenn > 0:
        print("{}+".format(a[lenn]),end = "")
    lenn -= 1
    return summ(a, lenn)

a = str(input())
lenn = len(a)-1

print(summ(a, lenn))



