'''
This module stores the main code for Calendar App Final Project made by Luke Raynovich.
The main class in this module is the MyGUI class which holds all the GUI objects needed for the
system to operate. This module also required the following modules to alse be downloaded,
Modules:
    Class_Date
    Class_Time
    Class_EventTiming
    Class_Day
    Class_Calendar
    Class_Event
    Class_Month
    Class_Year

To run the Calendar App simply run this module.
Thanks, and I hope you enjoy!
'''

# import all needed items from tkinter
import tkinter as tk
from tkinter import messagebox

# Import all requred classes
import Class_Date as D
import Class_Time as T
import Class_EventTiming as ET
import Class_Day as DA
import Class_Calendar as C
import Class_Event as E

# GUI Class for storing all needed GUI objects and methods for GUI
class MyGUI:
    '''
    MyGUI class for storing GUI frames and objects. 
    Class also stores all required methods for GUI and object commands. 
    Attributes:
        filename 
        year_select
        month_select
        day_select
        calendar
        startdate
    Additionally class holds attributs for all objects of GUI
    Methods:
        __init__() : initialize
        nav_<month> : method for month button commands, navigates to designated month
        day<day#> : method for day button commands, navigates to designated month
        edit_event : command called by edit event button 
        exit_event : command called by exit event button
        add_event : command called by add event buton
        load_file : command called by load file button
        create_file : command called by create file button
        plus_year : command called by plus year button
        minus_year : command called by minus year button
        back_to_year : command called by back to year button
        back_to_month : command called by back to month button
        on_closing : command called by on closing button
        day_page : command called by day page button
    '''
    def __init__(self):
        '''
        initialization : load all GUI objects into attributes, along with
        normal class attributes
        '''
        # initialize all normal attributes and 
        self.filename = ''
        self.welcomepage = 0
        self.year_select = 2023
        self.month_select = 0
        self.day_select = 0
        self.calendar = C.Calendar()
        self.startdate = D.Date(2023,12,31)
        self.calendar.events.append('')
        self.calendar.events.append('')

        # Establishes window and sets title and size
        self.window = tk.Tk()
        self.window.title('Calendar')
        self.window.geometry('800x500')

        # Create first set of frames
        self.frame1 = tk.Frame(self.window)
        self.frame2 = tk.Frame(self.window)
        self.frame3 = tk.Frame(self.window)
        self.frame4 = tk.Frame(self.window)
        self.frame7 = tk.Frame(self.window)
        #Place first set of frames
        self.frame1.place(x=500,y=100)
        self.frame2.place(x=450,y=200)
        self.frame3.place(x=520,y=200)
        self.frame4.place(x=500,y=250)
        self.frame7.place(x=20,y=120)

        # Start window list for all start window frames
        self.startwindow = []
        self.startwindow.append(self.frame1)
        self.startwindow.append(self.frame2)
        self.startwindow.append(self.frame3)
        self.startwindow.append(self.frame4)
        self.startwindow.append(self.frame7)

        # Objects for starting window
        self.create_file_button = tk.Button(self.frame1,height=3, width = 16, text='Create New File', font=('Arial', 16),command=self.create_file)
        self.create_file_button.pack()
        self.create_file_label = tk.Label(self.frame2,text = 'filename:', font=('Arial', 16))
        self.create_file_label.pack()
        self.create_filename = tk.Entry(self.frame3, width = 20)
        self.create_filename.pack()
        self.load_file_button = tk.Button(self.frame4,height=3, width = 16, text='Load Old File', font=('Arial', 16),command=self.load_file)
        self.load_file_button.pack()
        self.information = tk.Label(self.frame7,text='Welcome to my Final Exam Calendar App', font=(('Arial',20)))
        self.information.pack(padx=10,pady=10)
        # intro text welcome message
        introtext = ''
        introtext += 'Enter a filename to get started\n\n'
        introtext += 'Close the window to save your\n'
        introtext += 'calendar when you are done\n\n'
        introtext += 'Enjoy!'
        self.introduction = tk.Label(self.frame7,text=introtext,font=('Arial', 16))
        self.introduction.pack(padx=5,pady=5)

        # Create second set of frames
        self.frame11 = tk.Frame(self.window)
        self.frame12 = tk.Frame(self.window)
        self.frame13 = tk.Frame(self.window)
        # Place second set of frames
        self.frame11.place(x=350,y=100)
        self.frame12.place(x=494,y=100)
        self.frame13.place(x=638,y=100)

        # Third set of frames
        self.frame23 = tk.Frame(self.window)
        self.frame23.place(x=10,y=10)

        # Event label and box for displaying events
        self.event_label = tk.Label(self.frame23,height=1,width=35,text='Events:', font=('Arial', 16))
        self.events_box = tk.Text(self.frame23,height=10,width=50,)

        # Fourth set of frames
        self.frame41 = tk.Frame(self.window)
        self.frame42 = tk.Frame(self.window)
        self.frame43 = tk.Frame(self.window)
        self.frame44 = tk.Frame(self.window)
        #place fourth set of frames
        self.frame41.place(x=360,y=50)
        self.frame42.place(x=480,y=40)
        self.frame43.place(x=700,y=50)
        self.frame44.place(x=530,y=10)

        # Events frame for displaying events for entire calendar
        self.events_frame = tk.LabelFrame(self.window,text='Events',background='Gray')
        self.events_label = tk.Text(self.events_frame,height=23,width=47,font=('Arial',10))
        self.events_label.pack()

        # Objects for editing and saving calendar name and description
        self.cname = tk.Label(self.frame23,height=1,width=35,text='Calendar Name:', font=('Arial', 16))
        self.cnametext = tk.Entry(self.frame23,width=20,font=('Arial', 14))
        self.cdesc = tk.Label(self.frame23,height=1,width=25,text='Calendar description:', font=('Arial', 16))
        self.cdesctext = tk.Text(self.frame23,height=5,width=45,font=('Arial', 12))
        self.cnametextsave = tk.Label(self.frame23,width=20,height=1,text=(self.calendar.events[0]),font=('Arial', 14))
        self.cdesctextsave = tk.Label(self.frame23,width=45,height=5,text=(self.calendar.events[1]),font=('Arial',12))

        # Buttons for saving entries in previous objects
        self.cdetailssave = tk.Button(self.frame23,height=1,width=4, text='save',command=self.cdetails_save)
        self.cdetailsedit = tk.Button(self.frame23,height=1,width=4, text='edit',command=self.cdetails_edit)

        # Next and Previous Year/Month buttons for navigating months and years
        self.year_prev = tk.Button(self.frame41,height=2,width=4, text='prev',command=self.minus_year)
        self.year_next = tk.Button(self.frame43,height=2,width=4, text='next',command=self.plus_year)
        self.year_label = tk.Label(self.frame42,height=1,width=10,text=str(self.year_select), font=('Arial',40))

        # Mode Year and Month Buttons for navigating to and from month and year mode
        self.mode_year = tk.Button(self.frame44,height=1,width=4,text='years',command=self.back_to_year)
        self.mode_month = tk.Button(self.frame44,height=1,width=4,text='months',command=self.back_to_month)

        # list for organizing control buttons
        self.control_buttons = []
        self.control_buttons.append(self.year_next)
        self.control_buttons.append(self.year_prev)
        self.control_buttons.append(self.year_label)
 
        # Frame set 5
        self.frame51 = tk.Frame(self.window)
        self.frame51.place(x=10,y=200)

        # Frame for all month buttons
        self.ym_buttons = tk.Frame(self.window)

        # All month navigation month which call thier personal month navigation commands
        self.jan_but = tk.Button(self.ym_buttons,height=3, width = 12, text='January', font=('Arial', 16),command=self.nav_jan)
        self.jan_but.grid(row=0,column=0)
        self.feb_but = tk.Button(self.ym_buttons,height=3, width = 12, text='February', font=('Arial', 16),command=self.nav_feb)
        self.feb_but.grid(row=0,column=1)
        self.mar_but = tk.Button(self.ym_buttons,height=3, width = 12, text='March', font=('Arial', 16),command=self.nav_mar)
        self.mar_but.grid(row=0,column=2)
        self.apr_but = tk.Button(self.ym_buttons,height=3, width = 12, text='April', font=('Arial', 16),command=self.nav_apr)
        self.apr_but.grid(row=1,column=0)
        self.may_but = tk.Button(self.ym_buttons,height=3, width = 12, text='May', font=('Arial', 16),command=self.nav_may)
        self.may_but.grid(row=1,column=1)
        self.jun_but = tk.Button(self.ym_buttons,height=3, width = 12, text='June', font=('Arial', 16),command=self.nav_jun)
        self.jun_but.grid(row=1,column=2)
        self.jul_but = tk.Button(self.ym_buttons,height=3, width = 12, text='July', font=('Arial', 16),command=self.nav_jul)
        self.jul_but.grid(row=2,column=0)
        self.aug_but = tk.Button(self.ym_buttons,height=3, width = 12, text='August', font=('Arial', 16),command=self.nav_aug)
        self.aug_but.grid(row=2,column=1)
        self.sep_but = tk.Button(self.ym_buttons,height=3, width = 12, text='September', font=('Arial', 16),command=self.nav_sep)
        self.sep_but.grid(row=2,column=2)
        self.oct_but = tk.Button(self.ym_buttons,height=3, width = 12, text='October', font=('Arial', 16),command=self.nav_oct)
        self.oct_but.grid(row=3,column=0)
        self.nov_but = tk.Button(self.ym_buttons,height=3, width = 12, text='November', font=('Arial', 16),command=self.nav_nov)
        self.nov_but.grid(row=3,column=1)
        self.dec_but = tk.Button(self.ym_buttons,height=3, width = 12, text='December', font=('Arial', 16),command=self.nav_dec)
        self.dec_but.grid(row=3,column=2)

        # Frame for all day buttons
        self.day_button_frame = tk.Frame(self.window)
        # List for organizing all day buttons
        self.day_buttons = []

        # All day navigation buttons which call their navigation commands
        self.day_1 = tk.Button(self.day_button_frame,height=2,width=4, text='1st',font=('Arial', 16),command=self.day1)
        self.day_2 = tk.Button(self.day_button_frame,height=2,width=4, text='2nd',font=('Arial', 16),command=self.day2)
        self.day_3 = tk.Button(self.day_button_frame,height=2,width=4, text='3rd',font=('Arial', 16),command=self.day3)
        self.day_4 = tk.Button(self.day_button_frame,height=2,width=4, text='4th',font=('Arial', 16),command=self.day4)
        self.day_5 = tk.Button(self.day_button_frame,height=2,width=4, text='5th',font=('Arial', 16),command=self.day5)
        self.day_6 = tk.Button(self.day_button_frame,height=2,width=4, text='6th',font=('Arial', 16),command=self.day6)
        self.day_7 = tk.Button(self.day_button_frame,height=2,width=4, text='7th',font=('Arial', 16),command=self.day7)
        self.day_8 = tk.Button(self.day_button_frame,height=2,width=4, text='8th',font=('Arial', 16),command=self.day8)
        self.day_9 = tk.Button(self.day_button_frame,height=2,width=4, text='9th',font=('Arial', 16),command=self.day9)
        self.day_10 = tk.Button(self.day_button_frame,height=2,width=4, text='10th',font=('Arial', 16),command=self.day10)
        self.day_11 = tk.Button(self.day_button_frame,height=2,width=4, text='11th',font=('Arial', 16),command=self.day11)
        self.day_12 = tk.Button(self.day_button_frame,height=2,width=4, text='12th',font=('Arial', 16),command=self.day12)
        self.day_13 = tk.Button(self.day_button_frame,height=2,width=4, text='13th',font=('Arial', 16),command=self.day13)
        self.day_14 = tk.Button(self.day_button_frame,height=2,width=4, text='14th',font=('Arial', 16),command=self.day14)
        self.day_15 = tk.Button(self.day_button_frame,height=2,width=4, text='15th',font=('Arial', 16),command=self.day15)
        self.day_16 = tk.Button(self.day_button_frame,height=2,width=4, text='16th',font=('Arial', 16),command=self.day16)
        self.day_17 = tk.Button(self.day_button_frame,height=2,width=4, text='17th',font=('Arial', 16),command=self.day17)
        self.day_18 = tk.Button(self.day_button_frame,height=2,width=4, text='18th',font=('Arial', 16),command=self.day18)
        self.day_19 = tk.Button(self.day_button_frame,height=2,width=4, text='19th',font=('Arial', 16),command=self.day19)
        self.day_20 = tk.Button(self.day_button_frame,height=2,width=4, text='20th',font=('Arial', 16),command=self.day20)
        self.day_21 = tk.Button(self.day_button_frame,height=2,width=4, text='21st',font=('Arial', 16),command=self.day21)
        self.day_22 = tk.Button(self.day_button_frame,height=2,width=4, text='22nd',font=('Arial', 16),command=self.day22)
        self.day_23 = tk.Button(self.day_button_frame,height=2,width=4, text='23rd',font=('Arial', 16),command=self.day23)
        self.day_24 = tk.Button(self.day_button_frame,height=2,width=4, text='24th',font=('Arial', 16),command=self.day24)
        self.day_25 = tk.Button(self.day_button_frame,height=2,width=4, text='25th',font=('Arial', 16),command=self.day25)
        self.day_26 = tk.Button(self.day_button_frame,height=2,width=4, text='26th',font=('Arial', 16),command=self.day26)
        self.day_27 = tk.Button(self.day_button_frame,height=2,width=4, text='27th',font=('Arial', 16),command=self.day27)
        self.day_28 = tk.Button(self.day_button_frame,height=2,width=4, text='28th',font=('Arial', 16),command=self.day28)
        self.day_29 = tk.Button(self.day_button_frame,height=2,width=4, text='29th',font=('Arial', 16),command=self.day29)
        self.day_30 = tk.Button(self.day_button_frame,height=2,width=4, text='30th',font=('Arial', 16),command=self.day30)
        self.day_31 = tk.Button(self.day_button_frame,height=2,width=4, text='31st',font=('Arial', 16),command=self.day31)

        # add all buttons to organized list 
        self.day_buttons.append(self.day_1)
        self.day_buttons.append(self.day_2)
        self.day_buttons.append(self.day_3)
        self.day_buttons.append(self.day_4)
        self.day_buttons.append(self.day_5)
        self.day_buttons.append(self.day_6)
        self.day_buttons.append(self.day_7)
        self.day_buttons.append(self.day_8)
        self.day_buttons.append(self.day_9)
        self.day_buttons.append(self.day_10)
        self.day_buttons.append(self.day_11)
        self.day_buttons.append(self.day_12)
        self.day_buttons.append(self.day_13)
        self.day_buttons.append(self.day_14)
        self.day_buttons.append(self.day_15)
        self.day_buttons.append(self.day_16)
        self.day_buttons.append(self.day_17)
        self.day_buttons.append(self.day_18)
        self.day_buttons.append(self.day_19)
        self.day_buttons.append(self.day_20)
        self.day_buttons.append(self.day_21)
        self.day_buttons.append(self.day_22)
        self.day_buttons.append(self.day_23)
        self.day_buttons.append(self.day_24)
        self.day_buttons.append(self.day_25)
        self.day_buttons.append(self.day_26)
        self.day_buttons.append(self.day_27)
        self.day_buttons.append(self.day_28)
        self.day_buttons.append(self.day_29)
        self.day_buttons.append(self.day_30)
        self.day_buttons.append(self.day_31)

        # frame set 9
        self.frame99 = tk.Frame(self.window)
        self.frame99.place(x=600,y=5)
        # add event button
        self.event_add = tk.Button(self.frame99,height=2,width=12,text='{ + } Add Event', font=('Arial', 14), command=self.add_event)
        
        # frame set 6
        self.frame61 = tk.LabelFrame(self.window,text='Add Event',background='Black')
        self.frame62 = tk.LabelFrame(self.frame61,text='Event Time',background='Gray')
        self.frame63 = tk.LabelFrame(self.frame61,text='Event Date',background='Gray')
        self.frame64 = tk.Frame(self.frame61,background='Gray')
        self.frame65 = tk.Frame(self.frame61,background='Gray')
        self.frame66 = tk.LabelFrame(self.frame61,text='',background='Gray')

        # all objects for the event creating window which allows user input for event generation
        self.event_start_time = tk.Label(self.frame62,height=1,width=16,text='Start Time(24hr):', font=('Arial', 14))
        self.event_start_time.grid(row=0,column=0)
        self.event_start_hour = tk.Entry(self.frame62,width=2, font=('Arial', 14))
        self.event_start_hour.grid(row=0,column=1)
        self.col1 = tk.Label(self.frame62,height=1,width=1,text=':', font=('Arial', 14))
        self.col1.grid(row=0,column=2)
        self.event_start_minute = tk.Entry(self.frame62,width=2, font=('Arial', 14))
        self.event_start_minute.grid(row=0,column=3)
        self.event_end_time = tk.Label(self.frame62,height=1,width=16,text='End Time(24hr):', font=('Arial', 14))
        self.event_end_time.grid(row=1,column=0)
        self.event_end_hour = tk.Entry(self.frame62,width=2, font=('Arial', 14))
        self.event_end_hour.grid(row=1,column=1)
        self.col2 = tk.Label(self.frame62,height=1,width=1,text=':', font=('Arial', 14))
        self.col2.grid(row=1,column=2)
        self.event_end_minute = tk.Entry(self.frame62,width=2, font=('Arial', 14))
        self.event_end_minute.grid(row=1,column=3)

        # Second half of event creation window
        self.event_start_date = tk.Label(self.frame63,height=1,width=26,text='Start Date(MM/DD/YYYY):', font=('Arial', 14))
        self.event_start_date.grid(row=0,column=0)
        self.event_start_MM = tk.Entry(self.frame63,width=2, font=('Arial', 14))
        self.event_start_MM.grid(row=0,column=1)
        self.sl1 = tk.Label(self.frame63,height=1,width=1,text='/', font=('Arial', 14))
        self.sl1.grid(row=0,column=2)
        self.event_start_DD = tk.Entry(self.frame63,width=2, font=('Arial', 14))
        self.event_start_DD.grid(row=0,column=3)
        self.sl2 = tk.Label(self.frame63,height=1,width=1,text='/', font=('Arial', 14))
        self.sl2.grid(row=0,column=4)
        self.event_start_YYYY = tk.Entry(self.frame63,width=4, font=('Arial', 14))
        self.event_start_YYYY.grid(row=0,column=5)
        self.event_end_date = tk.Label(self.frame63,height=1,width=26,text='End Date(MM/DD/YYYY):', font=('Arial', 14))
        self.event_end_date.grid(row=1,column=0)
        self.event_end_MM = tk.Entry(self.frame63,width=2, font=('Arial', 14))
        self.event_end_MM.grid(row=1,column=1)
        self.sl3 = tk.Label(self.frame63,height=1,width=1,text='/', font=('Arial', 14))
        self.sl3.grid(row=1,column=2)
        self.event_end_DD = tk.Entry(self.frame63,width=2, font=('Arial', 14))
        self.event_end_DD.grid(row=1,column=3)
        self.sl4 = tk.Label(self.frame63,height=1,width=1,text='/', font=('Arial', 14))
        self.sl4.grid(row=1,column=4)
        self.event_end_YYYY = tk.Entry(self.frame63,width=4, font=('Arial', 14))
        self.event_end_YYYY.grid(row=1,column=5)
        self.event_na = tk.Label(self.frame64, height=1, width=20, text='Event Name: ',font=('Arial', 14))
        self.event_na.pack()
        self.event_name = tk.Text(self.frame64,height=1,width=40,font=('Arial', 12))
        self.event_name.pack()
        self.event_de = tk.Label(self.frame65, height=1, width=20, text='Event Description: ',font=('Arial', 14))
        self.event_de.pack()
        self.event_desc = tk.Text(self.frame65,height=3, width=40, font=('Arial', 12))
        self.event_desc.pack()

        # Save and exit buttons for saving or discarding created events
        self.event_save = tk.Button(self.frame66,height=1,width=4,text='save',font=('Arial',14),command=self.save_event)
        self.event_save.grid(row=0,column=0)
        self.event_exit = tk.Button(self.frame66,height=1,width=4,text='exit',font=('Arial',14),command=self.exit_event)
        self.event_exit.grid(row=0,column=1)

        # frame for Faulty edit event button not actually implemented into code
        self.frame89 = tk.LabelFrame(self.window,text='Edit Event')
        self.name_question = tk.Label(self.frame89,text='Event Name:', width=12,height=1,font=('Arial',14))
        self.name_question_box = tk.Entry(self.frame89,width=20,font=('Arial',14))
        self.name_confirm = tk.Button(self.frame89,text='enter',height=1,width=4,font=('Arial',14),command=self.edit_event)
        self.name_question.grid(row=0,column=0)
        self.name_question_box.grid(row=0,column=1)
        self.name_confirm.grid(row=0,column=2)

        
        # list for all event creation window frames required
        self.eventwindow = []
        # add all frames
        self.eventwindow.append(self.frame64)
        self.eventwindow.append(self.frame65)
        self.eventwindow.append(self.frame62)
        self.eventwindow.append(self.frame63)
        self.eventwindow.append(self.frame66)
                               
    
        # Window close protocol that calles on_closing when user tries to close window
        self.window.protocol('WM_DELETE_WINDOW',self.on_closing)

        # Objects needed for day Event display
        self.submit_button = tk.Button(self.window, height=20, width = 50)
        self.day_textframe = tk.LabelFrame(self.window,text='Events')
        self.day_textbox = tk.Text(self.day_textframe,width=61,height=24,font=('Arial',14))
        self.day_textbox.pack()


        # set window as the main loop
        self.window.mainloop()


    '''
    The following methods are for each individual month navigation button.
    The follweing methods organize the GUI to display their month layout.
    Each method is called when their corresponding buttons are pressed.
    '''
    def nav_jan(self):
        for x in self.day_buttons:
            x.grid_forget()
        self.mode_year.pack()
        self.month_select = 1
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()
        self.ym_buttons.place_forget()
        x = E.Day_Of_Week(D.Date(self.year_select,self.month_select,1))
        for i in range(31):
            m = (i  + x) % 7
            n = (i + x) // 7
            self.day_buttons[i].grid(row=n,column=m)
        self.day_button_frame.place(x=300,y=100)
        
    def nav_feb(self):
        for x in self.day_buttons:
            x.grid_forget()
        self.mode_year.pack()
        self.month_select = 2
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()
        self.ym_buttons.place_forget()
        x = E.Day_Of_Week(D.Date(self.year_select,self.month_select,1))
        if D.Date(self.year_select).leapyear:
            xx = 29
        else:
            xx = 28
        for i in range(xx):
            m = (i  + x) % 7
            n = (i + x) // 7
            self.day_buttons[i].grid(row=n,column=m)
        self.day_button_frame.place(x=300,y=100)

    def nav_mar(self):
        for x in self.day_buttons:
            x.grid_forget()
        self.mode_year.pack()
        self.month_select = 3
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()
        self.ym_buttons.place_forget()
        x = E.Day_Of_Week(D.Date(self.year_select,self.month_select,1))
        for i in range(31):
            m = (i  + x) % 7
            n = (i + x) // 7
            self.day_buttons[i].grid(row=n,column=m)
        self.day_button_frame.place(x=300,y=100)

    def nav_apr(self):
        for x in self.day_buttons:
            x.grid_forget()
        self.mode_year.pack()
        self.month_select = 4
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()
        self.ym_buttons.place_forget()
        x = E.Day_Of_Week(D.Date(self.year_select,self.month_select,1))
        for i in range(30):
            m = (i  + x) % 7
            n = (i + x) // 7
            self.day_buttons[i].grid(row=n,column=m)
        self.day_button_frame.place(x=300,y=100)

    def nav_may(self):
        for x in self.day_buttons:
            x.grid_forget()
        self.mode_year.pack()
        self.month_select = 5
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()
        self.ym_buttons.place_forget()
        x = E.Day_Of_Week(D.Date(self.year_select,self.month_select,1))
        for i in range(31):
            m = (i  + x) % 7
            n = (i + x) // 7
            self.day_buttons[i].grid(row=n,column=m)
        self.day_button_frame.place(x=300,y=100)

    def nav_jun(self):
        for x in self.day_buttons:
            x.grid_forget()
        self.mode_year.pack()
        self.month_select = 6
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()
        self.ym_buttons.place_forget()
        x = E.Day_Of_Week(D.Date(self.year_select,self.month_select,1))
        for i in range(30):
            m = (i  + x) % 7
            n = (i + x) // 7
            self.day_buttons[i].grid(row=n,column=m)
        self.day_button_frame.place(x=300,y=100)

    def nav_jul(self):
        for x in self.day_buttons:
            x.grid_forget()
        self.mode_year.pack()
        self.month_select = 7
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()
        self.ym_buttons.place_forget()
        x = E.Day_Of_Week(D.Date(self.year_select,self.month_select,1))
        for i in range(31):
            m = (i  + x) % 7
            n = (i + x) // 7
            self.day_buttons[i].grid(row=n,column=m)
        self.day_button_frame.place(x=300,y=100)

    def nav_aug(self):
        for x in self.day_buttons:
            x.grid_forget()
        self.mode_year.pack()
        self.month_select = 8
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()
        self.ym_buttons.place_forget()
        x = E.Day_Of_Week(D.Date(self.year_select,self.month_select,1))
        for i in range(31):
            m = (i  + x) % 7
            n = (i + x) // 7
            self.day_buttons[i].grid(row=n,column=m)
        self.day_button_frame.place(x=300,y=100)

    def nav_sep(self):
        for x in self.day_buttons:
            x.grid_forget()
        self.mode_year.pack()
        self.month_select = 9
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()
        self.ym_buttons.place_forget()
        x = E.Day_Of_Week(D.Date(self.year_select,self.month_select,1))
        for i in range(30):
            m = (i  + x) % 7
            n = (i + x) // 7
            self.day_buttons[i].grid(row=n,column=m)
        self.day_button_frame.place(x=300,y=100)

    def nav_oct(self):
        for x in self.day_buttons:
            x.grid_forget()
        self.mode_year.pack()
        self.month_select = 10
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()
        self.ym_buttons.place_forget()
        x = E.Day_Of_Week(D.Date(self.year_select,self.month_select,1))
        for i in range(31):
            m = (i  + x) % 7
            n = (i + x) // 7
            self.day_buttons[i].grid(row=n,column=m)
        self.day_button_frame.place(x=300,y=100)

    def nav_nov(self):
        for x in self.day_buttons:
            x.grid_forget()
        self.mode_year.pack()
        self.month_select = 11
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()
        self.ym_buttons.place_forget()
        x = E.Day_Of_Week(D.Date(self.year_select,self.month_select,1))
        for i in range(30):
            m = (i  + x) % 7
            n = (i + x) // 7
            self.day_buttons[i].grid(row=n,column=m)
        self.day_button_frame.place(x=300,y=100)

    def nav_dec(self):
        for x in self.day_buttons:
            x.grid_forget()
        self.mode_year.pack()
        self.month_select = 12
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()
        self.ym_buttons.place_forget()
        x = E.Day_Of_Week(D.Date(self.year_select,self.month_select,1))
        for i in range(31):
            m = (i  + x) % 7
            n = (i + x) // 7
            self.day_buttons[i].grid(row=n,column=m)
        self.day_button_frame.place(x=300,y=100)

    

    def cdetails_save(self):
        '''
        Method for saving calendar description and name.
        Saves all information into calendar class variables and displays
        saved information on screen
        Called by cdetailssave button.
        '''
        self.calendar.events[0] = self.cnametext.get()
        self.calendar.events[1] = self.cdesctext.get('1.0',tk.END)
        self.cname.pack_forget()
        self.cnametext.pack_forget()
        self.cdesc.pack_forget()
        self.cdesctext.pack_forget()
        self.cdetailssave.pack_forget()
        self.cnametextsave = tk.Label(self.frame23,width=20,height=1,text=(self.calendar.events[0]),font=('Arial', 14))
        self.cdesctextsave = tk.Label(self.frame23,width=30,height=7,text=(self.calendar.events[1]),font=('Arial',12))
        self.cname.pack()
        self.cnametextsave.pack()
        self.cdesc.pack()
        self.cdesctextsave.pack()
        self.cdetailsedit.pack()


    def cdetails_edit(self):
        '''
        Method for editing calendar description and name.
        Allows user to input new informationa and reorganizes screen
        Called by cdetailsedit button.
        '''
        self.cname.pack_forget()
        self.cnametextsave.pack_forget()
        self.cdesc.pack_forget()
        self.cdesctextsave.pack_forget()
        self.cdetailsedit.pack_forget()
        self.cnametextsave = tk.Label(self.frame23,width=20,height=1,text=(self.calendar.events[0]),font=('Arial', 14))
        self.cdesctextsave = tk.Label(self.frame23,width=30,height=7,text=(self.calendar.events[1]),font=('Arial',12))
        self.cname.pack()
        self.cnametext.pack()
        self.cdesc.pack()
        self.cdesctext.pack()
        self.cdetailssave.pack()


    def save_event(self):
        '''
        saves information in event creation frame to event object
        which is entered into calendar class
        '''
        # Grabs information from entry boxes
        name = self.event_name.get('1.0',tk.END)
        description = self.event_desc.get('1.0',tk.END)
        startdate1 = D.Date(int(self.event_start_YYYY.get()),int(self.event_start_MM.get()),int(self.event_start_DD.get()))
        enddate1 = D.Date(int(self.event_end_YYYY.get()),int(self.event_end_MM.get()),int(self.event_end_DD.get()))
        starttime1 = T.Time(int(self.event_start_hour.get()),int(self.event_start_minute.get()))
        endtime1 = T.Time(int(self.event_start_hour.get()),int(self.event_start_minute.get()))
        eventtime = ET.EventTiming(starttime1,endtime1,startdate1,enddate1)
        event1 = E.Event(name,description,eventtime)

        #Closes event creation window
        self.calendar.events.append(event1)
        for x in self.eventwindow:
            x.pack_forget()
        self.frame61.place_forget()
        self.events_label.delete('1.0',tk.END)
        self.events_label.insert(tk.END,str(self.calendar))
        if self.day_select != 0:
            self.day_textframe.place(x=300,y=90)
        
    def find_edit(self):
        # Non-implemented find edit method
        self.frame89.place(x=600,y=5)


    def edit_event(self):
        # Buggy Non-Implemented edit event methode for edit event button
        found = False
        delname = self.name_question_box.get()
        self.frame89.place_forget()
        for i in range(2,self.calendar.events):
            if self.calendar.events[i].eventName == delname:
                found = True


    def exit_event(self):
        '''
        Method for exit event button that discards 
        event and closes event creation window
        '''
        for x in self.eventwindow:
            x.pack_forget()
        self.frame61.place_forget()
        if self.day_select != 0:
            self.day_textframe.place(x=300,y=90)
        
    def add_event(self):
        '''
        Method called by add event button that 
        displays event creation window
        '''
        self.day_textframe.place_forget()
        self.frame61.place(x=250,y=100)
        for x in self.eventwindow:
            x.pack()

    def load_file(self):
        '''
        Method for load file button that loads file, 
        closes welcome window and opens main window.
        '''
        filename = self.create_filename.get()
        self.filename = filename
        if filename[-4:] == '.dat':
            self.calendar.load(filename)
            messagebox.showinfo(title='Loading . . .',message="Calendar Loaded!")
            # Close objects in start window
            for x in self.startwindow:
                x.destroy()
            
            # Open all normal window objects
            for y in self.control_buttons:
                y.pack()
            self.ym_buttons.place(x=350,y=100)
            self.event_add.pack()
            self.cnametextsave = tk.Label(self.frame23,width=20,height=1,text=(self.calendar.events[0]),font=('Arial', 14))
            self.cdesctextsave = tk.Label(self.frame23,width=30,height=7,text=(self.calendar.events[1]),font=('Arial',12))
            self.cname.pack()
            self.cnametextsave.pack()
            self.cdesc.pack()
            self.cdesctextsave.pack()
            self.cdetailsedit.pack() 
            self.events_label.delete('1.0',tk.END)
            self.events_label.insert(tk.END,str(self.calendar))
            self.events_frame.place(x=5,y=220)
            self.welcomepage = 1
        else:
            # Error message if incorrect file name
            messagebox.showinfo(title='ERROR',message="Filename must end in '.dat'")


    def create_file(self):
        '''
        Method for creating file button that also closes 
        welcome window and displays normal window
        '''
        filename = self.create_filename.get()
        self.filename = filename
        if filename[-4:] == '.dat':
            self.calendar.save(filename)
            messagebox.showinfo(title='Saving . . .',message="Calendar Created!")
            # Closes welcome window
            for x in self.startwindow:
                x.destroy()

            # Open all normal window objects
            for y in self.control_buttons:
                y.pack()
            self.ym_buttons.place(x=350,y=100)
            self.event_add.pack()
            self.cname.pack()
            self.cnametextsave.pack()
            self.cdesc.pack()
            self.cdesctextsave.pack()
            self.cdetailsedit.pack()
            self.events_label.delete('1.0',tk.END)
            self.events_label.insert(tk.END,str(self.calendar))
            self.events_frame.place(x=5,y=220)
            self.welcomepage = 1
            
        else:
            # Error message if incorrect file name
            messagebox.showinfo(title='ERROR',message="Filename must end in '.dat'")


    def plus_year(self):
        '''
        method for plus year button that navigates to new year/month
        '''
        if self.month_select == 0:
            self.year_select += 1
            self.year_label.pack_forget()
            self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.year_select), font=('Arial',40))
            self.year_label.pack()
        else:
            self.day_button_frame.place_forget()
            for x in self.day_buttons:
                x.grid_forget()
            if self.month_select == 12:
                self.month_select = 1
                self.year_select += 1
            else:
                self.month_select += 1
            self.year_label.pack_forget()
            self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
            self.year_label.pack()
            x = E.Day_Of_Week(D.Date(self.year_select,self.month_select,1))
            xx = 0
            if self.month_select == 1 or self.month_select == 3 or self.month_select == 5 or self.month_select == 7 or self.month_select == 8 or self.month_select == 10 or self.month_select == 12:
                xx = 31
            elif self.month_select == 4 or self.month_select == 6 or self.month_select == 9 or self.month_select == 11:
                xx = 30
            elif self.month_select == 2:
                if D.Date(self.year_select).leapyear:
                    xx = 29
                else:
                    xx = 28
            for i in range(xx):
                m = (i  + x) % 7
                n = (i + x) // 7
                self.day_buttons[i].grid(row=n,column=m)
            self.day_button_frame.place(x=300,y=100)


    def minus_year(self):
        '''
        method for minus year button which navigates to last year/month
        '''
        if self.month_select == 0:
            self.year_select -= 1
            self.year_label.pack_forget()
            self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.year_select), font=('Arial',40))
            self.year_label.pack()
        else:
            self.day_button_frame.place_forget()
            for x in self.day_buttons:
                x.grid_forget()
            if self.month_select == 1:
                self.month_select = 12
                self.year_select -= 1
            else:
                self.month_select -= 1
            self.year_label.pack_forget()
            self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
            self.year_label.pack()
            x = E.Day_Of_Week(D.Date(self.year_select,self.month_select,1))
            xx = 0
            if self.month_select == 1 or self.month_select == 3 or self.month_select == 5 or self.month_select == 7 or self.month_select == 8 or self.month_select == 10 or self.month_select == 12:
                xx = 31
            elif self.month_select == 4 or self.month_select == 6 or self.month_select == 9 or self.month_select == 11:
                xx = 30
            elif self.month_select == 2:
                if D.Date(self.year_select).leapyear:
                    xx = 29
                else:
                    xx = 28
            for i in range(xx):
                m = (i  + x) % 7
                n = (i + x) // 7
                self.day_buttons[i].grid(row=n,column=m)
            self.day_button_frame.place(x=300,y=100)
    
    def back_to_year(self):
        '''
        method for back to year button which sets display mode back to year
        '''
        self.day_button_frame.place_forget()
        self.month_select = 0
        self.mode_year.pack_forget()
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.year_select), font=('Arial',40))
        self.year_label.pack()
        self.ym_buttons.place(x=350,y=100)

    def back_to_month(self):
        '''
        method for back to month button which sets display mode back to month
        '''
        self.year_prev.pack()
        self.year_next.pack()
        self.day_textframe.place_forget()
        self.day_select = 0
        self.mode_month.pack_forget()
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=(str(self.month_select) + '/' + str(self.year_select)), font=('Arial',40))
        self.year_label.pack()
        for x in self.day_buttons:
            x.grid_forget()
        x = E.Day_Of_Week(D.Date(self.year_select,self.month_select,1))
        xx = 0
        if self.month_select == 1 or self.month_select == 3 or self.month_select == 5 or self.month_select == 7 or self.month_select == 8 or self.month_select == 10 or self.month_select == 12:
            xx = 31
        elif self.month_select == 4 or self.month_select == 6 or self.month_select == 9 or self.month_select == 11:
            xx = 30
        elif self.month_select == 2:
            if D.Date(self.year_select).leapyear:
                xx = 29
            else:
                xx = 28
        for i in range(xx):
            m = (i  + x) % 7
            n = (i + x) // 7
            self.day_buttons[i].grid(row=n,column=m)
        self.day_button_frame.place(x=300,y=100)
        self.mode_year.pack()


    def on_closing(self):
        '''
        closing method for when user tries to close window
        '''
        if messagebox.askyesno(title='Quit?', message='Are you sure you would like to exit?'):
            if self.welcomepage == 1:
                if messagebox.askyesno(title='Save?', message='Would you like to save changes?'):
                    self.calendar.save(self.filename)
                    self.window.destroy()
                else:
                    self.window.destroy()
            self.window.destroy()
    

    def day_page(self):
        '''
        method called by all day navigation methods which 
        displays day page specific to the day called
        '''
        self.mode_year.pack_forget()
        self.year_next.pack_forget()
        self.year_prev.pack_forget()
        self.mode_month.pack()
        self.day_button_frame.place_forget()
        self.day_textframe.place(x=300,y=90)
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=10,text=(str(self.month_select) + '/' + str(self.day_select) + '/' + str(self.year_select)), font=('Arial',40))
        self.year_label.pack()
        self.day_textbox.delete('1.0',tk.END)
        X = []
        date1 = D.Date(self.year_select,self.month_select,self.day_select)
        for i in range(2,len(self.calendar.events)):
            if self.calendar.events[i].eventtiming.startdate == date1 or (self.calendar.events[i].eventtiming.startdate < date1 and self.calendar.events[i].eventtiming.enddate >= date1):
                X.append(self.calendar.events[i])
        day1 = DA.Day(date1,X)
        self.day_textbox.insert(tk.END,str(day1))

    '''
    The following methods are all the day navigation 
    methods for each day navigation button
    '''
    def day1(self):
        self.day_select = 1
        self.day_page()

    def day2(self):
        self.day_select = 2
        self.day_page()

    def day3(self):
        self.day_select = 3
        self.day_page()

    def day4(self):
        self.day_select = 4
        self.day_page()

    def day5(self):
        self.day_select = 5
        self.day_page()

    def day6(self):
        self.day_select = 6
        self.day_page()

    def day7(self):
        self.day_select = 7
        self.day_page()

    def day8(self):
        self.day_select = 8
        self.day_page()

    def day9(self):
        self.day_select = 9
        self.day_page()

    def day10(self):
        self.day_select = 10
        self.day_page()

    def day11(self):
        self.day_select = 11
        self.day_page()

    def day12(self):
        self.day_select = 12
        self.day_page()

    def day13(self):
        self.day_select = 13
        self.day_page()

    def day14(self):
        self.day_select = 14
        self.day_page()

    def day15(self):
        self.day_select = 15
        self.day_page()

    def day16(self):
        self.day_select = 16
        self.day_page()

    def day17(self):
        self.day_select = 17
        self.day_page()

    def day18(self):
        self.day_select = 18
        self.day_page()

    def day19(self):
        self.day_select = 19
        self.day_page()

    def day20(self):
        self.day_select = 20
        self.day_page()

    def day21(self):
        self.day_select = 21
        self.day_page()

    def day22(self):
        self.day_select = 22
        self.day_page()

    def day23(self):
        self.day_select = 23
        self.day_page()

    def day24(self):
        self.day_select = 24
        self.day_page()

    def day25(self):
        self.day_select = 25
        self.day_page()

    def day26(self):
        self.day_select = 26
        self.day_page()

    def day27(self):
        self.day_select = 27
        self.day_page()

    def day28(self):
        self.day_select = 28
        self.day_page()

    def day29(self):
        self.day_select = 29
        self.day_page()

    def day30(self):
        self.day_select = 30
        self.day_page()

    def day31(self):
        self.day_select = 31
        self.day_page()

    
MyGUI()
