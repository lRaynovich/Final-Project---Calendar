'''
This module stores the custom date class for 
storing all information of date
'''

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
        
    def __le__(self,other):
        if self.year < other.year:
            return True
        elif self.year > other.year:
            return False
        else:
            if self.month < other.month:
                return True
            elif self.month > other.month:
                return False
            else:
                if self.day < other.day:
                    return True
                elif self.day > other.day:
                    return False
                else:
                    return True

    def __lt__(self,other):
        if self.year < other.year:
            return True
        elif self.year > other.year:
            return False
        else:
            if self.month < other.month:
                return True
            elif self.month > other.month:
                return False
            else:
                if self.day < other.day:
                    return True
                elif self.day > other.day:
                    return False
                else:
                    return False

    def __ge__(self,other):
        if self.year > other.year:
            return True
        elif self.year < other.year:
            return False
        else:
            if self.month > other.month:
                return True
            elif self.month < other.month:
                return False
            else:
                if self.day > other.day:
                    return True
                elif self.day < other.day:
                    return False
                else:
                    return True

    def __gt__(self,other):
        if self.year > other.year:
            return True
        elif self.year < other.year:
            return False
        else:
            if self.month > other.month:
                return True
            elif self.month < other.month:
                return False
            else:
                if self.day > other.day:
                    return True
                elif self.day < other.day:
                    return False
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