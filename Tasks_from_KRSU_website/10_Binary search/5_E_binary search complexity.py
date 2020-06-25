import math


n = int(input())


if (n == 1):
    print("0")
else:
    answer = math.log(n, 2) + 1
    tot_answer = int(answer)
    print(tot_answer)
