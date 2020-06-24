num = int(input())
Array = list(map(int, input().split()))
New_array = []
for i in range(len(Array), 0 , -1):
   
    New_array.append(Array[i-1])
for j in range(len(New_array)):
    print(New_array[j], end=' ')
