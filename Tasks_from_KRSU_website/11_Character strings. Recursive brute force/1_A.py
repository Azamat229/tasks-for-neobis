strs = list(input())
new = []
for i in range(len(strs)):
    if strs[i] == "a":
        new.append("b")
    elif strs[i] == 'A':
        new.append('B')
    elif strs[i] == 'b':
        new.append('a')
    elif strs[i] == 'B':
        new.append('A')
    else:
        new.append(strs[i])
for j in range(len(strs)):
    print(new[j],end='')
