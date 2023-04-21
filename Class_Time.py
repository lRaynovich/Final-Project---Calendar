'''

'''

class Time:
    def __init__(self,hours=1,minutes=0):
        self.hours = hours
        self.minutes = minutes
        # confine hours from 0-23 for 24 hour format
        if self.hours < 0:
            self.hours = 0
        elif self.hours > 23:
            self.hours = 23
        # confine minutes to 0-59
        if self.minutes < 0:
            self.minutes = 0
        elif self.minutes > 59:
            self.minutes = 59

    def __str__(self):
        hourholder = self.hours
        minuteholder = self.minutes
        amholder = True
         
        if hourholder < 12:
            amholder = True
            if hourholder ==0:
                hourholder = 12
        # change pm hours to 12 hour format
        elif hourholder >= 12:
            amholder = False
            if hourholder > 12:
                hourholder -= 12
        if amholder:
            return str(hourholder) + ':' + str(minuteholder) + ' AM'
        else:
            return str(hourholder) + ':' + str(minuteholder) + ' PM'
        
    def __le__(self,other):
        if self.hours < other.hours:
            return True
        elif self.hours > other.hours:
            return False
        else:
            if self.minutes < other.minutes:
                return True
            elif self.minutes > other.minutes:
                return False
            else:
                True

    def __le__(self,other):
        if self.hours < other.hours:
            return True
        elif self.hours > other.hours:
            return False
        else:
            if self.minutes < other.minutes:
                return True
            elif self.minutes > other.minutes:
                return False
            else:
                False

    def __ge__(self,other):
        if self.hours > other.hours:
            return True
        elif self.hours < other.hours:
            return False
        else:
            if self.minutes > other.minutes:
                return True
            elif self.minutes < other.minutes:
                return False
            else:
                True

    def __ge__(self,other):
        if self.hours > other.hours:
            return True
        elif self.hours < other.hours:
            return False
        else:
            if self.minutes > other.minutes:
                return True
            elif self.minutes < other.minutes:
                return False
            else:
                False


        
    def Add_Time(self,minutes=0,hours=0):
        if minutes < 0:
            minutes = 0
        if hours < 0:
            hours = 0
        hours = hours + (minutes // 60)
        adddays = hours // 24
        addhours = hours % 24
        addminutes = minutes % 60
        finalhours = self.hours + addhours
        finalminutes = self.minutes + addminutes
        if (finalminutes // 60) == 1:
            finalhours += 1
        if finalhours > 23:
            adddays += 1
            return adddays, addhours, addminutes
        else:
            return adddays, addhours, addminutes