'''
This is V1 of the Calendar GUI
'''

import tkinter as tk
import Classes_V2 as c
from tkinter import messagebox

class CalendarGUI:
    def __init__(self):
        self.xx = tk.Tk()
        self.xx.geometry('1200x800')
        self.xx.title('Calendar Window')

        self.menubar = tk.Menu(self.xx)
        self.filmenu = tk.Menu()

        self.label1 = tk.Label(self.xx, text='Calendar Name: ', font=('Arial',18))
        self.label1.place(x=30,y=10,height=20,width=200)
        self.textbox1 = tk.Text(self.xx, height=1, font=('Arial',16))
        self.textbox1.place(x=200,y=10,heigh=30,width=250)

        self.checkstate1 = tk.IntVar()

        self.check1 = tk.Checkbutton(self.xx, text='Show Calendar Name', font=('Arial',16), variable=self.checkstate1)
        self.check1.place(x=600,y=10, height=30, width=250)

        self.button1 = tk.Button(self.xx, text='Save', font=('Arial',16),command=self.show_message)
        self.button1.place(x=30,y=150,height=50,width=100)

        self.xx.protocol('WM_DELETE_WINDOW',self.on_closing)
 

        self.xx.mainloop()

    def show_message(self):
        if self.checkstate1.get()==0:
            print(self.textbox1.get('1.0',tk.END))
        else:
            messagebox.showinfo(title='Message', message=self.textbox1.get('1.0',tk.END))

    def on_closing(self):
        if messagebox.askyesno(title='Quit?', message='Are you sure you would like to exit?'):
            print('Closing Calendar . . .')
            print('Ending Program . . .')
            self.xx.destroy()


