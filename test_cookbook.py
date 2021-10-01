import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu, Radiobutton


class OOP():

    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Python GUI")
        self.createWidgets()

    def createWidgets(self):
        tabControl = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text='Tab 1')
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text='Tab 2')
        tab3 = ttk.Frame(tabControl)
        tabControl.add(tab3, text='Tab 3')
        tabControl.pack(expand=1, fill="both")

        self.monty = ttk.LabelFrame(tab1, text=' Monty Python ')
        self.monty.grid(column=0, row=0, padx=8, pady=4)
        
        self.monty2 = ttk.LabelFrame(tab2, text=' Monty Python2 ')
        self.monty2.grid(column=0, row=0, padx=8, pady=4)

        ttk.Label(
            self.monty,
            text="Enter a name:").grid(column=0, row=0, sticky='W')
        self.name = tk.StringVar()
        nameEntered = ttk.Entry(self.monty, width=12, textvariable=self.name)
        nameEntered.grid(column=0, row=1, sticky='W')
        self.action = ttk.Button(self.monty, text="Click Me!")
        self.action.grid(column=2, row=1)
        
        ttk.Label(
            self.monty2,
            text="Enter a big name:").grid(column=0, row=0, sticky='W')
        self.name = tk.StringVar()
        nameEntered = ttk.Entry(self.monty2, width=12, textvariable=self.name)
        nameEntered.grid(column=0, row=1, sticky='W')
        self.action = ttk.Button(self.monty2, text="Click Me!")
        self.action.grid(column=2, row=1)
        ttk.Label(self.monty, text="Choose a number:").grid(column=1, row=0)
        number = tk.StringVar()
        numberChosen = ttk.Combobox(self.monty, width=12, textvariable=number)
        numberChosen['values'] = ("Bullet", "Blitz", "Coups rapide")
        numberChosen.grid(column=1, row=1)
        numberChosen.current(1)

        scrolW = 30
        scrolH = 3
        self.scr = scrolledtext.ScrolledText(self.monty, width=scrolW, height=scrolH, wrap=tk.WORD)
        self.scr.grid(column=0, row=3, sticky='WE', columnspan=3)
        
        menuBar = Menu(tab1)
        self.win.config(menu=menuBar)
        fileMenu = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="File", menu=fileMenu)
        helpMenu = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Help", menu=helpMenu)
        nameEntered.focus()

        stylePoliceFr =["Normal", "Gras", "Italique", "Gras/Italique"]
        stylePoliceTk =["normal", "bold", "italic" , "bold italic"]
        # Le style actuel est mémorisé dans un 'objet-variable' tkinter ;
        self.choixPolice = tk.StringVar()
        self.choixPolice.set(stylePoliceTk[0])
        # Création des quatre 'boutons radio' :
        
        for n in range(4):
            r_bout = Radiobutton(self.monty2,
            text = stylePoliceFr[n],
            variable = self.choixPolice,
            value = stylePoliceTk[n])
            #command = self.changePolice)
            r_bout.grid(column=n, row=4, sticky='W')
        """"   
        r_bout2 = Radiobutton(self.monty2,
            text = stylePoliceFr[2],
            variable = self.choixPolice,
            value = stylePoliceTk[2])
            #command = self.changePolice)
        r_bout2.grid(column=1, row=4, sticky='W')
"""


        # ==========================


oop = OOP()
oop.win.mainloop()
