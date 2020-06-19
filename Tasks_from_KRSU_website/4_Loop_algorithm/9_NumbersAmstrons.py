def arm(num):
    num_sum = 0
    n = len(str(num))
    while num:
        num_sum += (num%10)**n
        num //= 10
    return num_sum
 
for num in range(100,999):
    if num == arm(num):
        print(num)
