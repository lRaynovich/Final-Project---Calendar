'''
first version of calendar classes for final project
'''

import pickle
import datetime


class Calendar:
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
    
class Event:
    def __init__(self, eventName='', eventDescription='', allDay=False, recurring=False, date=datetime.date(1,1,1)):
        self.eventName = eventName
        self.eventDescription = eventDescription
        self.allDay = allDay
        self.recurring = recurring
        self.date = date

    def __str__(self):
        display = '\n'
        display += '\t- ' + self.eventName + '-\n' + self.eventDescription 
        display += '\nRecurring : ' 
        if self.recurring:
            display += 'yes'
        else:
            display += 'no'
        display += '\nAll Day : '
        if self.allDay:
            display += 'yes'
        else:
            display += 'no'
        display += '\n-----------'
        return display
    
    def user_define(self):
        self.eventName = input("Event Name: ")
        self.eventDescription = input("Event Description: ")
        dateyear = int(input('Enter date year: '))
        datemonth = int(input('Enter date month: '))
        dateday = int(input('Enter date day: '))
        self.date = datetime.date(dateyear, datemonth, dateday)
        ad = input("Is the event all day(enter 'yes' or 'no'): ")
        if ad == 'yes':
            self.allDay = True
        elif ad == 'no':
            self.allDay = False
        rec = input("Is the event all day(enter 'yes' or 'no'): ")
        if rec == 'yes':
            self.recurring = True
        elif rec == 'no':
            self.recurring = False





def fill_year(yearnum= Year):
    for i in range(1,13):
        yearnum.months.append(Month(i))
    for x in yearnum.months:
        if x.monthNum == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            for j in range(1,32):
                x.days.append(Day(j))
        elif x.monthNum == 4 or 6 or 9 or 11:
            for j in range(1,31):
                x.days.append(Day(j))
        elif x.monthNum == 2:
            for j in range(1,29):
                x.days.append(Day(j))
        else:
            pass