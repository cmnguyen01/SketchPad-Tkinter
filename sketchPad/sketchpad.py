
from ast import Continue
import math
import random
import numpy as np
import tkinter as Tk
from tkinter import * 
from tkinter.ttk import * 
from abc import ABC, abstractmethod
class Shape:
    def __init__(self, master = None):
        self.master = master
         
        # Calls create method of class Shape
        self.create()


class sketchpad:
    
    def __init__(self,master=None):
        
        self.master=master
        
        #w=self.canvas(master)
        root=Tk()
        root.title("Sketchpad")
        root.geometry("500x500")
        #menu
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.donothing)
        filemenu.add_command(label="Open", command=self.donothing)
        filemenu.add_command(label="Save", command=self.donothing)
        filemenu.add_command(label="Save as...", command=self.donothing)
        filemenu.add_command(label="Close", command=root.destroy)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=self.donothing)

        editmenu.add_separator()

        editmenu.add_command(label="Cut", command=self.donothing)
        editmenu.add_command(label="Copy", command=self.donothing)
        editmenu.add_command(label="Paste", command=self.donothing)
        editmenu.add_command(label="Delete", command=self.donothing)
        editmenu.add_command(label="Select All", command=self.donothing)

        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
        root.config(menu=menubar)
        #buttons
        shapeButton=Button(root, text="Shape")
        shapeButton.pack()
        handButton=Button(root, text="Hand")
        handButton.pack()
        graphButton=Button(root, text="Hand")
        graphButton.pack()
        
        
      
    def donothing(self):
        filewin = Toplevel(self.root)
    def save(self):
        pass

class Mode(ABC):
    def __init__(self) -> None:
        pass
class shapeMode(Mode):
    def __init__(self) -> None:
        pass
class graphMode(Mode):
    def __init__(self)-> None:
        pass
class handMode(Mode):
    def __init__(self):
        pass

if __name__ == "__main__":
    #since the gui is the sketchpad i made the main open the sketchpad
    master=sketchpad()
    mainloop()