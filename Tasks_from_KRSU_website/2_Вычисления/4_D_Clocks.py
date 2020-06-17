time = input().split()
hour = int(time[0]) * 3600
minute = int(time[1]) * 60
second = int(time[2]) * 1
total_on_sec = hour + minute + second
print(total_on_sec)
