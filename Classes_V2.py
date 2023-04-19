'''
second version of the calendar classes for 
python final project
'''


import pickle

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
            return str(hourholder) + ':' + str(self.minuteholder) + ' AM'
        else:
            return str(hourholder) + ':' + str(self.minuteholder) + ' PM'
        
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
            

class Date:
    def __init__(self,year=1,month=1,day=1):
        # set values equal to arguments
        self.year = year
        self.month = month
        self.day = day
        self.monthstr = ''
        self.monthstrabr = ''
        # confine month to bounds 1-12
        if self.month < 1:
            self.month = 1
        elif self.month > 12:
            self.month = 12
        # confine year to at least 2023
        if self.year < 2023:
            self.year = 2023
        # generate leap year attribute
        if self.year % 4 == 0:
            self.leapyear = True
        else:
            self.leapyear = False
        # create confines for days depending on month and leap year
        if self.month==1 or self.month==3 or self.month==5 or self.month==7 or self.month==8 or self.month==10 or self.month==12:
            if self.day > 31:
                self.day = 31
        elif self.month==4 or self.month==6 or self.month==9 or self.month==11:
            if self.day > 30:
                self.day = 30
        elif self.month==2:
            if self.leapyear:
                if self.day > 29:
                    self.day = 29
            else:
                if self.day > 28:
                    self.day = 28
        # confine day to above 1
        if self.day < 1:
            self.day = 1
        # create attribute for day string
        if self.day==1 or self.day==21 or self.day==31:
            self.daystr = str(self.day) + 'st'
        elif self.day==2 or self.day==22:
            self.daystr = str(self.day) + 'nd'
        elif self.day==3 or self.day==23:
            self.daystr = str(self.day) + 'rd'
        else:
            self.daystr = str(self.day) + 'th'
        # create attributes for month stringa and abbreviated month string
        if self.month == 1:
            self.monthstr = 'January'
            self.monthstrabr = 'Jan'
        elif self.month == 2:
            self.monthstr = 'February'
            self.monthstrabr = 'Feb'
        elif self.month == 3:
            self.monthstr = 'March'
            self.monthstrabr = 'Mar'
        elif self.month == 4:
            self.monthstr = 'April'
            self.monthstrabr = 'Apr'
        elif self.month == 5:
            self.monthstr = 'May'
            self.monthstrabr = 'May'
        elif self.month == 6:
            self.monthstr = 'June'
            self.monthstrabr = 'Jun'
        elif self.month == 7:
            self.monthstr = 'July'
            self.monthstrabr = 'Jul'
        elif self.month == 8:
            self.monthstr = 'August'
            self.monthstrabr = 'Aug'
        elif self.month == 9:
            self.monthstr = 'September'
            self.monthstrabr = 'Sep'
        elif self.month == 10:
            self.monthstr = 'October'
            self.monthstrabr = 'Oct'
        elif self.month == 11:
            self.monthstr = 'November'
            self.monthstrabr = 'Nov'
        elif self.month == 12:
            self.monthstr = 'December'
            self.monthstrabr = 'Dec'
        else:
            self.monthstr = 'Error'
            self.monthstrabr = 'Err'

    def __str__(self):
        # returns normal date
        return str(self.month) + '/' + str(self.day) + '/' + str(self.year)
    
    def __eq__(self, other):
        if self.day == other.day and self.month == other.month and self.year == other.year:
            return True
        else:
            return False
    
    def DayString(self):
        # returns day string
        return self.daystr

    def DateString(self):
        # returns full date string
        return self.monthstr + ' ' + self.daystr + ', ' + str(self.year)
    
    def DateStringAbr(self):
        # returns abreviate date string with month and day
        return self.monthstrabr + ' ' + self.daystr
    
    def Next_Date(self, adddays):
        days = adddays + self.day
        finalyear = self.year
        finalmonth = self.month
        finalday = self.day
        finalleapyear = self.leapyear
        while days > 0:
            if finalmonth == 1 or finalmonth==3 or finalmonth==5 or finalmonth==7 or finalmonth==8 or finalmonth==10:
                if days > 31:
                    finalmonth += 1
                    days -= 31
                else:
                    finalday = days
                    days = days - days

            elif finalmonth == 4 or finalmonth== 6 or finalmonth==9 or finalmonth==11:
                if days > 30:
                    finalmonth += 1
                    days -= 30
                else:
                    finalday = days
                    days = days - days

            elif finalmonth == 2:
                if finalleapyear:
                    if days > 29:
                        finalmonth += 1
                        days -= 29
                    else:
                        finalday = days
                        days = days - days
                else:
                    if days > 28:
                        finalmonth+= 1
                        days -= 28
                    else:
                        finalday = days
                        days = days - days
            elif finalmonth == 12:
                if days > 31:
                    finalmonth = 1
                    finalyear += 1
                    if finalyear % 4 == 0:
                        finalleapyear = True
                    else:
                        finalleapyear = False
                    days -= 31
                else:
                    finalday = days
                    days = days - days
        return Date(finalyear,finalmonth,finalday)

    def Prev_Date(self,takedays):
        finalyear = self.year
        inalmonth = self.month
        finalday = self.day
        finalleapyear = self.leapyear
        days = finalday - takedays
        while days < 0:
            if inalmonth == 1:
                finalyear -= 1
                if finalyear % 4 == 0:
                    finalleapyear = True
                else:
                    finalleapyear = False
                days -= 31
                inalmonth = 12
                days = 31 + days
            elif inalmonth==2 or inalmonth==4 or inalmonth==6 or inalmonth==8 or inalmonth==9 or inalmonth == 11:
                inalmonth = inalmonth - 1
                days = 31 + days
            elif inalmonth == 5 or inalmonth == 7 or inalmonth == 10 or inalmonth==12:
                inalmonth = inalmonth - 1
                days = 30 + days
            elif inalmonth == 3:
                inalmonth = 1
                if finalleapyear:
                    days = 29 + days
                else:
                    days = 28 + days
        finalday= days
        return Date(finalyear,inalmonth,finalday)



