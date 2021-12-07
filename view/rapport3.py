
class ViewPlayer:
    def __init__(self, data_type: any):
        self.lastname = data_type[0]
        self.firstname = data_type[1]
        self.rank = data_type[2]
        self.ind = data_type[3]
        self.score = data_type[4]
        self.id = data_type[5]

    def print_data(self):
        print('%-13s' % self.lastname,
              '%-12s' % self.firstname,
              '%-8s' % self.rank,
              '%-10s' % self.ind,
              '%-8s' % self.score,
              '%-8s' % self.id
              )


class Viewplayer_db(ViewPlayer):
    def __init__(self, data_type: any):
        self.id = data_type[0]
        self.lastname = data_type[1]
        self.firstname = data_type[2]
        self.birthdate = data_type[3]
        self.gender = data_type[4]
        self.rank = data_type[5]
        self.score = data_type[6]

    def print_data(self):
        print('%-5s' % self.id,
              '%-15s' % self.lastname,
              '%-12s' % self.firstname,
              '%-22s' % self.birthdate,
              '%-10s' % self.gender,
              '%-10s' % self.rank,
              '%-5s' % self.score
              )


class ViewMatch:
    def __init__(self, data_type: any):
        self.nom_echiquier = data_type[0]
        self.ind_j1 = data_type[1]
        self.ind_j2 = data_type[2]
        self.state = data_type[3]

    def print_data(self):
        print('%-20s' % self.nom_echiquier,
              '%-20s' % self.ind_j1,
              '%-18s' % self.ind_j2,
              '%-10s' % self.state
              )


class ViewTnmt:
    def __init__(self, data_type: any):
        self.id = data_type[0]
        self.nom = data_type[1]
        self.place = data_type[2]
        self.start_date = data_type[3]
        self.end_date = data_type[4]
        self.time_control = data_type[5]
        self.nbround = data_type[6]
        self.state = data_type[7]

    def print_data(self):
        print('%-7s' % self.id,
              '%-22s' % self.nom,
              '%-20s' % self.place,
              '%-20s' % self.start_date,
              '%-20s' % self.end_date,
              '%-15s' % self.time_control,
              '%-10s' % self.nbround,
              '%-10s' % self.state,
              )


class ViewRound:
    def __init__(self, data_type: any):
        self.id = data_type['number']
        self.start_date = data_type['start_date']
        self.end_date = data_type['end_date']

    def print_data(self):
        print('%-10s' % self.id,
              '%-19s' % self.start_date,
              '%-5s' % self.end_date
              )


class ViewMatch_db(ViewMatch):
    def __init__(self, data_type: any):
        self.id = data_type[0]
        self.round = data_type[1]
        self.id_TMNT = data_type[2]
        self.nom = data_type[3]
        self.joueur1 = data_type[4]
        self.joueur2 = data_type[5]
        self.scorej1 = data_type[6]
        self.scorej2 = data_type[7]
        self.start_date = data_type[8]
        self.end_date = data_type[9]

    def print_data(self):
        print('%-10s' % self.round,
              '%-7s' % self.nom,
              '%-24s' % self.joueur1,
              '%-25s' % self.joueur2,
              '%-18s' % self.scorej1,
              '%-15s' % self.scorej2,
              '%-18s' % self.start_date,
              '%-22s' % self.end_date,
              )


