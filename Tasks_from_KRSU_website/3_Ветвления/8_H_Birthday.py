d, m = map(int, input().split())

day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

ans = d + 4
i = 1
while i < m:
    if i == 4 or i == 6 or i == 9 or i == 11:
        ans += 30
    elif i == 2:
        ans += 29
    else:
        ans += 31
    i += 1

print(day[ans % 7 - 1])
