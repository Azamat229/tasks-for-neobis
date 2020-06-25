##strs = list(input().split())
##
##maxx = max(len(w)for w in strs)
##
##
##for i in range(len(strs)):
##    if maxx == len(strs[i]):
##        print(strs[i])
##        print(maxx)
##        break
##
strs = list(input().split())
max_word = max(strs, key=len)
print(max_word)
print(len(max_word))
