import tkinter as tk
import board
import recognizer
import sched
from tkinter import *
from logger import log
ON = 1
OFF = 0

class GUI:
    def __init__(self):
        log('User interface is initializing ...')
        self.status = OFF
        self.window = tk.Tk()
        self.window.title('sPi Camera system')
        self.window.geometry('350x120')

        self.startButton = Button(self.window, text='Start', font=('Helvetica', 12), bg='light blue', fg='white', command=self.init, state=tk.NORMAL)
        self.startButton.grid(column=0, row=0)

        self.stopButton = Button(self.window, text='Stop', font=('Helvetica', 12), bg='red', fg='white', command=self.kill, state=tk.DISABLED)
        self.stopButton.grid(column=0, row=1)

        self.awayTimeEntry = Entry(self.window, width=5)
        self.awayTimeEntry.grid(column=1, row=0)

        self.awayButton = Button(self.window, text='Away', font=('Helvetica', 12), bg='light blue', fg='white', command=self.set_away, state=tk.DISABLED)
        self.awayButton.grid(column=2, row=0)

        log('Starting Raspberry functions ...')
        board.setup()

        log('Window will appear after recognizer initializes')
        self.recog = recognizer.Recognizer()

        
        self.window.mainloop()

    def init(self):
        self.startButton['state'] = tk.DISABLED
        self.stopButton['state'] = tk.NORMAL
        self.awayButton['state'] = tk.NORMAL

        self.status = ON
        log('Starting recognizer ...')
        self.recog.start()

    def kill(self):
        self.stopButton['state'] = tk.DISABLED
        self.awayButton['state'] = tk.DISABLED
        self.startButton['state'] = tk.NORMAL
        self.status = OFF
        self.recognizer.kill()
        board.kill()

    def set_away(self):
        raise NotImplementedError
    

GUI()