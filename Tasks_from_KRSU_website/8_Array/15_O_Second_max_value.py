num = int(input())
array = list(set(map(int, input().split())))

num_index = 0
num_max = 0
num_max_second = 0

for i in range(len(array)):
    if num_max < array[i]:
        num_max = array[i]
        num_index = i
for j in range(len(array)):
    if num_index != j:
        if num_max_second < array[j]:
            num_max_second = array[j]
print(num_max_second)
        
    
