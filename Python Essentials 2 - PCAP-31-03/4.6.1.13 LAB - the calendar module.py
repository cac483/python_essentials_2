from calendar import Calendar

class MyCalendar(Calendar):
    def __init__(self, firstweekday: int = 0) -> None:
        super().__init__(firstweekday)
    
    def count_weekday_in_year(self, year, weekday: int = 7):
        wd_count = 0
        if weekday < 7 and weekday >= 0:
            for m in range(12):
                month = m + 1
                for weeks in self.monthdays2calendar(year, month):
                    for days in weeks:
                        if days[1] == weekday and days[0] > 0:
                            wd_count += 1
            return wd_count
        else:
            raise ValueError

mycal = MyCalendar()
print(mycal.count_weekday_in_year(year=2000,weekday=6))