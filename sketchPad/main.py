
from ast import Continue
import math
import random
import numpy as np
import tkinter as Tk
from graphmode import *
from tkinter import * 
from tkinter.ttk import * 
from tkinter.filedialog import *

def donothing(self):
    filewin = Toplevel(self.root)
def save_as(self):
    f = asksaveasfile(initialfile = 'Untitled.jpeg',
    defaultextension=".jpeg",filetypes=[("All Files","*.*"),("jpeg","*.jpeg")])
def open(self):
    f=askopenfile()
def new(self):
    w.delete('all')
def graphButton_Press(self,event):
    w.delete('all')
    w.bind("<ButtonRelease>", self.createCircles)
    w.unbind("<B1-motion>",self.paint)
def paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    w.create_oval(x1,y1,x2,y2,fill="black", width=0)

if __name__ == "__main__":
    #since the gui is the sketchpad i made the main open the sketchpad
    root=Tk()
    root.title("Sketchpad")
    root.geometry("500x500")
    global w
        
        #menu
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=new)
    filemenu.add_command(label="Open", command=open)
    filemenu.add_command(label="Save", command=save_as)
    filemenu.add_command(label="Save as...", command=save_as)
    filemenu.add_command(label="Close", command=root.destroy)
    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=donothing)
        
    editmenu.add_separator()

    editmenu.add_command(label="Cut", command=donothing)
    editmenu.add_command(label="Copy", command=donothing)
    editmenu.add_command(label="Paste", command=donothing)
    editmenu.add_command(label="Delete", command=donothing)
    editmenu.add_command(label="Select All", command=donothing)

    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)
    root.config(menu=menubar)
        
        #buttons
    graphButton=Button(root, text="Graph")
    graphButton.bind("<Button-1>", graphButton_Press)
    graphButton.pack()
        #canvas
    w=Canvas(root, bg="white",height=400, width=500)
    w.pack(expand=YES, fill=BOTH)
    w.bind("<B1-Motion>",paint)
    #master=sketchpad()
    mainloop()