words = list(map(str, input().split()))


 
for i in range(len(words)):
    if words[i][-1] == 'v':
        last = words[i]
    if words[i][-1] == 'h':
        mid = words[i].upper()
    else:
        name = words[i].upper()

print("{}.{}. {} ".format(name[0], mid[0], last))
