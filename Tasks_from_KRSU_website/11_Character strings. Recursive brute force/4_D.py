words = list(map(str, input().split()))

last = words[0]
name = words[1]
mid = words[2]

print("{}.{}. {}".format(name[0], mid[0], last))



##for i in range(len(words)):
##    if words[i][-1] == 'v':
##        last = words[i]
##    if words[i][-1] == 'h':
##        mid = words[i].upper()
##    else:
##        name = words[i].upper()
##
##print("{}.{}. {} ".format(name[0], mid[0], last))

