import tkinter as Tk
from tkinter import Frame, StringVar, ttk, Label, LabelFrame, Entry, PhotoImage, StringVar, IntVar
import sqlite3
from tkinter.constants import END
from tkcalendar import Calendar, DateEntry
from tinydb import TinyDB, where, Query
from manager_tg import Manager


def treeview_sort_column(tv, col, reverse):
    # permet de faire le classement dans la fenetre listing
    # traite element / element et colonne / colonne

    list_tree = [(tv.set(k, col), k) for k in tv.get_children('')]
    list_tree.sort(key=lambda t: t[0], reverse=reverse)
    #      ^^^^^^^^^^^^^^^^^^^^^^^

    for index, (val, k) in enumerate(list_tree):
        tv.move(k, '', index)

    tv.heading(col,
               command=lambda: treeview_sort_column(tv, col, not reverse))


class ChessMaster:
    def __init__(self, notebook, frame):
        self.notebook = notebook
        self.frame = frame
        ntbk = ttk.Notebook()


class GenericLayout(ttk.Frame):
    def __init__(self, master, title):
        ttk.Frame.__init__(self, master)
        label_frame = LabelFrame(master, text=title)
        label_frame.grid(row=0, column=1, sticky='n')
        mlabel = Label(label_frame, text='Nom du tournoi :').grid(row=0, column=0, sticky='nw', pady=2)


