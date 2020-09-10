import shutil
import os
import time
import sys
import datetime
import glob
from datetime import timedelta
import tkinter as tk
destination = 'C:/Users/bposs/Documents/MonitoredFiles/'
source = 'C:/Users/bposs/Documents/DailyFiles/'

    #a list of files
a = os.listdir(source)

for i in a:
    b = os.path.join(source, i)
    c = datetime.datetime.now() - timedelta(hours=24)
    d = os.path.getmtime(b)
    e = datetime.datetime.fromtimestamp(d)
    if e >= c:
        shutil.move(b, destination)
        print(i)

from tkinter import *
win = Tk()
b1 = Button(win, text="Check files")
b2 = Button(win, text="Copy Files")
b3 = Button(win, text="Initiate")
b1.pack(side=LEFT, padx = 20)
b2.pack(side=LEFT, padx = 20)
b3.pack(side=LEFT, padx = 20)

HEIGHT = 700
WIDTH= 800

#check files
def but1():
    print(a)
b1.configure(command=but1)
    #Copy files
def but2():
    print(destination)
b2.configure(command=but2)

    #Initiate
def but3():
    print(i)
b3.configure(command=but3)


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#cce6ff')
frame.place(relx=0.1, rely= 0.1, relwidth=0.8, relheight=0.8)

b1 = tk.Button(frame, text="Check files", command=but1)
b1.pack(side='left', padx = 20)
                   
b2 = tk.Button(frame, text="Copy Files", command=but2)
b2.pack(side='left', padx = 20)

b3 = tk.Button(frame, text="Initiate", command=but3)
b3.pack(side='left', padx = 20)



label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)
root.mainloop()


root.mainloop()



       
    




