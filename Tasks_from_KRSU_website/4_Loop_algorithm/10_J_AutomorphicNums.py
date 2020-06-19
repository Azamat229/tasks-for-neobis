N = int(input())
for i in range(1, N) :
    a = str(i**2)     
    if a[-len(str(i))] == str(i) :
        print("{}*{}={}".format(i,i, a) )
