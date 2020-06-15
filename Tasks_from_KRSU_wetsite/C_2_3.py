x1 = input()

x1 = list(str(x1))

for i in range(len(x1)):
    if i < len(x1) - 1:
        print(int(x1[i]), end=', ')
    else:
        print(int(x1[i]))

"""
input:
34567
output:
3, 4, 5, 6, 7
"""
