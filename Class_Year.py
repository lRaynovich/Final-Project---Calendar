'''

'''

import Class_Month as M

class Year:
    def __init__(self,year=2023,months=[]):
        self.year = year
        self.months = months
        self.eventCount = 0
        for month in self.months:
            self.eventCount += month.eventCount

    def __str__(self):
        display = ('\n' + ('*' * 20) + '\n')
        display += '\n*****\n' + str(self.months[0].days[0].date.year) + '\n*****\n'
        for month in self.months:
            display += str(month.Abbreviate())
        display += ('\n' + ('*' * 20) + '\n')
        return display
    
    def Abbreviate(self):
        display = ('\n***************\n')
        display += (str(self.months[0].days[0].date.year) + ' : ' + str(self.eventCount) + ' events')
        display += ('\n***************\n')
        return display
    
    def Add_Month(self,month=M.Month):
        self.months.append(month)