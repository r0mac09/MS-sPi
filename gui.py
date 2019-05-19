import tkinter as tk
import board

from tkinter import *

ON = 1
OFF = 0

class GUI:
    def __init__(self):

        self.status = OFF
        self.window = tk.Tk()
        self.window.title('sPi Camera system')
        self.window.geometry('350x120')

        self.startButton = Button(self.window, text='Start', font=('Helvetica', 12), bg='light blue', fg='white', command=self.initBoard, state=tk.NORMAL)
        self.startButton.grid(column=0, row=0)

        self.stopButton = Button(self.window, text='Stop', font=('Helvetica', 12), bg='red', fg='white', command=self.killBoard, state=tk.DISABLED)
        self.stopButton.grid(column=0, row=1)

        self.awayTimeEntry = Entry(self.window, width=5)
        self.awayTimeEntry.grid(column=1, row=0)

        self.awayButton = Button(self.window, text='Away', font=('Helvetica', 12), bg='light blue', fg='white', command=self.set_away, state=tk.DISABLED)
        self.awayButton.grid(column=2, row=0)

        self.window.mainloop()

    def initBoard(self):
        self.startButton['state'] = tk.DISABLED
        self.stopButton['state'] = tk.NORMAL
        self.awayButton['state'] = tk.NORMAL

        status = ON
        board.setup()

    def killBoard(self):
        self.stopButton['state'] = tk.DISABLED
        self.awayButton['state'] = tk.DISABLED
        self.startButton['state'] = tk.NORMAL
        status = OFF
        board.kill()

    def set_away(self):
        raise NotImplementedError
    

GUI()