'''
This module stores the event class which is used for storing 
information for user generated events
'''

# import necessary module
import Class_Date as D
import Class_Day as DA
import Class_Time as T
import Class_Month as M
import Class_Year as Y
import Class_EventTiming as ET


class Event:
    '''
    Class Event for storing event information
    Attributes:
        eventname : string
        eventdescription : string
        eventtiming : EventTiming object
    Methods:
        __init__() : initialize class
        __str__() : print string of event
        User_Define() : Uses user input to define class attributes
    '''
    def __init__(self,eventName='',eventdescription='',eventtiming=ET.EventTiming):
        # initialize all attributes
        self.eventname = eventName
        self.eventdescription = eventdescription
        self.eventtiming = eventtiming

    def __str__(self):
        # return string of event
        display = '-- ' + str(self.eventtiming) + ' --'
        display += '\n* ' + self.eventname 
        display +=  self.eventdescription + '\n'
        return display
    
    def User_Define(self):
        # use user input to redefine class attributes
        self.eventname = input('Event Name: ')
        self.eventdescription = input('Event Description: ')
        self.eventtiming = self.eventtiming.User_Define(self)

def Fill_Year(year=2023):
    '''
    Method for filling Year object with all month and day objects necessary
    '''
    months = []
    for i in range(1,13):
        days = []
        if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12:
            x = 32
        elif i==4 or i==6 or i==9 or i==11:
            x = 31
        else:
            if year % 4 == 0:
                x = 30
            else:
                x = 29
        for j in range(1,x):
            day = DA.Day(D.Date(year,i,j))
            days.append(day)
        month = M.Month(i,days,year)
        months.append(month)
    return Y.Year(year,months)

def Day_Of_Week(dayinweek=ET.Date):
    '''
    method for returning day of the week number 0-6 based 
    on Date object passed as argument 1
    '''
    x = str(dayinweek.year)
    y = int(x[2:])
    y = y + (y //4)
    y += dayinweek.day
    if dayinweek.month == 4 or dayinweek.month == 7:
        y += 0
    elif dayinweek.month == 1 or dayinweek.month == 10:
        y += 1
    elif dayinweek.month == 5:
        y += 2
    elif dayinweek.month == 8:
        y += 3
    elif dayinweek.month == 2 or dayinweek.month == 3 or dayinweek.month == 11:
        y += 4
    elif dayinweek.month == 6:
        y += 5
    elif dayinweek.month == 9 or dayinweek.month == 12:
        y += 6
    if dayinweek.leapyear:
        if dayinweek.month == 1 or dayinweek.month == 2:
            y -= 1
    y += 5
    y = y % 7
    return y