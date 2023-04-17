'''
This is V1 of the Calendar GUI
'''

import tkinter as tk

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




CalendarGUI()


  

'''label1 = tk.Label(xx,text='Calendar Display', font=('Arial', 18))
label1.pack(padx=10,pady=10)

textbox1 = tk.Text(xx,height=5, width=5,font=('Arial',14)) 
textbox1.pack(padx=10,pady=10)

entrybox = tk.Entry(xx)
entrybox.pack(padx=5)
button = tk.Button(xx,text='Save', font=('Helvetica',18))
button.pack(pady=40)

xx.mainloop()'''