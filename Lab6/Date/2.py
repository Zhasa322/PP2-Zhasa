import datetime

x=datetime.datetime.now()
print("Yesterday: ", x.year, x.month, x.day-1)
print("Today: ", x.year, x.month, x.day)
print("Tomorrow: ", x.year, x.month, x.day+1)