'''

'''

import Class_Day as D

class Month:
    def __init__(self,monthnum=1,days=[],year=2023):
        self.monthnum = monthnum
        self.days = days
        self.year = year
        self.eventCount = 0
        for day in self.days:
            self.eventCount += day.eventCount

    def __str__(self):
        display = ('\n**********\n' + self.days[0].date.monthstr + '\n**********\n')
        for day in self.days:
            display += '\n' + str(day.Abbreviate())
        display += ('\n**********\n')
        return display

    def Abbreviate(self):
        display = ('\n***************\n')
        display += (self.days[0].date.monthstr + ' : ' + str(self.eventCount) + ' events')
        display += ('\n***************\n')
        return display
    
    def Add_Day(self,day=D.Day):
        self.days.append(day)