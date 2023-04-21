'''
This module stores the calendar event which stores all 
information in a calendar
'''

# import necessary modules
import pickle
import Class_Year as Y

class Calendar:
    '''
    Calendar class for storing all information for calendar objects
    Attributes:
        events : list of Event objects
    Methods:
        __init__() : initializes
        partition(arg1,arg2,arg3) : partition method for quicksort
        quicksort(arg1,arg2,arg3) : quicksort events based on date
        __str__() : returns string of calendar
        save(arg1) : saves calendar into arg1 filename
        load(arg1) : loads calendar from arg1 filename
        add_year(arg1) : adds Year object to calendar
    '''
    def __init__(self,events=[]):
        # initialize
        self.events = events


    def partition(self, A, p, r):
        # method for quicksort for sorting events
        x = A[r]
        i = p - 1
        for j in range(p,r):
            if A[j].eventtiming.startdate <= x.eventtiming.startdate:
                i += 1
                (A[i], A[j]) = (A[j], A[i])
        (A[i+1], A[r]) = (A[r], A[i+1])
        return(i+1)

    
    def quicksort(self,A, p, r):
        # method for sorting evets based on start time
        if(p < r):
            q = self.partition(A, p, r)
            self.quicksort(A, p, q-1)
            self.quicksort(A, q+1, r)
    
    def __str__(self):
        # returns sorted string of calendar events
        display = '\n***************\n'
        display += str(self.events[0]) + ':\n'
        display += str(self.events[1])
        display += '\n***************\n'
        A = []
        for i in range(2,len(self.events)):
            A.append(self.events[i])
        self.quicksort(A, 0, len(A) - 1)
        X = [self.events[0],self.events[1]] + A
        for i in range(2,len(X)):
            display += str(X[i])
            display += '-------------------\n'
        display += ('\n' + ('*' * 20) + '\n')
        return display

    def save(self, fileName):
        # saves calendar into filename
        with open(fileName, 'wb') as f:
            print('\n       Saving Calendar . . .\n')
            pickle.dump(self.events, f)
            print('\n   Calendar Saved!\n')

    def load(self, fileName):
        # loads calendar from filename
        with open(fileName, 'rb') as f:
            print('\n       Loading Calendar . . .\n')
            self.events = pickle.load(f)
            print('\n   Calendar Loaded!\n')

    def Add_Year(self,year=Y.Year):
        # Add year object to calendar
        self.years.append(year)

