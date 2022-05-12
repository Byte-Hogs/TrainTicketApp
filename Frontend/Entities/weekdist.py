class WeekDist():
    def __init__(self, monday = None, tuesday = None, wednesday = None, thursday = None, friday = None, saturday = None, sunday = None) -> None:
        self.__monday = monday
        self.__tuesday = tuesday
        self.__wednesday = wednesday
        self.__thursday = thursday
        self.__friday = friday
        self.__saturday = saturday
        self.__sunday = sunday
    
    def get(self, day:str):
        if day == 'monday':
            return self.__monday
        elif day == 'tuesday':
            return self.__tuesday
        elif day == 'wednesday':
            return self.__wednesday
        elif day == 'thursday':
            return self.__thursday
        elif day == 'friday':
            return self.__friday
        elif day == 'saturday':
            return self.__saturday
        elif day == 'sunday':
            return self.__sunday
        else:
            raise ValueError('day not recognized')
    
    def set(self, day:str, value):
        if day == 'monday':
            self.__monday = value
        elif day == 'tuesday':
            self.__tuesday = value
        elif day == 'wednesday':
            self.__wednesday = value
        elif day == 'thursday':
            self.__thursday = value
        elif day == 'friday':
            self.__friday = value
        elif day == 'saturday':
            self.__saturday = value
        elif day == 'sunday':
            self.__sunday = value
        else:
            raise ValueError('day not recognized')