class EventTiming:
    def __init__(self,starttime=Time, endtime=Time,startdate=Date,enddate=Date, allday=False):
        self.starttime = starttime
        self.endtime = endtime
        self.startdate = startdate
        self.enddate = enddate
        self.allday = allday

    def __str__(self):
        display = ''
        if self.startdate == self.enddate:
            if self.allday:
                display += str(self.startdate) + ' All Day'
            else:
                display += 'Time : ' + str(self.starttime) + ' to ' + str(self.endtime)
        else:
            if self.allday:
                display += 'Start : ' + str(self.startdate)
                display += '\nEnd : ' + str(self.enddate)
            else:
                display += 'Start : ' + str(self.startdate) + ' ' + str(self.starttime)
                display += '\nEnd : ' + str(self.enddate) + ' ' + str(self.endtime)
        return display
    
    def User_Define(self):
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
        self.startdate = Date(y1,m1,d1)
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
            self.startdate = Date(y,m2,d2)
        if self.allday:
            self.starttime = Time(0,0)
            self.endtime = Time(0,0)
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
            self.starttime = Time(h,mi)
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
            self.endtime = Time(h,mi)











''''
class RecurringTime(EventTiming):
    def __init__(self, starttime=Time, endtime=Time, startdate=Date, enddate=Date, allday=False,recurringdates=[]):
        super().__init__(starttime, endtime, startdate, enddate, allday)
        self.recurringdates = recurringdates
        self.recurring string
'''

class Event:
    def __init__(self,eventName='',eventdescription='',eventtiming=EventTiming):
        self.eventname = eventName
        self.eventdescription = eventdescription
        self.eventtiming = eventtiming

    def __str__(self):
        display = '-- ' + str(self.eventtiming) + ' --'
        display += '\n* ' + self.eventname + ' *'
        display += '\n' + self.eventdescription
        return display
    
    def User_Define(self):
        self.eventname = input('Event Name: ')
        self.eventdescription = input('Event Description: ')
        self.eventtiming = self.eventtiming.User_Define(self)



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

    
class Day:
    def __init__(self,date= Date,events=[]):
        self.date = date
        self.events = events
        self.eventCount = 0
        for event in self.events:
            self.eventCount += 1

    def __str__(self):
        display = '\n-- ' + self.date.DateString() + ' --'
        for event in self.events:
            display += event
        return display
    
    def Abbreviate(self):
        return ('-- ' + self.date.daystr + ' : ' + str(self.eventCount) + ' events --')



class Calendar:
    def __init__(self,name='',description='',years=[]):
        self.name = name
        self.description = description
        self.years = years
    
    def __str__(self):
        display = ''
        display += ('\n' + ('*' * 20) + '\n-- ' + self.name + ' --\n' + ('*' * 20) + '\n')
        for year in self.years:
            display += str(year)
        display += ('\n' + ('*' * 20) + '\n')
        return display
    
    def save(self, fileName):
        with open(fileName, 'wb') as f:
            print('\n       Saving Calendar . . .\n')
            pickle.dump(self, f)
            print('\n   Calendar Saved!\n')

    def load(self, fileName):
        with open(fileName, 'rb') as f:
            print('\n       Loading Calendar . . .\n')
            pickle.load(f)
            print('\n   Calendar Loaded!\n')

    def Add_Year(self,year=Year):
        self.years.append(year)


#   def Add_Event(self,event=Event):
#      self.events


'''
class EventGroup:
    def __init__(self):

    def __str__(self):

class Birthday(Event):
    def __init__(self):

    def __str__(self):
'''

def Fill_Year(year=2023):
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
            day = Day(Date(year,i,j))
            days.append(day)
        month = Month(i,days,year)
        months.append(month)
    return Year(year,months)

def Day_Of_Week(dayinweek=Date):
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

'''a = Date(2023,4,20)
print(Day_Of_Week(a))'''
