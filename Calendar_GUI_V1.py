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
        self.calendar = c.Calendar
        self.window = tk.Tk()
        self.window.title('CalendarNameVariable')
        self.window.geometry('800x500')

        self.frame1 = tk.Frame(self.window)
        self.frame2 = tk.Frame(self.window)
        self.frame3 = tk.Frame(self.window)
        self.frame4 = tk.Frame(self.window)
        self.frame5 = tk.Frame(self.window)
        self.frame6 = tk.Frame(self.window)

        # Frames for welcome page
        self.frame1.place(x=300,y=100)
        self.frame2.place(x=250,y=200)
        self.frame3.place(x=320,y=200)
        self.frame4.place(x=300,y=250)
        self.frame5.place(x=250,y=350)
        self.frame6.place(x=320,y=350)

        self.frame11 = tk.Frame(self.window)
        self.frame12 = tk.Frame(self.window)
        self.frame13 = tk.Frame(self.window)

        self.frame11.place(x=300,y=100)
        self.frame12.place(x=450,y=100)
        self.frame13.place(x=600,y=100)

        self.ym_buttons = []
        for j in range(3):
            for i in range(4):
                if j == 0:
                    self.ym_buttons.append(tk.Button(self.frame11,height=3, width = 12, text='Create New File', font=('Arial', 16),command=self.nav_month))
                elif j == 1:
                    self.ym_buttons.append(tk.Button(self.frame12,height=3, width = 12, text='Create New File', font=('Arial', 16),command=self.nav_month))
                elif j == 2:
                    self.ym_buttons.append(tk.Button(self.frame13,height=3, width = 12, text='Create New File', font=('Arial', 16),command=self.nav_month))



        self.day_buttons = []
        for i in range(42):
            self.day_buttons.append(tk.Button(self.frame1,height=2, width = 10, text='Create New File', font=('Arial', 16),command=self.nav_day))
        
        


        self.create_file_button = tk.Button(self.frame1,height=3, width = 16, text='Create New File', font=('Arial', 16),command=self.create_file)
        self.create_file_button.pack()
        self.create_file_label = tk.Label(self.frame2,text = 'filename:', font=('Arial', 16))
        self.create_file_label.pack()
        self.create_filename = tk.Entry(self.frame3, width = 20)
        self.create_filename.pack()
        self.load_file_button = tk.Button(self.frame4,height=3, width = 16, text='Load Old File', font=('Arial', 16),command=self.load_file)
        self.load_file_button.pack()
        self.create_file_label = tk.Label(self.frame5, text = 'filename:', font=('Arial', 16))
        self.create_file_label.pack()
        self.load_filename = tk.Entry(self.frame6, width = 20)
        self.load_filename.pack()
        #self.frame = tk.Frame(self.window)
        #elf.frame.pack()
        self.window.protocol('WM_DELETE_WINDOW',self.on_closing)

        #self.event_edit_frame.grid(row=0,column=0)


        self.submit_button = tk.Button(self.window, height=20, width = 50)


        self.window.mainloop()

    

    def nav_month(self,date=c.Date):
        print('month')
    
    def nav_day(self, date=c.Date): 
        print('day')

    

    def load_file(self):
        filename = self.load_filename.get()
        if filename[-4:] == '.dat':
            messagebox.showinfo(title='ERROR',message="well done")
            self.frame1.pack_forget()
            self.frame2.pack_forget()
            self.frame3.pack_forget()
            self.frame4.pack_forget()
            self.frame5.pack_forget()
            self.frame6.pack_forget()
            # self.calendar.load(filename)
            for x in self.ym_buttons:
                x.pack()
                
        else:
            messagebox.showinfo(title='ERROR',message="Filename must end in '.dat'")



    def create_file(self):
        filename = self.create_filename.get()
        if filename[-4:] == '.dat':
            messagebox.showinfo(title='ERROR',message="well done")
            self.frame1.destroy()
            self.frame2.destroy()
            self.frame3.destroy()
            self.frame4.destroy()
            self.frame5.destroy()
            self.frame6.destroy()
            # self.calendar.save(filename)
            for x in self.ym_buttons:
                x.pack()
        else:
            messagebox.showinfo(title='ERROR',message="Filename must end in '.dat'")





    def on_closing(self):
        if messagebox.askyesno(title='Quit?', message='Are you sure you would like to exit?'):
            if messagebox.askyesno(title='Save?', message='Would you like to save changes?'):
                print('Saving Calendar . . .')
                # insert save function
                print('Calendar Saved!')
                self.window.destroy()
            else:
                print('Closing Calendar . . .')
                print('Ending Program . . .')
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