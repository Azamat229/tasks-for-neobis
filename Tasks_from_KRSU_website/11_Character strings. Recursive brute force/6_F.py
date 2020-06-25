##str = list(map(str, input().split()))
##a, b = input().split()
##for i in range(len(str)):
##    if str[i] == a:
##        str[i] = b
##for j in range(len(str)):
##    print(str[j], end=' ')
##
str = input()
a, b = input().split()
new = str.replace(a,b)
print(new)
    
    
