
from ast import Continue
import math
import random
import numpy as np
import tkinter as Tk
#from graphMode import graphMode
from tkinter import * 
from tkinter.ttk import * 
from tkinter.filedialog import *
from mode import *
from main import *
class sketchpad(mode):
    def createCircles(self,event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        w.create_oval(x1,y1,x2,y2,fill="red", width=5)

    def __init__(self,master=None):
        master=master
        w.unbind("<B1-Motion>",paint)
        