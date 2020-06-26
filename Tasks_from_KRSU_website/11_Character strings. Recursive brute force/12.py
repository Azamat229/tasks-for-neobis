num = int(input())
abc = num
new = []

while(num):
    a = input()
    new.append(a[3:])
    
    num-=1
new.sort()
b = ", "
print(b.join(new))

##for i in range(abc):
##    if i+1 == len(new):
##        print(new[i], end=' ')
##    else:
##        print(new[i], end=", ")
##
