words = list(map(str, input().split(".")))
change = input()
if len(words) > 2:
    words[-1] = change
    for i in range(len(words)):
        if i+1 == len(words):
            print(words[i])
        else:
            print(words[i],end=".")
else:
    print("{}.{}".format(words[0], change))
