'''
first version of calendar classes for final project
'''

import pickle


class Calendar:
    '''
    Calendar class for storing whole calendar object in one place
    attributes:
    calendar name
    calendar description
    year = list of objects with class Year
    '''

    def __init__(self, calendarName='', calendarDescription='',years=[]):
        # initialize calendar object
        self.calendarName = calendarName
        self.years = years
        self.calendarDescription = calendarDescription
    
    def __str__(self):
        # string function for printing all years in calendar
        display = ''
        display += ('\n' + ('*' * 20) + '\n' + self.calendarName + '\n' + ('*' * 20) + '\n')
        for year in self.years:
            display += str(year)
        display += ('\n' + ('*' * 20) + '\n')
        return display
    
    def save(self, fileName):
        # save calendar object using pickle library
        with open(fileName, 'wb') as f:
            print('\n       Saving Calendar . . .\n')
            pickle.dump(self, f)
            print('\n   Calendar Saved!\n')

    def load(self, fileName):
        # load calendar object using pickle library
        with open(fileName, 'rb') as f:
            print('\n       Loading Calendar . . .\n')
            pickle.load(f)
            print('\n   Calendar Loaded!\n')


class Year(Calendar):
    '''
    Year class which inherits all methoda and functions of Calendar, 
    year class stores all the months in the year which hold calendar
    information for months
    attributes:
    yearNum = int
    is_leap_year = bool
    months = list of objects of class Month
    '''
    def __init__(self, yearNum=2023, is_leap_year=False, months=[]):
        # initialize Year object
        self.yearNum = yearNum
        self.is_leap_year = is_leap_year
        self.months = months
        self.eventCount = 0
        for month in months:
            self.eventCount += month.eventCount

    def __str__(self):
        # string method for printing out all events in a year
        display = ('\n' + ('*' * 20) + '\n')
        display += '\n*****\n' + str(self.yearNum) + '\n*****\n'
        for month in self.months:
            display += str(month)
        display += ('\n' + ('*' * 20) + '\n')
        return display

    def abbreviate(self):
        # abbreviate returns a string of an abreviated year calendar
        display = ('\n' + ('*' * 20) + '\n')
        display += (str(self.yearNum) + ' : ' + str(self.eventCount) + ' events')
        display += ('\n' + ('*' * 20) + '\n')
        return display 