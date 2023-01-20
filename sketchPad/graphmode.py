from asyncio.windows_events import NULL
import networkx as nx
import tkinter as Tk
from tkinter import *
from main import *
from mode import *
class graph():
    global nodeDictionary
    def __init__(self):
        self.nodeDictionary={}
    def addNodes(self,node1,node2):
        if(self.nodeDictionary.get(node1)==NULL):
            self.nodeDictionary[node1]=node2
        else:
            self.nodeDictionary.update(g.nodeDictionary.get(node1),node2)
            
class graphmode(mode):
    global g
    g=graph()
    def __init__(self,master=None):
        master=master
        w.unbind("<B1-Motion>",paint)
        
    def draw():
        pass
        #w.bind(<"mouse")
    


class node():
    global g
    g=graph()
    def __init__(self,value,x,y):
        value=value
        x=x
        y=y
    #create and draw node on canvas
    def createNode(event, color,value):
        x1, y1 = (event.x - 1), (event.y - 1)
        n=node(value,x1,y1)
        if(color==NULL):
            #if there was no color selected
            w.create_oval(x1,y1,fill="white", width=5)
            w.create_text(x1,y1,text=value)
        else:
            #if there was a color selected
            w.create_oval(x1,y1,fill=color, width=5)
            #add the value to the node
            w.create_text(x1,y1,text=value)