class Rapport:
    def __init__(self, affichage: str):
        self.affichage = affichage

    def print_row_tab_player(self, player_serialized):
        """print the information of player a the end of round"""
        print("")
        data_title = ["Nom", "Prenom", "rang", "Ind", "Score", "ID"]
        mon_title = ViewPlayer(data_title)
        mon_title.print_data()
        print("")

        for row in range(len(player_serialized)):
            mon_player_to_print = ViewPlayer(player_serialized[row])
            mon_player_to_print.print_data()

        print("")

    def print_row_tab_round(self, round, match):
        """ print the result of a round  match/match without name of player"""
        match_view_list = []
        print("")
        data_title = ["Nom Echiquier", "indice joueur 1", "indice Joueur 2",  "Resultat"]
        mon_title = ViewMatch(data_title)
        mon_title.print_data()
        print("")
        for row in range(0, len(match), 4):
            m_row = row + 3
            match_view_list = [match[row], match[row+1], match[row+2], match[row+3]]
            if match[m_row] == 10:
                match_view_list[3] = 'Non joué'
                mavisumatch = ViewMatch(match_view_list)
                mavisumatch.print_data()

        print("")

    def print_row_tab_round_2(self, round, match):
        """ print the result of a round  match/match with name of player by objet to print"""
        match_view_list = []
        print("")
        data_title = ["Nom Echiquier", "indice joueur 1", "indice Joueur 2",  "Resultat"]
        mon_title = ViewMatch(data_title)
        mon_title.print_data()
        print("")

        for row in range(len(match)):
            match_view_list = [match[row][0],
                               match[row][1] + "  " + match[row][4],
                               match[row][2] + "  " + match[row][5],
                               match[row][3]]
            if match[row][3] == 10:
                match_view_list[3] = 'Non joué'

                mavisumatch = ViewMatch(match_view_list)
                mavisumatch.print_data()
        print("")

    def print_players_database(self, player_serialized, title2='rank', title="Liste des joueurs du club"):
        """ print all data of the player database with object to print"""

        tab = "    "
        # method of sorting
        if title2 == 'rank':
            title2b = "rangé par classement"
        elif title2 == 'alpha':
            title2b = "rangé par ordre alphabetique"
        else:
            title2b = ""

        print("")
        print('%-25s' % tab, title)
        if not title2 == "":
            print('%-25s' % tab, title2b)
        data_title = ["ID", "Nom", "Prénom", "date de naissance", "Genre", "Rang", "Score"]
        mon_title = Viewplayer_db(data_title)
        mon_title.print_data()
        print("")

        for row in range(len(player_serialized)):
            m_player_to_print = Viewplayer_db(player_serialized[row])
            m_player_to_print.print_data()
        print("Nombre de joueurs :", len(player_serialized))

    def print_tournament_database(self, tmnt_serialized, title2='open', title="Liste des tournois"):
        """ print all data of the tournament database"""

        tab = "    "
        # method of sorting
        if title2 == 'open':
            title2b = "en cours"
        elif title2 == 'finished':
            title2b = "terminés"
        else:
            title2b = ""

        print("")
        print('%-25s' % tab, title)
        if not title2 == "":
            print('%-25s' % tab, title2b)

        data_title = ["ID", "Nom", "Lieu", "Date de début", "Date de fin", "Controle temps", "Nbr Round", "Statut"]
        m_tmnt = ViewTnmt(data_title)
        m_tmnt.print_data()

        print("")
        for row in range(len(tmnt_serialized)):
            m_tmnt = ViewTnmt(tmnt_serialized[row])

            if title2 == 'open' and m_tmnt.state == "open":
                m_tmnt.print_data()

            if title2 == 'finished' and m_tmnt.state == "closed":
                m_tmnt.print_data()

            else:
                # all tournaments will beprinted on screen
                m_tmnt.print_data()

        print("")

    def print_round_tmnt_datase(self, data_serialized, title2="", title="Liste des round"):
        """ print all round in tournament with start date and end_date by object to print"""
        tab = "    "

        title2b = ""

        print("")
        print('%-25s' % tab, title)
        if not title2 == "":
            print('%-25s' % tab, title2b)
        data_title = {'id': "ID", "number": "Round", "start_date": "Date de début", "end_date": "Date de fin"}
        my_round = ViewRound(data_title)
        my_round.print_data()

        print("")

        for row in range(len(data_serialized)):
            my_round = ViewRound(data_serialized[row])
            my_round.print_data()

    def print_match_tmnt_datase(self, data_serialized, title2='open', title="Liste des match"):
        """ print match evenement  with a match specific match objet to print"""
        tab = "    "
        # method of sorting
        if title2 == 'open':
            title2b = "en cours"
        elif title2 == 'finished':
            title2b = "terminés"
        else:
            title2b = ""

        print("")
        print('%-25s' % tab, title)
        if not title2 == "":
            print('%-25s' % tab, title2b)

        data_title = [
            "ID", "round", "iD_TMNT", "Nom", "Joueur 1", "joueur 2", 'score joueur 1',
            'score joueur 2', "Date de début", "Date de fin"
                    ]
        m_match_db = ViewMatch_db(data_title)
        m_match_db.print_data()

        print("")

        for row in range(len(data_serialized)):
            m_match_db = ViewMatch_db(data_serialized[row])
            m_match_db.print_data()
