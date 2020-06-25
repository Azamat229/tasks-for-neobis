def R(n, start, p):
    if n == 0:
        print(p[:-1])
    else:
        for j in range(start, n + 1):
            R(n - j, j, p + str(j) + '+')
 
R(int(input()), 1, '')
