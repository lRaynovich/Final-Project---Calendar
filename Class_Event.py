'''

'''

import Class_EventTiming as ET

class Event:
    def __init__(self,eventName='',eventdescription='',eventtiming=ET.EventTiming):
        self.eventname = eventName
        self.eventdescription = eventdescription
        self.eventtiming = eventtiming

    def __str__(self):
        display = '-- ' + str(self.eventtiming) + ' --'
        display += '\n* ' + self.eventname 
        display +=  self.eventdescription + '\n'
        return display
    
    def User_Define(self):
        self.eventname = input('Event Name: ')
        self.eventdescription = input('Event Description: ')
        self.eventtiming = self.eventtiming.User_Define(self)