class WeekDayError(Exception):
    pass
	

class Weeker:
    valid_days = {
        "Mon":0,
        "Tue":1,
        "Wed":2,
        "Thu":3,
        "Fri":4,
        "Sat":5,
        "Sun":6
    }

    def __init__(self, day):
        if day in Weeker.valid_days.keys():
            self.__day = day
            self.__dayval = Weeker.valid_days[day]
        else:
            raise WeekDayError

    def __str__(self):
        return self.__day

    def add_days(self, n):
        if isinstance(n, int):
            self.__dayval = (self.__dayval + (n % 7)) % 7
            for day in Weeker.valid_days:
                if Weeker.valid_days[day] == self.__dayval:
                    self.__day = day
        else:
            raise WeekDayError


    def subtract_days(self, n):
        if isinstance(n, int):
            if self.__dayval < (n % 7):
                self.__dayval = (self.__dayval + 7 - (n % 7))
            else:
                self.__dayval = self.__dayval - (n % 7)

            for day in Weeker.valid_days:
                if Weeker.valid_days[day] == self.__dayval:
                    self.__day = day
        else:
            raise WeekDayError


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
