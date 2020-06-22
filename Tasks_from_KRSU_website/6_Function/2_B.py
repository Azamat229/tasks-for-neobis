num = list(map(int, input()))
summ = 0
for i in range(len(num)):
    num.sort(reverse = True)
    summ += num[i]
    
print("{}+{}+{}={}".format(num[2],num[1],num,summ))