class MyGUI:
    def __init__(self):
        self.filename = ''
        self.year_select = 2023
        self.month_select = 0
        self.day_select = 0
        self.calendar = c.Calendar()
        self.startdate = c.Date(2023,12,31)

        self.calendar.years.append(c.Fill_Year())
        self.window = tk.Tk()
        self.window.title('CalendarNameVariable')
        self.window.geometry('800x500')

        self.frame1 = tk.Frame(self.window)
        self.frame2 = tk.Frame(self.window)
        self.frame3 = tk.Frame(self.window)
        self.frame4 = tk.Frame(self.window)
        self.frame7 = tk.Frame(self.window)

        # Frames for welcome page
        self.frame1.place(x=500,y=100)
        self.frame2.place(x=450,y=200)
        self.frame3.place(x=520,y=200)
        self.frame4.place(x=500,y=250)
        self.frame7.place(x=20,y=120)

        self.startwindow = []
        self.startwindow.append(self.frame1)
        self.startwindow.append(self.frame2)
        self.startwindow.append(self.frame3)
        self.startwindow.append(self.frame4)
        self.startwindow.append(self.frame7)



        self.frame11 = tk.Frame(self.window)
        self.frame12 = tk.Frame(self.window)
        self.frame13 = tk.Frame(self.window)

        

        self.frame11.place(x=350,y=100)
        self.frame12.place(x=494,y=100)
        self.frame13.place(x=638,y=100)

        self.frame23 = tk.Frame(self.window)

        self.frame23.place(x=10,y=10)

        self.frame41 = tk.Frame(self.window)
        self.frame42 = tk.Frame(self.window)
        self.frame43 = tk.Frame(self.window)
        self.frame44 = tk.Frame(self.window)
        self.frame41.place(x=360,y=50)
        self.frame42.place(x=450,y=50)
        self.frame43.place(x=700,y=50)
        self.frame44.place(x=530,y=20)


        self.events_frame = tk.LabelFrame(self.window,text='Events',background='Gray')
        
        self.events_label = tk.Text(self.events_frame,height=20,width=50,font=('Arial',10))
        self.events_label.pack()
        
        # self.events_label.insert(tk.END,stext)




        self.cname = tk.Label(self.frame23,height=1,width=35,text='Calendar Name:', font=('Arial', 16))
        self.cnametext = tk.Entry(self.frame23,width=20,font=('Arial', 14))
        self.cdesc = tk.Label(self.frame23,height=1,width=25,text='Calendar description:', font=('Arial', 16))
        self.cdesctext = tk.Text(self.frame23,height=5,width=45,font=('Arial', 12))

        self.cnametextsave = tk.Label(self.frame23,width=20,height=1,text=(self.calendar.name),font=('Arial', 14))
        self.cdesctextsave = tk.Label(self.frame23,width=45,height=5,text=(self.calendar.description),font=('Arial',12))


        self.cdetailssave = tk.Button(self.frame23,height=1,width=4, text='save',command=self.cdetails_save)
        self.cdetailsedit = tk.Button(self.frame23,height=1,width=4, text='edit',command=self.cdetails_edit)

        self.year_prev = tk.Button(self.frame41,height=2,width=4, text='prev',command=self.minus_year)
        self.year_next = tk.Button(self.frame43,height=2,width=4, text='next',command=self.plus_year)
        self.year_label = tk.Label(self.frame42,height=1,width=10,text=str(self.year_select), font=('Arial',40))

        self.mode_year = tk.Button(self.frame44,height=1,width=4,text='years',command=self.back_to_year)

        self.control_buttons = []
        self.control_buttons.append(self.year_next)
        self.control_buttons.append(self.year_prev)
        self.control_buttons.append(self.year_label)
 

        self.frame51 = tk.Frame(self.window)
        self.frame51.place(x=10,y=200)

        self.event_label = tk.Label(self.frame23,height=1,width=35,text='Events:', font=('Arial', 16))
        self.events_box = tk.Text(self.frame23,height=10,width=50,)

        self.ym_buttons = tk.Frame(self.window)


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


        self.day_button_frame = tk.Frame(self.window)
        self.day_buttons = []
        self.day_1 = tk.Button(self.day_button_frame,height=2,width=4, text='1st',font=('Arial', 16))
        self.day_2 = tk.Button(self.day_button_frame,height=2,width=4, text='2nd',font=('Arial', 16))
        self.day_3 = tk.Button(self.day_button_frame,height=2,width=4, text='3rd',font=('Arial', 16))
        self.day_4 = tk.Button(self.day_button_frame,height=2,width=4, text='4th',font=('Arial', 16))
        self.day_5 = tk.Button(self.day_button_frame,height=2,width=4, text='5th',font=('Arial', 16))
        self.day_6 = tk.Button(self.day_button_frame,height=2,width=4, text='6th',font=('Arial', 16))
        self.day_7 = tk.Button(self.day_button_frame,height=2,width=4, text='7th',font=('Arial', 16))
        self.day_8 = tk.Button(self.day_button_frame,height=2,width=4, text='8th',font=('Arial', 16))
        self.day_9 = tk.Button(self.day_button_frame,height=2,width=4, text='9th',font=('Arial', 16))
        self.day_10 = tk.Button(self.day_button_frame,height=2,width=4, text='10th',font=('Arial', 16))
        self.day_11 = tk.Button(self.day_button_frame,height=2,width=4, text='11th',font=('Arial', 16))
        self.day_12 = tk.Button(self.day_button_frame,height=2,width=4, text='12th',font=('Arial', 16))
        self.day_13 = tk.Button(self.day_button_frame,height=2,width=4, text='13th',font=('Arial', 16))
        self.day_14 = tk.Button(self.day_button_frame,height=2,width=4, text='14th',font=('Arial', 16))
        self.day_15 = tk.Button(self.day_button_frame,height=2,width=4, text='15th',font=('Arial', 16))
        self.day_16 = tk.Button(self.day_button_frame,height=2,width=4, text='16th',font=('Arial', 16))
        self.day_17 = tk.Button(self.day_button_frame,height=2,width=4, text='17th',font=('Arial', 16))
        self.day_18 = tk.Button(self.day_button_frame,height=2,width=4, text='18th',font=('Arial', 16))
        self.day_19 = tk.Button(self.day_button_frame,height=2,width=4, text='19th',font=('Arial', 16))
        self.day_20 = tk.Button(self.day_button_frame,height=2,width=4, text='20th',font=('Arial', 16))
        self.day_21 = tk.Button(self.day_button_frame,height=2,width=4, text='21st',font=('Arial', 16))
        self.day_22 = tk.Button(self.day_button_frame,height=2,width=4, text='22nd',font=('Arial', 16))
        self.day_23 = tk.Button(self.day_button_frame,height=2,width=4, text='23rd',font=('Arial', 16))
        self.day_24 = tk.Button(self.day_button_frame,height=2,width=4, text='24th',font=('Arial', 16))
        self.day_25 = tk.Button(self.day_button_frame,height=2,width=4, text='25th',font=('Arial', 16))
        self.day_26 = tk.Button(self.day_button_frame,height=2,width=4, text='26th',font=('Arial', 16))
        self.day_27 = tk.Button(self.day_button_frame,height=2,width=4, text='27th',font=('Arial', 16))
        self.day_28 = tk.Button(self.day_button_frame,height=2,width=4, text='28th',font=('Arial', 16))
        self.day_29 = tk.Button(self.day_button_frame,height=2,width=4, text='29th',font=('Arial', 16))
        self.day_30 = tk.Button(self.day_button_frame,height=2,width=4, text='30th',font=('Arial', 16))
        self.day_31 = tk.Button(self.day_button_frame,height=2,width=4, text='31st',font=('Arial', 16))

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

            

       # self.day_buttons = []
       # for i in range(42):
        #    self.day_buttons.append(tk.Button(self.frame1,height=2, width = 10, text='Create New File', font=('Arial', 16),command=self.nav_day))
        

        self.frame99 = tk.Frame(self.window)
        self.frame99.place(x=600,y=5)
        self.event_add = tk.Button(self.frame99,height=2,width=12,text='{ + } Add Event', font=('Arial', 14), command=self.add_event)
        

        self.frame61 = tk.LabelFrame(self.window,text='Add Event',background='Black')
        self.frame62 = tk.LabelFrame(self.frame61,text='Event Time',background='Gray')
        self.frame63 = tk.LabelFrame(self.frame61,text='Event Date',background='Gray')
        self.frame64 = tk.Frame(self.frame61,background='Gray')
        self.frame65 = tk.Frame(self.frame61,background='Gray')
        self.frame66 = tk.LabelFrame(self.frame61,text='',background='Gray')

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

        self.event_save = tk.Button(self.frame66,height=1,width=4,text='exit',font=('Arial',14),command=self.exit_event)
        self.event_save.grid(row=0,column=0)

        self.event_exit = tk.Button(self.frame66,height=1,width=4,text='exit',font=('Arial',14),command=self.exit_event)
        self.event_exit.grid(row=0,column=1)



        self.event_de = tk.Label(self.frame65, height=1, width=20, text='Event Description: ',font=('Arial', 14))
        self.event_de.pack()
        self.event_desc = tk.Text(self.frame65,height=3, width=40, font=('Arial', 12))
        self.event_desc.pack()

  




        
        self.eventwindow = []
        self.eventwindow.append(self.frame64)
        self.eventwindow.append(self.frame65)
        self.eventwindow.append(self.frame62)
        self.eventwindow.append(self.frame63)
        self.eventwindow.append(self.frame66)




        




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
        introtext = ''
        introtext += 'Enter a filename to get started\n\n'
        introtext += 'Close the window to save your\n'
        introtext += 'calendar when you are done\n\n'
        introtext += 'Enjoy!'

        self.introduction = tk.Label(self.frame7,text=introtext,font=('Arial', 16))
        self.introduction.pack(padx=5,pady=5)
                                    


    
        self.window.protocol('WM_DELETE_WINDOW',self.on_closing)


        self.submit_button = tk.Button(self.window, height=20, width = 50)


        self.window.mainloop()

    def nav_jan(self):
        for x in self.day_buttons:
            x.grid_forget()
        self.mode_year.pack()
        self.month_select = 1
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()
        self.ym_buttons.place_forget()
        x = c.Day_Of_Week(c.Date(self.year_select,self.month_select,1))
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
        x = c.Day_Of_Week(c.Date(self.year_select,self.month_select,1))
        for i in range(31):
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
        x = c.Day_Of_Week(c.Date(self.year_select,self.month_select,1))
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
        x = c.Day_Of_Week(c.Date(self.year_select,self.month_select,1))
        for i in range(31):
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
        x = c.Day_Of_Week(c.Date(self.year_select,self.month_select,1))
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
        x = c.Day_Of_Week(c.Date(self.year_select,self.month_select,1))
        for i in range(31):
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
        x = c.Day_Of_Week(c.Date(self.year_select,self.month_select,1))
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
        x = c.Day_Of_Week(c.Date(self.year_select,self.month_select,1))
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
        x = c.Day_Of_Week(c.Date(self.year_select,self.month_select,1))
        for i in range(31):
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
        x = c.Day_Of_Week(c.Date(self.year_select,self.month_select,1))
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
        x = c.Day_Of_Week(c.Date(self.year_select,self.month_select,1))
        for i in range(31):
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
        x = c.Day_Of_Week(c.Date(self.year_select,self.month_select,1))
        for i in range(31):
            m = (i  + x) % 7
            n = (i + x) // 7
            self.day_buttons[i].grid(row=n,column=m)
        self.day_button_frame.place(x=300,y=100)


    
    def cdetails_save(self):
        self.calendar.name = self.cnametext.get()
        self.calendar.description = self.cdesctext.get('1.0',tk.END)
        self.cname.pack_forget()
        self.cnametext.pack_forget()
        self.cdesc.pack_forget()
        self.cdesctext.pack_forget()
        self.cdetailssave.pack_forget()
        self.cnametextsave = tk.Label(self.frame23,width=20,height=1,text=(self.calendar.name),font=('Arial', 14))
        self.cdesctextsave = tk.Label(self.frame23,width=30,height=7,text=(self.calendar.description),font=('Arial',12))
        self.cname.pack()
        self.cnametextsave.pack()
        self.cdesc.pack()
        self.cdesctextsave.pack()
        self.cdetailsedit.pack()


    def cdetails_edit(self):
        self.cname.pack_forget()
        self.cnametextsave.pack_forget()
        self.cdesc.pack_forget()
        self.cdesctextsave.pack_forget()
        self.cdetailsedit.pack_forget()
        self.cnametextsave = tk.Label(self.frame23,width=20,height=1,text=(self.calendar.name),font=('Arial', 14))
        self.cdesctextsave = tk.Label(self.frame23,width=30,height=7,text=(self.calendar.description),font=('Arial',12))
        self.cname.pack()
        self.cnametext.pack()
        self.cdesc.pack()
        self.cdesctext.pack()
        self.cdetailssave.pack()


    def save_event(self):

        for x in self.eventwindow:
            x.pack_forget()
        self.frame61.place_forget()

    def exit_event(self):
        
        for x in self.eventwindow:
            x.pack_forget()
        self.frame61.place_forget()


    def add_event(self):
        self.frame61.place(x=250,y=100)
        for x in self.eventwindow:
            x.pack()

    def load_file(self):
        filename = self.create_filename.get()
        self.filename = filename
        if filename[-4:] == '.dat':
            self.calendar.load(filename)
            print(self.calendar.description)
            messagebox.showinfo(title='Loading . . .',message="Calendar Loaded!")
            for x in self.startwindow:
                x.destroy()
            for y in self.control_buttons:
                y.pack()
            self.ym_buttons.place(x=350,y=100)
            self.event_add.pack()
            self.cnametextsave = tk.Label(self.frame23,width=20,height=1,text=(self.calendar.name),font=('Arial', 14))
            self.cdesctextsave = tk.Label(self.frame23,width=30,height=7,text=(self.calendar.description),font=('Arial',12))
            self.cname.pack()
            self.cnametextsave.pack()
            self.cdesc.pack()
            self.cdesctextsave.pack()
            self.cdetailsedit.pack() 
            self.events_frame.place(x=5,y=220)
        else:
            messagebox.showinfo(title='ERROR',message="Filename must end in '.dat'")



    def create_file(self):
        filename = self.create_filename.get()
        self.filename = filename
        if filename[-4:] == '.dat':
            self.calendar.save(filename)
            messagebox.showinfo(title='Saving . . .',message="Calendar Created!")
            for x in self.startwindow:
                x.destroy()
            for y in self.control_buttons:
                y.pack()
            self.ym_buttons.place(x=350,y=100)
            self.event_add.pack()
            self.cname.pack()
            self.cnametextsave.pack()
            self.cdesc.pack()
            self.cdesctextsave.pack()
            self.cdetailsedit.pack()
            self.events_frame.place(x=5,y=220)
        else:
            messagebox.showinfo(title='ERROR',message="Filename must end in '.dat'")


    def plus_year(self):
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
            x = c.Day_Of_Week(c.Date(self.year_select,self.month_select,1))
            for i in range(31):
                m = (i  + x) % 7
                n = (i + x) // 7
                self.day_buttons[i].grid(row=n,column=m)
            self.day_button_frame.place(x=300,y=100)


    def minus_year(self):
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
            x = c.Day_Of_Week(c.Date(self.year_select,self.month_select,1))
            for i in range(31):
                m = (i  + x) % 7
                n = (i + x) // 7
                self.day_buttons[i].grid(row=n,column=m)
            self.day_button_frame.place(x=300,y=100)
    
    def back_to_year(self):
        self.day_button_frame.place_forget()
        self.month_select = 0
        self.mode_year.pack_forget()
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.year_select), font=('Arial',40))
        self.year_label.pack()
        self.ym_buttons.place(x=350,y=100)





    def on_closing(self):
        if messagebox.askyesno(title='Quit?', message='Are you sure you would like to exit?'):
            if messagebox.askyesno(title='Save?', message='Would you like to save changes?'):
                self.calendar.save(self.filename)
                self.window.destroy()
            else:
                self.window.destroy()

  
MyGUI()

'''label1 = tk.Label(xx,text='Calendar Display', font=('Arial', 18))
label1.pack(padx=10,pady=10)

textbox1 = tk.Text(xx,height=5, width=5,font=('Arial',14)) 
textbox1.pack(padx=10,pady=10)

entrybox = tk.Entry(xx)
entrybox.pack(padx=5)
button = tk.Button(xx,text='Save', font=('Helvetica',18))
button.pack(pady=40)

xx.mainloop()'''