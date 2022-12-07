
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
        self.root=Tk()
        self.root.geometry("500x500")
        self.menubar = Menu(self.root)
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="New")
        filemenu.add_command(label="Open", command=self.donothing)
        filemenu.add_command(label="Save", command=self.donothing)
        filemenu.add_command(label="Save as...", command=self.donothing)
        filemenu.add_command(label="Close", command=self.donothing)
        filemenu.add_cascade(label="File", menu=filemenu)
        shapeButton=Button(self.root, text="Shape")
        shapeButton.pack()
        handButton=Button(self.root, text="Hand")
        handButton.pack()
        graphButton=Button(self.root, text="Hand")
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