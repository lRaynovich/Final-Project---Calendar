'''

'''

import Class_Date as D

class Day:
    def __init__(self,date= D.Date,events=[]):
        self.date = date
        self.events = events
        self.eventCount = 0
        for event in self.events:
            self.eventCount += 1

    def partition(self, A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p,r):
            if A[j].eventtiming.starttime <= x.eventtiming.starttime:
                i += 1
                (A[i], A[j]) = (A[j], A[i])
        (A[i+1], A[r]) = (A[r], A[i+1])
        return(i+1)

    
    def quicksort(self,A, p, r):
        if(p < r):
            q = self.partition(A, p, r)
            self.quicksort(A, p, q-1)
            self.quicksort(A, q+1, r)

    def __str__(self):
        A = self.events
        self.quicksort(A, 0, len(A) - 1)


        display = '\n-- ' + self.date.DateString() + ' --\n'
        for e in A:
            display += str(e) + '**********\n'
        return display
    
    def Abbreviate(self):
        return ('-- ' + self.date.daystr + ' : ' + str(self.eventCount) + ' events --')