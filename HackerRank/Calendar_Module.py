import calendar

# input: month day year
m, d, y = map(int, input().split())

# weekday: Monday=0 ... Sunday=6
day_index = calendar.weekday(y, m, d)

# convert to day name in CAPITAL
days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

print(days[day_index])
