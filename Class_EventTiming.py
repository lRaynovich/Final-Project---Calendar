'''
This module stores the event timing class for 
storing all information for an events timing
'''

#import needed modules
import Class_Date as D
import Class_Time as T

class EventTiming(T.Time):
    '''
    Class for storing event time details also inherites time
    Attributes:
        starttime : Time object
        endtime : Time object
        startdate : Date object
        enddate : Date object
    Methods:
        __init__ : initializes class
        __str__ : returns string of event timing
        User_define : allows user input to define class
    '''
    def __init__(self,starttime=T.Time, endtime=T.Time,startdate=D.Date,enddate=D.Date):
        # initializes
        self.starttime = starttime
        self.endtime = endtime
        self.startdate = startdate
        self.enddate = enddate

    def __str__(self):
        # returns string of event timing details
        display = ''
        if self.startdate == self.enddate:
                display += 'Date : ' + str(self.startdate) + '  '
                display += 'Time : ' + str(self.starttime) + ' to ' + str(self.endtime)
        else:
            display += 'Start : ' + str(self.startdate) + ' ' + str(self.starttime)
            display += '\nEnd : ' + str(self.enddate) + ' ' + str(self.endtime)
        return display
    
    def User_Define(self):
        # uses user input to define class - used for testing class before GUI
        self.allday = input("All day?(Enter 'y' or 'n') ")
        while self.allday != 'y' and self.allday != 'n':
            self.allday = input("Enter 'y' or 'n' for yes or no: ")
        print('Enter start date: ')
        X = True
        while X:
            try:
                y1 = int(input('Year(YYYY): '))
                X = False
            except ValueError:
                print('ERROR - Enter a year #(YYYY)')
                X = True
        X = True
        while X:
            try:
                m1 = int(input('Month: '))
                X = False
            except ValueError:
                print('ERROR - Enter a Month #')
                X = True
        X = True
        while X:
            try:
                d1 = int(input('Day: '))
                X = False
            except ValueError:
                print('ERROR - Enter a Day #')
                X = True
        self.startdate = D.Date(y1,m1,d1)
        print('Enter end date: ')
        X = True
        while X:
            y2 = input('Year(YYYY OR press ENTER if event is one day): ')
            if y2 == '':
                self.enddate = self.startdate
                X = False
            else:
                try:
                    y = int(y2)
                    X = False
                except:
                    print('ERROR - Enter a day or press ENTER')
                    X = True
        if y2 != '':
            X = True
            while X:
                try:
                    m2 = int(input('Month: '))
                    X = False
                except ValueError:
                    print('ERROR - Enter a Month #')
                    X = True
            X = True
            while X:
                try:
                    d2 = int(input('Day: '))
                    X = False
                except ValueError:
                    print('ERROR - Enter a Day #')
                    X = True
            self.startdate = D.Date(y,m2,d2)
        if self.allday:
            self.starttime = T.Time(0,0)
            self.endtime = T.Time(0,0)
        else:
            X = True
            print('Enter start time(24 hr clock): ')
            while X:
                try:
                    h = int(input('Hour: '))
                    X = False
                except ValueError:
                    print('ERROR - enter hour #')
                    X = True
            X = True 
            while X:
                try:
                    mi = int(input('Minutes: '))
                    X = False
                except ValueError:
                    print('ERROR - enter minute #')
                    X = True
            self.starttime = T.Time(h,mi)
            X = True
            print('Enter end time(24 hr clock): ')
            while X:
                try:
                    h = int(input('Hour: '))
                    X = False
                except ValueError:
                    print('ERROR - enter hour #')
                    X = True
            X = True 
            while X:
                try:
                    mi = int(input('Minutes: '))
                    X = False
                except ValueError:
                    print('ERROR - enter minute #')
                    X = True
            self.endtime = T.Time(h,mi)