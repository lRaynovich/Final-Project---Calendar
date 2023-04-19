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

        self.ym_buttons = []

        for j in range(12):
            if j == 0:
                self.ym_buttons.append(tk.Button(self.frame11,height=3, width = 12, text='January', font=('Arial', 16),command=self.nav_jan))
            elif j == 3:
                self.ym_buttons.append(tk.Button(self.frame11,height=3, width = 12, text='April', font=('Arial', 16),command=self.nav_apr))
            elif j == 6:
                self.ym_buttons.append(tk.Button(self.frame11,height=3, width = 12, text='July', font=('Arial', 16),command=self.nav_jul))
            elif j ==9:
                self.ym_buttons.append(tk.Button(self.frame11,height=3, width = 12, text='October', font=('Arial', 16),command=self.nav_oct))
            elif j == 1:
                self.ym_buttons.append(tk.Button(self.frame12,height=3, width = 12, text='February', font=('Arial', 16),command=self.nav_feb))
            elif j == 4:
                self.ym_buttons.append(tk.Button(self.frame12,height=3, width = 12, text='May', font=('Arial', 16),command=self.nav_may))
            elif j == 7:
                self.ym_buttons.append(tk.Button(self.frame12,height=3, width = 12, text='August', font=('Arial', 16),command=self.nav_aug))
            elif j == 10:
                self.ym_buttons.append(tk.Button(self.frame12,height=3, width = 12, text='November', font=('Arial', 16),command=self.nav_nov))
            elif j ==2:
                self.ym_buttons.append(tk.Button(self.frame13,height=3, width = 12, text='March', font=('Arial', 16),command=self.nav_mar))
            elif j ==5:
                self.ym_buttons.append(tk.Button(self.frame13,height=3, width = 12, text='June', font=('Arial', 16),command=self.nav_jun))
            elif j ==8:
                self.ym_buttons.append(tk.Button(self.frame13,height=3, width = 12, text='September', font=('Arial', 16),command=self.nav_sep))
            elif j ==11:
                self.ym_buttons.append(tk.Button(self.frame13,height=3, width = 12, text='December', font=('Arial', 16),command=self.nav_dec))


            

       # self.day_buttons = []
       # for i in range(42):
        #    self.day_buttons.append(tk.Button(self.frame1,height=2, width = 10, text='Create New File', font=('Arial', 16),command=self.nav_day))
        

        self.frame99 = tk.Frame(self.window)
        self.frame99.place(x=600,y=10)
        self.event_add = tk.Button(self.frame99,height=2,width=6,text='{ + } Add Event', font=('Arial', 14), command=self.add_event)
        

        self.frame61 = tk.Frame(self.window)
        self.frame61.place(x=300,y=300)
        self.frame62 = tk.Frame(self.frame61)
        self.frame63 = tk.Frame(self.frame61)
        self.frame64 = tk.Frame(self.frame61)
        self.frame65 = tk.Frame(self.frame61)
        
        self.eventwindow = []
        self.eventwindow.append(self.frame61)
        self.eventwindow.append(self.frame62)
        self.eventwindow.append(self.frame63)
        self.eventwindow.append(self.frame64)
        self.eventwindow.append(self.frame65)

        




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
        self.mode_year.pack()
        self.month_select = 1
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()

    def nav_feb(self):
        self.mode_year.pack()
        self.month_select = 2
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()

    def nav_mar(self):
        self.mode_year.pack()
        self.month_select = 3
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()

    def nav_apr(self):
        self.mode_year.pack()
        self.month_select = 4
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()

    def nav_may(self):
        self.mode_year.pack()
        self.month_select = 5
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()

    def nav_jun(self):
        self.mode_year.pack()
        self.month_select = 6
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()

    def nav_jul(self):
        self.mode_year.pack()
        self.month_select = 7
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()

    def nav_aug(self):
        self.mode_year.pack()
        self.month_select = 8
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()

    def nav_sep(self):
        self.mode_year.pack()
        self.month_select = 9
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()

    def nav_oct(self):
        self.mode_year.pack()
        self.month_select = 10
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()

    def nav_nov(self):
        self.mode_year.pack()
        self.month_select = 11
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()

    def nav_dec(self):
        self.mode_year.pack()
        self.month_select = 12
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
        self.year_label.pack()


    
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


    def add_event(self):
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
            # self.calendar.load(filename)
            for x in self.ym_buttons:
                x.pack()
            self.frame99.pack()

            self.cnametextsave = tk.Label(self.frame23,width=20,height=1,text=(self.calendar.name),font=('Arial', 14))
            self.cdesctextsave = tk.Label(self.frame23,width=30,height=7,text=(self.calendar.description),font=('Arial',12))
            self.cname.pack()
            self.cnametextsave.pack()
            self.cdesc.pack()
            self.cdesctextsave.pack()
            self.cdetailsedit.pack() 
        else:
            messagebox.showinfo(title='ERROR',message="Filename must end in '.dat'")



    def create_file(self):
        filename = self.create_filename.get()
        self.filename = filename
        if filename[-4:] == '.dat':
            self.calendar.save(filename)
            messagebox.showinfo(title='Saving . . .',message="Calendar Created!")
            self.frame99.pack()
            for x in self.startwindow:
                x.destroy()
            for y in self.control_buttons:
                y.pack()

            for x in self.ym_buttons:
                x.pack()
            self.cname.pack()
            self.cnametextsave.pack()
            self.cdesc.pack()
            self.cdesctextsave.pack()
            self.cdetailsedit.pack()
        else:
            messagebox.showinfo(title='ERROR',message="Filename must end in '.dat'")


    def plus_year(self):
        if self.month_select == 0:
            self.year_select += 1
            self.year_label.pack_forget()
            self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.year_select), font=('Arial',40))
            self.year_label.pack()
        else:
            if self.month_select == 12:
                self.month_select = 1
                self.year_select += 1
            else:
                self.month_select += 1
            self.year_label.pack_forget()
            self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
            self.year_label.pack()
        

    def minus_year(self):
        if self.month_select == 0:
            self.year_select -= 1
            self.year_label.pack_forget()
            self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.year_select), font=('Arial',40))
            self.year_label.pack()
        else:
            if self.month_select == 1:
                self.month_select = 12
                self.year_select -= 1
            else:
                self.month_select -= 1
            self.year_label.pack_forget()
            self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.month_select)+'/'+str(self.year_select), font=('Arial',40))
            self.year_label.pack()
    
    def back_to_year(self):
        self.month_select = 0
        self.mode_year.pack_forget()
        self.year_label.pack_forget()
        self.year_label = tk.Label(self.frame42,height=1,width=6,text=str(self.year_select), font=('Arial',40))
        self.year_label.pack()



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