class ChessLstPlayerFrame(ttk.Frame):
    def __init__(self, master, title="Player"):
        ttk.Frame.__init__(self, master)
        self.title = title

        photo = PhotoImage(file='icons/knight-horse-chess-player.gif')
        birthdate_valid = None
        player_fr = LabelFrame(master, text='Créer un nouveau joueur')

        player_fr.grid(row=0, column=0, ipadx=0, ipady=50, sticky='wn')

        cal1 = Calendar(player_fr, selectmode='day', year=1980, month=6, day=15)
        print(cal1.selection_get())
        cal1.grid(row=0, column=0, sticky='n')

        lst_player_fr = LabelFrame(player_fr, text='liste des joueurs Club')
        lst_player_fr.grid(row=1, column=0, ipadx=10, ipady=20, sticky='sw')

        label = Label(player_fr, image=photo)
        label.image = photo

        label.grid(row=0, column=0, padx=5, pady=10, sticky='nw')
        # ++++++++++++++++++++++++++++++++++++++
        # FORMULAIRE SAISIE
        # ++++++++++++++++++++++++++++++++++++++
        Label(player_fr, text='Nom:').grid(row=0, column=0, padx=100, pady=10, sticky='nw')
        self.lastname = StringVar()
        self.namefield = Entry(player_fr, textvariable=self.lastname)
        self.namefield.grid(row=0, column=0, sticky='nw', padx=210, pady=10)

        Label(player_fr, text='Prénom:').grid(row=0, column=0, padx=100, sticky='nw', pady=35)
        self.firstname = StringVar()
        self.firstnamefield = Entry(player_fr, textvariable=self.firstname)
        self.firstnamefield.grid(row=0, column=0, sticky='nw', padx=210, pady=35)

        Label(player_fr, text='Genre:').grid(row=0, column=0, sticky='nw', padx=100, pady=60)
        self.gender = StringVar()
        self.genderfield = ttk.Combobox(player_fr, textvariable=self.gender, width=17)
        self.genderfield['values'] = ("Masculin", 'Feminin')
        self.genderfield.grid(row=0, column=0, sticky='nw', padx=210, pady=60)
        self.genderfield.current(0)

        Label(player_fr, text='Date de naissance:').grid(row=0, column=0, sticky='nw', padx=100, pady=85)
        self.birthdate = StringVar()

        self.birthdatefield = DateEntry(player_fr, width=12, background='darkblue',
                                        foreground='white', borderwidth=2)
        self.birthdatefield.grid(row=0, column=0, sticky='nw', padx=210, pady=85)

        Label(player_fr, text='Classement:').grid(row=0, column=0, sticky='nw', padx=100, pady=110)
        self.rank = IntVar()
        self.rankfield = Entry(player_fr, textvariable=self.rank)
        self.rankfield.grid(row=0, column=0, sticky='nw', padx=210, pady=110)

        cal1 = Calendar(player_fr, selectmode='day', year=1980, month=6, day=15)

        cal1.grid(row=0, column=0, sticky='n')

        # ++++++++++++++++++++++++++++++++++++++
        # BOUTONS
        # ++++++++++++++++++++++++++++++++++++++

        ttk.Button(player_fr, text='Ajouter à la liste', command=self.create_player).grid(
                    row=0, column=0, sticky='nw', padx=210, pady=135)

        showbtn = ttk.Button(lst_player_fr, text="Voir la liste", command=self.view_records)
        showbtn.grid(row=1, column=0, padx=20, pady=20, sticky='w')
        self.msg = Label(text='', fg='red')
        self.msg.grid(row=1, column=0, padx=50, sticky='w')

        delbtn = ttk.Button(lst_player_fr, text="Delete Selected", command=self.delete_record)
        delbtn.grid(row=1, column=0, padx=200, sticky='w')

        updtbtn = ttk.Button(lst_player_fr, text="Modify Selected", command=self.open_modify_window)
        updtbtn.grid(row=1, column=0, padx=100, sticky='w')

        # ++++++++++++++++++++++++++++++++++++++
        # FORMULAIRE LISTING
        # ++++++++++++++++++++++++++++++++++++++
        my_columns = ("Id", "Name", "Firstname", "Birthdate", "Gender", "Rank",)
        self.tree = ttk.Treeview(lst_player_fr, height=6, columns=my_columns)
        self.tree.grid(row=2, column=0, sticky='nw')
        self.tree.heading('#0', text='', anchor='w')
        self.tree.column("#0", minwidth=1, width=2)

        for col in my_columns:
            self.tree.heading(col, text=col, anchor='w',
                              command=lambda c=col: treeview_sort_column(self.tree, c, False))

    def create_record(self):
        lastname = self.namefield.get()
        firstname = self.firstnamefield.get()
        gender = self.genderfield.get()
        birthdate = self.birthdatefield.get()
        rank = self.rankfield.get()

        if gender == 'Masculin':
            gender = "M"
        else:
            gender = "F"
        if lastname == "":
            self.msg["text"] = "Please Enter name"
            return
        if rank == "":
            self.msg["text"] = "Please Enter Number"
            return

        db_players = TinyDB('./data_players2.json').table('players_list')
        db_players.insert({"id": 1000, "lastname": lastname, "firstname": firstname, "gender": gender,
                           "birthdate": birthdate, "rank": rank, "score": 0})

    def create_player(self):
        lastname = self.namefield.get()
        firstname = self.firstnamefield.get()
        gender = self.genderfield.get()
        birthdate = self.birthdatefield.get()
        rank = self.rankfield.get()

        if gender == 'Masculin':
            gender = "M"
        else:
            gender = "F"
        if lastname == "":
            self.msg["text"] = "Please Enter name"
            return
        if rank == "":
            self.msg["text"] = "Please Enter Number"
            return

        my_player = {"id": 1000, "lastname": lastname, "firstname": firstname, "gender": gender,
                     "birthdate": birthdate, "rank": rank, "score": 0}
        players = {}
        manager = Manager('./data_players2.json', 'players_list', players)
        manager.data_insert(my_player)

        self.namefield.delete(0, END)
        self.rankfield.delete(0, END)
        self.msg["text"] = ("le classement de %s a été ajouté" % lastname)
        self.view_records()

    def view_records_old(self):
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)

        db_players = TinyDB('./data_players2.json').table('players_list')
        serialized_players = {}
        i = 0
        for db_item in db_players:
            serialized_players[i] = db_item

            print(serialized_players[i])
            i += 1
        print(serialized_players)
        values_lists = {}

        for player_item in range(len(serialized_players)):
            print(serialized_players[player_item])
            serial_d_player = serialized_players[player_item]

            value_list = serial_d_player.values()
            value_list = list(value_list)
            values_lists[player_item] = value_list
            rank_sorted = sorted(values_lists.items(), key=lambda t: t[1][5])
            alpha_sorted = sorted(values_lists.items(), key=lambda t: t[1][1])
            print(value_list)
            self.tree.insert("", END, text="", values=value_list[0:-1])

    def view_records(self):
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)

        tk_manager = Manager('./data_players2.json', 'players_list')
        all_db_data, count = tk_manager.load_all_from_tinydb()

        for player_item in range(count):
            serial_d_player = all_db_data[player_item]

            self.tree.insert("", END, text="", values=serial_d_player[0:-1])

    def sorting_head(self, value_list, head_list):
        for t in value_list:
            self.tree.insert('', END, values=(t,))

            for col in head_list:
                self.tree.heading(col, text=col,
                                  command=lambda c=col: treeview_sort_column(self.tree, c, False))

    def delete_record(self):
        self.msg["text"] = ""
        db_players = TinyDB('./data_players2.json').table('players_list')
        for selected_item in self.tree.selection():
            # dictionary
            item = self.tree.item(selected_item)
            # list
            record = (item['values'])
            #  id , lastname, firstname,
            print(record[0])

        query = db_players.search(where('id') == record[0])  # on prends l'id
        if len(query) > 0:
            db_players.remove(where('lastname') == record[1])
            self.msg["text"] = "Le classment de %s est supprimé " % record[1]

        self.view_records()

    def open_modify_window(self):
        try:
            self.msg["text"] = ""
            name = self.tree.item(self.tree.selection())['values'][1]

            oldrank = self.tree.item(self.tree.selection())['values'][5]
            self.msg["text"] = ""

            player_id = self.tree.item(self.tree.selection())['values'][0]
            self.msg["text"] = ""

            self.tl = Tk()
            Label(self.tl, text='Nom:').grid(row=0, column=1, sticky='W')
            ne = Entry(self.tl)
            ne.grid(row=0, column=2, sticky='W')
            ne.insert(0, name)
            ne.config(state='readonly')

            Label(self.tl, text='Ancien classement:').grid(row=1, column=1, sticky='W')
            ope = Entry(self.tl)
            ope.grid(row=1, column=2, sticky='W')
            ope.insert(0, str(oldrank))
            ope.config(state='readonly')

            Label(self.tl, text='Nouveau classement:').grid(row=2, column=1, sticky='W')
            newrk = StringVar()
            newrk = Entry(self.tl, textvariable=newrk)
            newrk.grid(row=2, column=2, sticky='W')

            upbtn = ttk.Button(self.tl, text='Modifier', command=lambda: self.update_record(newrk.get(),
                               oldrank, name, player_id))
            upbtn.grid(row=3, column=2, sticky='e')

            self.tl.mainloop()

        except IndexError as e:
            self.msg["text"] = "Please Select Item to Modify"

    def update_record(self, newrank, oldrank, name, id=None):
        """ modifie le rang du joueur
        en updatant la base par son nom,
        """
        try:
            db_players = TinyDB('./data_players2.json').table('players_list')

            query = db_players.search(where('id') == id)

            if query:
                db_players.update({'rank': newrank}, where('id') == id)
                self.msg["text"] = "Le classement de %s a été modifié" % name
            else:
                query = db_players.search(where('lastname') == name)
                db_players.update({'rank': newrank}, where('lastname') == name)
            self.tl.destroy()

        except IndexError as e:
            self.msg["text"] = "Please Select Item to Modify"
        self.view_records()


