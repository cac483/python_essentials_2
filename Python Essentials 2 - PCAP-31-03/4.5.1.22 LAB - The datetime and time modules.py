from datetime import timedelta
from datetime import date
from datetime import datetime

date1 = datetime(2020, 11, 4, 14, 53, 0)
print(date1.strftime('%Y/%m/%d %H:%M:%S'))
print(date1.strftime('%y/%B/%d %H:%M:%S %p'))
print(date1.strftime('%a, %Y %b %d'))
print(date1.strftime('%A, %Y %B %d'))
print(date1.strftime('Weekday: %w'))
print(date1.strftime('Day of the year: %j'))
print(date1.strftime('Week number of the year: %U'))