import tkinter as tk
from tkinter import *
from tkinter import ttk, Frame, PhotoImage, Label, LabelFrame, Button, Entry
import sqlite3
from tkcalendar import Calendar
    
    
class ChessPlayerFrame(Frame):
    def __init__(self, master, name="Mon nom"):
        Frame.__init__(self)
        
    #def ChessPlayerFrame(tab1):
        
        photo = PhotoImage(file='icons/knight-horse-chess-player.gif')

        label_fram1 = LabelFrame(master, text= 'Créer un nouveau joueur')
        label_fram1.grid(row=0, column=1, padx=8,pady=0, sticky='ew')

        label = Label(label_fram1, image=photo)
        label.image = photo
        label.grid(row=0, column=0,sticky=W )
        self.text_name = name
        Label(label_fram1, text=self.text_name).grid(row=1, column=1, sticky=W, pady=2)
        self.name= StringVar()
        self.namefield = Entry(label_fram1, textvariable=self.name)
        self.namefield.grid(row=1, column=2, sticky=W, padx=5, pady=2)


class ChessMaster:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Python GUI")
        self.createWidgets()
        #self.ChessPlayerFrame()

    def createWidgets(self):
        tabControl = ttk.Notebook(self.win)
        
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text='Tab 1')
        
        ChessPlayerFrame(tab1)
                
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text='Tab 2')
        
        tab3 = ttk.Frame(tabControl)
        
        tabControl.add(tab3, text='Tab 3')

        
        #tabControl.pack(expand=1, fill="both")
        tabControl.grid(sticky='W')


#def player_form(frame):


root = ChessMaster()

root.win.mainloop()