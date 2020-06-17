time = int(input())

hour = time // 3600
hour_rem = time - (3600 * hour)

minute = hour_rem // 60
minute_rem = hour_rem - 60 * minute

second = minute_rem
print(hour, minute, second)
