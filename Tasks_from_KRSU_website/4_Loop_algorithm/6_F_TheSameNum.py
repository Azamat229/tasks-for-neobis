numbers = list(map(int, input()))
commit = 0
for i in range(len(numbers)):
    if numbers[i] == numbers[i-1]:
        print("YES")
        commit += 1
        break
if commit < 1:
    print("NO")
