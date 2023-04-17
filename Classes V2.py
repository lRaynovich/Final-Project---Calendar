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
            

        
        
        
        






class EventTiming:
    def __init__(self,start=Time, Duration=):


    def __str__(self):



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
        while days > 0:
            if self.month == 1 or self.month==3 or self.month==5 or self.month==7 or self.month==8 or self.month==10:
                if days > 31:
                    self.month += 1
                    days -= 31
                else:
                    self.day = days
                    days = days - days

            elif self.month == 4 or self.month == 6 or self.month==9 or self.month==11:
                if days > 30:
                    self.month += 1
                    days -= 30
                else:
                    self.day = days
                    days = days - days

            elif self.month == 2:
                if self.leapyear:
                    if days > 29:
                        self.month += 1
                        days -= 29
                    else:
                        self.day = days
                        days = days - days
                else:
                    if days > 28:
                        self.month += 1
                        days -= 28
                    else:
                        self.day = days
                        days = days - days
            elif self.month == 12:
                if days > 31:
                    self.month = 1
                    self.year += 1
                    if self.year % 4 == 0:
                        self.leapyear = True
                    else:
                        self.leapyear = False
                    days -= 31
                else:
                    self.day = days
                    days = days - days

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


class Event:
    def __init__(self,eventName='',eventDescription='',date=Date,time=Time):


    def __str__(self):

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

    def Add_Event(self,event=Event):


    
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



'''
class EventGroup:
    def __init__(self):

    def __str__(self):

class Birthday(Event):
    def __init__(self):

    def __str__(self):

class Week:
    def __init__(self):

    def __str__(self):'''

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

y2024 = Fill_Year(2024)

print(y2024.months[0])