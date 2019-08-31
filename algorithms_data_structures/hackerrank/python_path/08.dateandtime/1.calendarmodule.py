import calendar

# print out a 12 month calendar!
# print(calendar.TextCalendar(firstweekday=6).formatyear(2016))

d = {0: 'MONDAY', 1: 'TUESDAY', 2: 'WEDNESDAY', 3: 'THURSDAY',
     4: 'FRIDAY', 5: 'SATURDAY', 6: 'SUNDAY'}

date = list(map(int, input().split()))
print(d[calendar.weekday(date[2], date[0], date[1])])
