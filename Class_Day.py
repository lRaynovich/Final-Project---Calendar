'''
This module stores the day class which stores 
all the information for a day object 
'''

#import needed modules
import Class_Date as D

class Day:
    '''
    Class day for storing events in a day
    Attributes: 
        date : Date object
        events : list of Event objects
        eventcount : int
    Methods:
        __init__ : initialize
        partition : partition method for quicksort
        quicksort : quicksorts events based on starttime
        __str__ : return string of events in day
        Abbreviate : returns abbreviated string of events in day
        '''
    def __init__(self,date= D.Date,events=[]):
        # initialize
        self.date = date
        self.events = events
        self.eventCount = 0
        for event in self.events:
            self.eventCount += 1

    def partition(self, A, p, r):
        # partition method for quicksort
        x = A[r]
        i = p - 1
        for j in range(p,r):
            if A[j].eventtiming.starttime <= x.eventtiming.starttime:
                i += 1
                (A[i], A[j]) = (A[j], A[i])
        (A[i+1], A[r]) = (A[r], A[i+1])
        return(i+1)

    
    def quicksort(self,A, p, r):
        # quicksort events based on event time
        if(p < r):
            q = self.partition(A, p, r)
            self.quicksort(A, p, q-1)
            self.quicksort(A, q+1, r)

    def __str__(self):
        # return string of events in day
        A = self.events
        self.quicksort(A, 0, len(A) - 1)
        display = '\n-- ' + self.date.DateString() + ' --\n'
        for e in A:
            display += str(e) + '**********\n'
        return display
    
    def Abbreviate(self):
        # return abbreviated string of event in day
        return ('-- ' + self.date.daystr + ' : ' + str(self.eventCount) + ' events --')