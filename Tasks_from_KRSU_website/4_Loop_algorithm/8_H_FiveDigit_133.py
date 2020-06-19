Array = []
for i in range(10000, 99999+1):
    
    if i % 133 == 125 and i % 134 == 111:
        Array.append(i)
for j in Array:
    print(j,end=" ")
    
