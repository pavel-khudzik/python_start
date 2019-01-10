import datetime

#datetime.date
#datetime.timedelta

dt = input().split() #2016 4 20
d = datetime.date(int(dt[0]), int(dt[1]), int(dt[2]))
d += datetime.timedelta(days=int(input())) #14
print(d.year, d.month, d.day)