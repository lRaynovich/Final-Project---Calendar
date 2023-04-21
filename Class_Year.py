'''
This module stores the year class which stores 
all the information for a year object 
'''

#import needed modules
import Class_Month as M

class Year:
    '''
    Class year for storing months for events in calendar
    Attributes:
        year : int
        months : list of Month objects
        eventcount : int
    Methods:
        __init__ : initializes class
        __str__ : returns string of year
        Abbreviate : returns abbreviated string of year
        Add_month : adds a Month object to the year
        '''
    def __init__(self,year=2023,months=[]):
        # initializes class
        self.year = year
        self.months = months
        self.eventCount = 0
        for month in self.months:
            self.eventCount += month.eventCount

    def __str__(self):
        # returns string of year
        display = ('\n' + ('*' * 20) + '\n')
        display += '\n*****\n' + str(self.months[0].days[0].date.year) + '\n*****\n'
        for month in self.months:
            display += str(month.Abbreviate())
        display += ('\n' + ('*' * 20) + '\n')
        return display
    
    def Abbreviate(self):
        # returns abbreviated string of year
        display = ('\n***************\n')
        display += (str(self.months[0].days[0].date.year) + ' : ' + str(self.eventCount) + ' events')
        display += ('\n***************\n')
        return display
    
    def Add_Month(self,month=M.Month):
        # adds month object to year
        self.months.append(month)