txt = input().split()
len_of_array = len(txt)
space = ' '
others_items_len = 0
for i in range(len_of_array):
    if i == 0:
        print(txt[0])
    else:
        others_items_len += len(txt[i-1])
        total_space = (others_items_len) * space
        print(total_space+txt[i])
