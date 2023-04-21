'''
This module stores the month class which stores 
all the information for a month object
'''

#import needed modules
import Class_Day as D

class Month:
    '''
    Class for storing days in a month for events in a calendar
    Attributes:
        monthnum : int
        days : list of Day objects
        year : int
        eventcount : int
    Methods:
        __int__ : intialize class
        __str__ : return string of day
        Abbreviate : return abbreviated string of month
        Add_day(arg1) : add day object, arg1,  to days 
    '''
    def __init__(self,monthnum=1,days=[],year=2023):
        # initialize
        self.monthnum = monthnum
        self.days = days
        self.year = year
        self.eventCount = 0
        for day in self.days:
            self.eventCount += day.eventCount

    def __str__(self):
        # return string of month
        display = ('\n**********\n' + self.days[0].date.monthstr + '\n**********\n')
        for day in self.days:
            display += '\n' + str(day.Abbreviate())
        display += ('\n**********\n')
        return display

    def Abbreviate(self):
        # return abreviated string of month
        display = ('\n***************\n')
        display += (self.days[0].date.monthstr + ' : ' + str(self.eventCount) + ' events')
        display += ('\n***************\n')
        return display
    
    def Add_Day(self,day=D.Day):
        # add day to days
        self.days.append(day)