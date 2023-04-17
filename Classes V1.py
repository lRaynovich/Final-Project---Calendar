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
    eventcount = int
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
    
class Month(Year):
    '''
    Month class that inherits all attributes and methods from Year class
    used to store all days in each month
    attributes
    monthnum = int
    days = list of objects of class day
    monthString = string
    monthStringAbr = string
    eventcount = int
    '''
    def __init__(self, monthNum = int, days=[]):
        # initailize attributes
        self.monthNum = monthNum
        if monthNum == 1:
            self.monthString = 'January'
            self.monthStringAbr = 'Jan'
        elif monthNum == 2:
            self.monthString = 'February'
            self.monthStringAbr = 'Feb'
        elif monthNum == 3:
            self.monthString = 'March'
            self.monthStringAbr = 'Mar'
        elif monthNum == 4:
            self.monthString = 'April'
            self.monthStringAbr = 'Apr'
        elif monthNum == 5:
            self.monthString = 'May'
            self.monthStringAbr = 'May'
        elif monthNum == 6:
            self.monthString = 'June'
            self.monthStringAbr = 'Jun'
        elif monthNum == 7:
            self.monthString = 'July'
            self.monthStringAbr = 'Jul'
        elif monthNum == 8:
            self.monthString = 'August'
            self.monthStringAbr = 'Aug'
        elif monthNum == 9:
            self.monthString = 'September'
            self.monthStringAbr = 'Sep'
        elif monthNum == 10:
            self.monthString = 'October'
            self.monthStringAbr = 'Oct'
        elif monthNum == 11:
            self.monthString = 'November'
            self.monthStringAbr = 'Nov'
        elif monthNum == 12:
            self.monthString = 'December'
            self.monthStringAbr = 'Dec'
        else:
            self.monthString = ''
            self.monthStringAbr = ''
        self.days = days
        self.eventCount = 0
        for day in self.days:
            self.eventCount += day.eventCount
        
    def __str__(self):
        # returns sting for printing calendar elements
        display = ('\n**********\n' + str(self.monthString) + '\n**********\n')
        for day in self.days:
            display += str(day)
        display += ('\n**********\n')
        
    def abbreviate(self):
        # abbreviates month elements
        display = ('\n**********\n')
        display += (str(self.monthStringAbr) + ' : ' + str(self.eventCount) + ' events')
        display += ('\n**********\n')
        return display
    
class Day(Month):
    '''
    Class for all calendar events in a day that inherits all attributes and
    methods of class month 
    attributes
    daynum = int
    events = list of objects of class Event
    daynumstr = string
    '''
    def __init__(self, dayNum=1, events = []):
        # initialize class elements
        self.dayNum =dayNum
        self.events = events
        self.dayNumStr = ''
        if self.dayNum == (1 or 21 or 31):
            self.dayNumStr = 'st'
        elif self.dayNum == (2 or 22):
            self.dayNumStr = 'nd'
        elif self.dayNum == (3 or 23):
            self.dayNumStr = 'rd'
        else:
            self.dayNumStr = 'th'
        self.eventCount = 0
        for event in self.events:
            self.eventCount += 1

    def __str__(self):
        # returns string for all events in day
        display = '-- ' + str(self.dayNum) + str(self.dayNumStr) + ' --'
        for event in self.events:
            display += str(event)
        display += '----------'
        return display
        
    def abbreviate(self):
        # returns abbreviated string of events in day
        display = ('-- ' + str(self.dayNum) + str(self.dayNumStr) + ' : ' + str(self.eventCount) + ' events --')
        return display