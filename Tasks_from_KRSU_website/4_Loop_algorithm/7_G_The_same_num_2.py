numbers = list(map(int, input()))
commit = 0
for i in range(len(numbers)):
    commit = 0

    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            commit += 1
    if commit > 1:
        print("YES")
        break

if commit < 2:
    print("NO")