class ChessPlayer_Tour(ChessLstPlayerFrame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        ins_trm_fr = LabelFrame(master, text="Inscription à un tournoi")
        ins_trm_fr.grid(row=0, column=0, padx=8, pady=8, sticky='nw')

        Label(ins_trm_fr, text='Choix tournoi:').grid(row=0, column=0, sticky='w', padx=5, pady=26)
        self.tr_select = StringVar()
        self.tr_select_field = ttk.Combobox(ins_trm_fr, textvariable=self.tr_select, width=17)
        self.tr_select_field['values'] = ("tour1", 'tour2')
        self.tr_select_field.grid(row=0, column=0, sticky='w', padx=100, pady=46)
        self.tr_select_field.current(0)

        ttk.Button(
            ins_trm_fr, text='Ajouter joueur au tournoi', command=self.create_record).grid(
            row=3, column=0, sticky='nw', padx=220, pady=35
                    )
        delbtn_player = ttk.Button(ins_trm_fr, text="Delete Selected", command=self.delete_record)
        delbtn_player.grid(row=3, column=0, padx=20, pady=35, sticky='nw')

        # ================================================================
        # liste
        # ================================================================
        self.tree = ttk.Treeview(ins_trm_fr, height=6, columns=("firstname", "gender", "birthdate", "rank"))
        self.tree.grid(row=2, column=0, sticky='nw')
        self.tree.heading('#0', text='Nom', anchor="w")
        self.tree.heading("firstname", text='Prénom', anchor="w")
        self.tree.heading("gender", text='Genre', anchor="w")
        self.tree.heading("birthdate", text='Date de naissance', anchor="w")
        self.tree.heading("rank", text='Classement', anchor="w")

        self.tree_trn = ttk.Treeview(ins_trm_fr, height=6, columns=("firstname", "rank"))
        self.tree_trn.grid(row=3, column=0, pady=100, sticky='ws')
        self.tree_trn.heading('#0', text='Nom', anchor='w')
        self.tree_trn.heading("firstname", text='Prénom', anchor='w')
        self.tree_trn.heading("rank", text='Classement', anchor='w')


class TournamentFrame(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)

        chess_fr = LabelFrame(master, text='Créer un nouveau tournoi')
        chess_fr.grid(row=0, column=0, padx=8, pady=8, sticky='n')

        lst_chess_fr = LabelFrame(chess_fr, text="Liste des tournois du club")
        lst_chess_fr.grid(row=4, column=0, padx=8, pady=8, sticky='n')

        photo = PhotoImage(file='icons/chess_tournament.gif')
        label = Label(chess_fr, image=photo)
        label.image = photo
        label.grid(row=0, column=0, padx=5, pady=10, sticky='nw')
        # ===============================================================
        #  formulaire de saisie
        # ===============================================================
        Label(chess_fr, text='Nom :').grid(row=0, column=0, sticky='nw', padx=150, pady=10)
        self.name = StringVar()
        self.namefield = Entry(chess_fr, textvariable=self.name)
        self.namefield.grid(row=0, column=0, sticky='nw', padx=260, pady=10)

        Label(chess_fr, text='Lieu :').grid(row=0, column=0, sticky='nw', padx=150, pady=35)
        self.place = StringVar()
        self.placefield = Entry(chess_fr, textvariable=self.place)
        self.placefield.grid(row=0, column=0, sticky='nw', padx=260, pady=35)

        Label(chess_fr, text='Date ouverture :').grid(row=0, column=0, sticky='nw', padx=150, pady=60)
        self.start_date = StringVar()
        self.start_datefield = Entry(chess_fr, textvariable=self.start_date)
        self.start_datefield.grid(row=0, column=0, sticky='nw', padx=260, pady=60)

        Label(chess_fr, text='Date fermeture :').grid(row=0, column=0, sticky='nw', padx=150, pady=85)
        self.end_date = StringVar()
        self.end_datefield = Entry(chess_fr, textvariable=self.end_date)
        self.end_datefield.grid(row=0, column=0, sticky='nw', padx=260, pady=85)

        Label(chess_fr, text='Gestion du temps :').grid(row=0, column=0, sticky='nw', padx=150,  pady=110)
        self.time_control = StringVar()
        self.time_controlfield = ttk.Combobox(chess_fr, width=17, textvariable=self.time_control)
        self.time_controlfield['values'] = ("Bullet", "Blitz", "Coups rapide")
        self.time_controlfield.grid(row=0, column=0, sticky='nw', padx=260, pady=110)
        self.time_controlfield.current(1)

        Label(lst_chess_fr, text='Affichage liste:').grid(row=0, column=0, sticky='nw', padx=50,  pady=50)
        self.lst_chess = StringVar()
        self.lst_chessfield = ttk.Combobox(lst_chess_fr, width=22, textvariable=self.lst_chess)
        self.lst_chessfield['values'] = ("Classement alphabétique", "Classement par rang")
        self.lst_chessfield.grid(row=0, column=0, sticky='nw', padx=150, pady=50)
        self.lst_chessfield.current(1)

        # ===============================================================
        #  liste
        # ===============================================================

        showbtn = ttk.Button(lst_chess_fr, text="Voir la liste", command=self.view_records)
        showbtn.grid(row=2, column=0, sticky='w')

        self.msg = Label(lst_chess_fr, text='', fg='red')
        self.msg.grid(row=1, column=1, sticky='e')

        self.tree_chess = ttk.Treeview(
            lst_chess_fr, height=6, columns=("place", "start_date", "end_date", "time_control")
            )
        self.tree_chess.grid(row=3, column=0, columnspan=100)
        self.tree_chess.heading('#0', text='Nom', anchor='w')
        self.tree_chess.heading("place", text='Lieu', anchor='w')
        self.tree_chess.heading("start_date", text='Date début', anchor='w')
        self.tree_chess.heading("end_date", text='Date de fin', anchor='w')
        self.tree_chess.heading("time_control", text='Gestion du temps', anchor='w')

        delbtn = ttk.Button(lst_chess_fr, text="Delete Selected", command=self.delete_record)
        delbtn.grid(row=2, column=0, pady=2, sticky='nw')

        updtbtn = ttk.Button(lst_chess_fr, text="Modify Selected", command=self.open_modify_window)
        updtbtn.grid(row=2, column=1, pady=2, sticky='nw')

    def create_record(self):
        name = self.namefield.get()
        place = self.placefield.get()
        if name == "":
            self.msg["text"] = "Please Enter name"
            return
        if place == "":
            self.msg["text"] = "Please Enter Lieu"
            return
        conn = sqlite3.connect('phonebook.db')
        c = conn.cursor()
        c.execute("INSERT INTO players VALUES(NULL,?, ?)", (name, place))
        conn.commit()
        c.close()
        self.namefield.delete(0, END)
        self.placefield.delete(0, END)
        self.msg["text"] = "le tournoi de %s a été ajouté" % name
        self.view_records()

    def view_records(self):
        x = self.tree_chess.get_children()
        for item in x:
            self.tree.delete(item)
        conn = sqlite3.connect('phonebook.db')
        c = conn.cursor()

        list = c.execute("SELECT * FROM contacts ORDER BY name desc")
        for row in list:
            self.tree_chess.insert("", 0, text=row[1], values=row[2])
        c.close()

    def delete_record(self):
        self.msg["text"] = ""
        conn = sqlite3.connect('phonebook.db')
        c = conn.cursor()
        name = self.tree.item(self.tree_chess.selection())['text']
        query = "DELETE FROM contacts WHERE name = '%s';" % name
        c.execute(query)
        conn.commit()
        c.close()
        self.msg["text"] = "Le classment de %s est supprimé " % name

    def open_modify_window(self):
        try:
            self.msg["text"] = ""
            name = self.tree.item(self.tree.selection())['text']
            oldrank = self.tree.item(self.tree.selection())['values'][0]

            self.tl = Tk()
            Label(self.tl, text='Nom:').grid(row=0, column=1, sticky='W')
            ne = Entry(self.tl)
            ne.grid(row=0, column=2, sticky='W')
            ne.insert(0, name)
            ne.config(state='readonly')

            Label(self.tl, text='Ancien data:').grid(row=1, column=1, sticky='W')
            ope = Entry(self.tl)
            ope.grid(row=1, column=2, sticky='W')
            # ope.insert(0,str(oldphone))
            ope.config(state='readonly')
            Label(self.tl, text='Nouveau data:').grid(row=2, column=1, sticky='W')
            newrk = StringVar()
            newrk = Entry(self.tl, textvariable=newrk)
            newrk.grid(row=2, column=2, sticky='W')

            upbtn = ttk.Button(self.tl, text='Modifier', command=lambda: self.update_record(
                               newrk.get(), oldrank, name))
            upbtn.grid(row=3, column=2, sticky="E")
            self.tl.mainloop()

        except IndexError as e:
            self.msg["text"] = "Please Select Item to Modify"

    def update_record(self, newdata, oldata, name):
        conn = sqlite3.connect('phonebook.db')
        c = conn.cursor()
        c.execute("UPDATE contacts SET contactnumber=? WHERE contactnumber=? AND name=?", (newdata, oldata, name))
        conn.commit()
        c.close()
        self.tl.destroy()
        self.msg["text"] = "Le classement de %s a été modifié" % name
        self.view_records()


class Turn(ttk.Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        fr = LabelFrame(master, text='Saisir un nouveau resultat')
        fr.grid(row=0, column=1, padx=8, pady=8, sticky='ew')

        Label(fr, text='Nom du tournoi :').grid(row=0, column=0, sticky='nw', padx=150, pady=10)
        self.name = StringVar()
        self.namefield = Entry(fr, textvariable=self.name)
        self.namefield.grid(row=0, column=0, sticky='nw', padx=260, pady=10)

        Label(fr, text='Round :').grid(row=0, column=0, sticky='nw', padx=150, pady=35)
        self.round = StringVar()
        self.roundfield = Entry(fr, textvariable=self.round)
        self.roundfield.grid(row=0, column=0, sticky='nw', padx=260, pady=35)

        Label(fr, text='Date ouverture :').grid(row=0, column=0, sticky='nw', padx=150, pady=60)
        self.start_date = StringVar()
        self.start_datefield = Entry(fr, textvariable=self.start_date)
        self.start_datefield.grid(rrow=0, column=0, sticky='nw', padx=260, pady=60)

        Label(fr, text='Date fermeture :').grid(row=0, column=0, sticky='nw', padx=150, pady=85)
        self.end_date = StringVar()
        self.end_datefield = Entry(fr, textvariable=self.end_date)
        self.end_datefield.grid(row=0, column=0, sticky='nw', padx=260, pady=85)

        Label(fr, text='Gestion du temps :').grid(row=0, column=0, sticky='nw', padx=150, pady=110)
        self.time_control = StringVar()
        self.time_controlfield = ttk.Combobox(fr, width=20, textvariable=self.time_control)
        self.time_controlfield['values'] = ("Bullet", "Blitz", "Coups rapide")
        self.time_controlfield.grid(row=0, column=0, sticky='nw', padx=260, pady=110)
        self.time_controlfield.current(1)

        ttk.Button(fr, text='Ajouter à la liste', command=self.create_record).grid(row=5, column=2,
                                                                                   sticky='e', padx=5, pady=2)
        showbtn = ttk.Button(text="Voir la liste", command=self.view_records)
        showbtn.grid(row=5, column=0, sticky='w')

        self.msg = Label(text='', fg='red')
        self.msg.grid(row=5, column=1, sticky='w')

        self.tree = ttk.Treeview(height=6, columns=("place", "start_date", "end_date", "time_control"))
        self.tree.grid(row=15, column=0, columnspan=100)
        self.tree.heading('#0', text='Nom', anchor='W')
        self.tree.heading("place", text='Lieu', anchor='W')
        self.tree.heading("start_date", text='Date début', anchor='W')
        self.tree.heading("end_date", text='Date de fin', anchor='W')
        self.tree.heading("time_control", text='Gestion du temps', anchor='W')

        delbtn = ttk.Button(text="Delete Selected", command=self.delete_record)
        delbtn.grid(row=7, column=0, sticky='w')

        updtbtn = ttk.Button(text="Modify Selected", command=self.open_modify_window)
        updtbtn.grid(row=7, column=1, sticky='w')
        self.view_records()


class MatchFrame(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        # ===============================================================
        #  formulaire de saisie
        # ===============================================================
        fr = LabelFrame(master, text='Saisir un nouveau resultat')
        fr.grid(row=0, column=0, padx=8, pady=8, sticky='nw')

        Label(fr, text='Nom du tournoi :').grid(row=0, column=0, sticky='nw', padx=150, pady=10)
        self.name = StringVar()
        self.namefield = ttk.Combobox(fr, width=17, textvariable=self.name)
        self.namefield['values'] = ["Tournoi 1 ", "Tournoi  2 ", ""]
        self.namefield.grid(row=0, column=0, sticky='nw', padx=260, pady=10)

        Label(fr, text='Round :').grid(row=0, column=0, sticky='nw', padx=150, pady=35)
        self.round = StringVar()
        self.roundfield = ttk.Combobox(fr, width=17, textvariable=self.round)
        self.roundfield['values'] = ["Round 1 ", "Round  2 ", ""]
        self.roundfield.grid(row=0, column=0, sticky='nw', padx=260, pady=35)

        Label(fr, text='Nom échiquier :').grid(row=0, column=0, sticky='nw', padx=150, pady=60)
        self.name_chess = StringVar()
        self.name_chessfield = Entry(fr, textvariable=self.name_chess)
        self.name_chessfield.grid(row=0, column=0, sticky='nw', padx=260, pady=60)

        Label(fr, text='Joueur 1 :').grid(row=0, column=0, sticky='nw', padx=410, pady=60)
        self.player1_name = StringVar()
        self.player1_namefield = Entry(fr, textvariable=self.player1_name)
        self.player1_namefield.grid(row=0, column=0, sticky='nw', padx=480, pady=60)

        Label(fr, text='Joueur 2 :').grid(row=0, column=0, sticky='nw', padx=410, pady=85)
        self.player2_name = StringVar()
        self.player2_namefield = Entry(fr, textvariable=self.player2_name)
        self.player2_namefield.grid(row=0, column=0, sticky='nw', padx=480, pady=85)

        Label(fr, text='Date ouverture :').grid(row=0, column=0, sticky='nw', padx=150, pady=85)
        self.start_date = StringVar()
        self.start_datefield = Entry(fr, textvariable=self.start_date)
        self.start_datefield.grid(row=0, column=0, sticky='nw', padx=260, pady=85)

        # la date de fermeture sera ecrite automatique à la saisie du resultat
        Label(fr, text='Date fermeture :').grid(row=0, column=0, sticky='nw', padx=150, pady=110)
        self.end_date = StringVar()
        self.end_datefield = Entry(fr, textvariable=self.end_date)
        self.end_datefield.grid(row=0, column=0, sticky='nw', padx=260, pady=110)

        Label(fr, text='Résultat :').grid(row=0, column=0, sticky='nw', padx=410, pady=110)
        self.matchresult = StringVar()
        self.matchresult_controlfield = ttk.Combobox(fr, width=17, textvariable=self.matchresult)
        self.matchresult_controlfield['values'] = ("Joueur 1 win", "Joueur 2 win", "Nul", "")
        self.matchresult_controlfield.grid(row=0, column=0, sticky='nw', padx=480, pady=110)
        self.matchresult_controlfield.current(3)
        # ===============================================================
        #  boutons
        # ===============================================================
        ttk.Button(fr, text='Enregistrer résultat').grid(row=0, column=0, sticky='nw', padx=150, pady=135)
        showbtn = ttk.Button(fr, text="Actualiser la liste")

        showbtn.grid(row=0, column=0, sticky='nw', padx=20, pady=135)

        self.msg = Label(fr, text='', fg='red')
        self.msg.grid(row=0, column=0, sticky='nw', padx=300, pady=135)

        delbtn = ttk.Button(fr, text="Delete Selected")
        delbtn.grid(row=0, column=0, sticky='nw', padx=20, pady=170)

        updtbtn = ttk.Button(fr, text="Modify Selected")
        updtbtn.grid(row=0, column=0, sticky='nw', padx=20, pady=200)

        # ===============================================================
        #  liste
        # ===============================================================
        self.tree = ttk.Treeview(fr, height=6, columns=("start_date", "end_date", "Player 1", "Player 2", "Results"))
        self.tree.grid(row=1, column=0, sticky='nw', pady=10)
        self.tree.heading('#0', text='Echiquier', anchor='W')
        self.tree.heading("start_date", text='Date début', anchor='W')
        self.tree.heading("end_date", text='Date de fin', anchor='W')
        self.tree.heading("Player 1", text='Player 1', anchor='W')
        self.tree.heading("Player 2", text='Player 2', anchor='W')
        self.tree.heading("Results", text='Résultat gagnant', anchor='W')


class ReportFrame(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        # ===============================================================
        #  formulaire de saisie
        # ===============================================================
        fr = LabelFrame(master, text='Affichage recapitulatif tournois')
        fr.grid(row=0, column=0, padx=8, pady=8, sticky='nw')

        Label(fr, text='Round :').grid(row=1, column=0, sticky='nw', pady=2)
        Label(fr, text='Match :').grid(row=2, column=0, sticky='nw', pady=2)

        # ===============================================================
        #  liste
        # ===============================================================
        self.tree = ttk.Treeview(fr, height=6, columns=("place", "start_date", "end_date", "time_control"))
        self.tree.grid(row=0, column=0, pady=20, sticky='w')
        self.tree.heading('#0', text='Nom', anchor='w')
        self.tree.heading("place", text='Lieu', anchor='w')
        self.tree.heading("start_date", text='Date début', anchor='w')
        self.tree.heading("end_date", text='Date de fin', anchor='w')
        self.tree.heading("time_control", text='Gestion du temps', anchor='w')

        self.rnd_tree = ttk.Treeview(fr, height=6, columns=("start_date", "end_date"))
        self.rnd_tree.grid(row=1, column=0, columnspan=3, pady=20, sticky='w')
        self.rnd_tree.heading('#0', text='Round', anchor='w')
        self.rnd_tree.heading("start_date", text='Date début', anchor='w')
        self.rnd_tree.heading("end_date", text='Date de fin', anchor='w')

        self.match_tree = ttk.Treeview(fr, height=6, columns=(
                                       "start_date", "end_date", "Player 1", "Player 2", "Results"))
        self.match_tree.grid(row=2, column=0, pady=20, sticky='w')
        self.match_tree.heading('#0', text='Echiquier', anchor='w')
        self.match_tree.heading("start_date", text='Date début', anchor='w')
        self.match_tree.heading("end_date", text='Date de fin', anchor='w')
        self.match_tree.heading("Player 1", text='Player 1', anchor='w')
        self.match_tree.heading("Player 2", text='Player 2', anchor='w')
        self.match_tree.heading("Results", text='Résultat gagnant', anchor='w')


def maintk():
    root = Tk()
    root.title("ChessMaster little Championship")
    # root.geometry("1024x728")

    ntbk = ttk.Notebook(root)
    # n.pack(pady=10, expand=True)
    ntbk.grid(row=0, column=0, padx=20, pady=20)
    o1 = ttk.Notebook(ntbk)
    ChessLstPlayerFrame(o1)       # Ajout de l'onglet 1

    # o1.pack()
    o1.grid(row=0, column=0, padx=25, pady=20)

    o2 = ttk.Notebook(ntbk)       # Ajout de l'onglet 2
    # o2.pack()
    TournamentFrame(o2)
    o2.grid(row=0, column=0, padx=35, pady=20)

    o3 = ttk.Notebook(ntbk)
    ChessPlayer_Tour(o3)
    o3.grid(row=0, column=0, padx=45, pady=20)

    o4 = ttk.Notebook(ntbk)
    MatchFrame(o4)       # Ajout de l'onglet 3
    # o3.pack()
    o4.grid(row=0, column=0, padx=55, pady=20)

    o5 = ttk.Frame(ntbk)       # Ajout de l'onglet 4
    # o4.pack()
    ReportFrame(o5)
    o5.grid(row=0, column=0, padx=65, pady=20)

    o6 = ttk.Frame(ntbk)
    GenericLayout(o6, 'test titre')
    o6.grid(row=0, column=0, padx=75, pady=20)

    ntbk.add(o1, text="Joueurs")      # Nom de l'onglet 1
    ntbk.add(o2, text="Tournois")      # Nom de l'onglet 2
    ntbk.add(o3, text="Joueurs en Tournois")      # Nom de l'onglet 3
    ntbk.add(o4, text="Matchs")      # Nom de l'onglet 4
    ntbk.add(o5, text="Rapports")      # Nom de l'onglet 5
    ntbk.add(o6, text="tests")

    # application = ChessPlayerFrame(root)
    # application = TournamentFrame(root)
    root.mainloop()


if __name__ == '__main__':
    maintk()
