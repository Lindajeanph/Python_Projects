import shutil
import os
import time
import sys
import datetime
import glob
from datetime import timedelta
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import pathlib

def getsource(self):
    ask = filedialog.askdirectory(title="Select a directory")
    self.entrysource.delete(0, END)
    self.entrysource.insert(END, ask)

def getdestination(self):
    retrieve = filedialog.askdirectory(title="Select the destination")
    self.entrydestination.delete(0, END)
    self.entrydestination.insert(END, retrieve)
    
    
def go(self):
    for i in a:
        a = os.listdir(source)
        b = os.path.join(source, i)
        c = datetime.datetime.now() - timedelta(hours=24)
        d = os.path.getmtime(b)
        e = datetime.datetime.fromtimestamp(d)
        if e >= c:
            shutil.move(b, destination)
            print(i)

def loadgui(self):
    #textbox label and button for source
    self.entrysource = tk.Entry(font= 40)
    self.entrysource.grid(row=0,column=2,rowspan=1,columnspan=1,padx=(30,40),pady=(40,0),sticky=N+W)

    self.b1_label=tk.Label(self.master, text="Choose directory")
    self.b1 = tk.Button(self.master, text="Choose directory", command=lambda:getsource(self))
    self.b1.grid(row=0,column=1,padx=(5,0),pady=(40,0),sticky=W)


    #textbox label button for destination
    self.entrydest = tk.Entry(font= 40)
    self.entrydest.grid(row=1,column=2,rowspan=1,columnspan=1,padx=(30,40),pady=(0,0),sticky=N+W)
    self.b2_label=tk.Label(self.master, text="Destination directory")                  
    self.b2 = tk.Button(self.master, text="Destination directory", command=lambda:getdestination(self))
    self.b2.grid(row=1,column=1,padx=(5,0),pady=(5,0),sticky=W)


    self.entrygo = tk.Entry(font=40)
    self.b3 = tk.Button(self.master, text="Initiate", command=lambda:go(self))
    self.b3.grid(row=2,column=1,padx=(5,0),pady=(5,0),sticky=W)

    self.b3.grid(row=3, column=3, padx=(10,0), pady=(20,0))
    
    

class ParentWindow(Frame):
   def __init__(self, master, *args, **kwargs):
       Frame.__init__(self, master, *args, **kwargs)

       #   define the master frame configuration
       self.master = master
       self.master.maxsize(800, 500)
       self.master.minsize(800, 500)
       self.master.title("Check for Files")
       self.master.config(bg="#333")
       self.master.protocol('WM_DELETE_WINDOW',
                            lambda: FileCheck_func.quit_message(self))

       
       #   Load in the GUI widgets from a separate module,
       loadgui(self)
    

if __name__=="__main__":
    root=tk.Tk()
    app=ParentWindow(root)
    root.mainloop()
    

    
    





    

    




