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


class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('CalendarNameVariable')
        self.window.geometry('800x600')
        self.create_file_button = tk.Button(self.window,height=40, width = 80, text='Create New File', font=('Arial', 16))
        self.create_file_button.pack(padx=10,pady=10)
        self.create_filename = tk.Entry(self.window, height = 10, width = 100)
        self.create_filename.pack(padx=10,pady=10)
        self.load_file_button = tk.Button(self.window,height=40, width = 80, text='Load Old File', font=('Arial', 16))
        self.load_file_button.pack(padx=10,pady=10)
        self.load_filename = tk.Entry(self.window, height = 10, width = 100)
        self.load_filename.pack(padx=10,pady=10)
        #self.frame = tk.Frame(self.window)
        #elf.frame.pack()
        self.window.protocol('WM_DELETE_WINDOW',self.on_closing)

        #self.event_edit_frame.grid(row=0,column=0)


        self.submit_button = tk.Button(self.window, height=20, width = 50)


        self.window.mainloop()

    def on_closing(self):
        if messagebox.askyesno(title='Quit?', message='Are you sure you would like to exit?'):
            if messagebox.askyesno(title='Save?', message='Would you like to save changes?'):
                print('Saving Calendar . . .')
                # insert save function
                print('Calendar Saved!')
            else:
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