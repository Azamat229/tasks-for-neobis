a, b = map(int, input().split())
array = list(map(int, input().split()))
new_array = set()
lenn = len(array)
for i in range(lenn):
    new_array.add(array[i] % b)
print(len(new_array))
