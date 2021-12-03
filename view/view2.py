
from manager_txt import *
# from chess_tournament import player_inscription
# from chess_tournament import players_database_list
# from chess_tournament import player_register, graphic_mode, modify_player
from chess_tournament import modify_player
from chess_tournament import *
import tournament_controler
import models
from typing import Any, List, Tuple
from rapport import print_round_tmnt_datase, print_match_tmnt_datase, print_players_database, print_tournament_database

class View:
    """ Affiche un titre & un contenu """
    def __init__(self, title: str, content: str = ""):
        self.title = title
        self.content = content

    def show(self):
        print("*"*len(self.title)*5)
        print(self.title)
        print("*"*len(self.title)*5)
        if self.content:
            print(self.content)


class Menu(View):
    """ Demande à l'utilisateur de faire un choix parmi plusieurs options et renvoi un entier """
    def __init__(self, title: str, options: List[str]):
        content = "\n".join(
            [f"{nb} - {option}" for nb, option in enumerate(options, start=1)])
        super().__init__(title, content=content)
        self.options = options

    def show(self):
        super().show()
        while True:
            try:
                choice = int(input(": "))
                if 0 < choice < len(self.options):
                    return choice
            except ValueError:
                pass


class Form(View):
    """ Demande à l'utilisateur de remplir des champs et renvoi un dictionnaire de données """
    def __init__(self, title: str, fields: List[Tuple[str, str, Any]]):
        super().__init__(title)
        self.fields = fields

    def show(self):
        data = {}
        super().show()
        for name, description, _type in self.fields:
            while True:
                try:
                    data[name] = _type(input("saisir  " + description + " ? "))

                    break
                except ValueError:
                    pass
        return data


class MenuPrincipal(View):
    """menu principal with choice"""

    def __init__(self, title: str, data: any):
        super().__init__(title)
        self.data = data

    def display_menu(self):
        for key in self.data.keys():
            print('')
            print(key, '--', self.data[key])
        print('')

    def saisie_donne(self):
        while(True):
            print('')
            try:
                choice = int(input('Entrez votre choix: '))

                return choice
            except ValueError:
                print('Mauvaise saisie ! SVP, entrez un chiffre correct')


menu_options = {
    1: 'Joueurs',
    2: 'Tournoi',
    3: 'Rapports',
    4: 'Mode graphique',
    5: 'Quitter',
}

menu_options_rapports = {
    1: "liste de tous les acteurs par ordre alphabetique",
    2: "liste de tous les acteurs par classement",
    3: "liste de tous les joueurs d'un tournoi par ordre alphabetique",
    4: "liste de tous les joueurs d'un tournoi par classement",
    5: "liste de tous les tournois",
    6: "liste de tous les tours d'un tournoi",
    7: "liste de tous les match d'un tournoi par classement",
    8: 'Retour menu principal <--',
}

menu_options_joueurs = {
    1: 'Créer Joueur',
    2: 'Modifier Joueur',
    3: 'Voir Joueurs',
    4: 'Retour menu principal <--',
}

menu_options_tournois = {
    1: 'Créer Tournoi',
    2: 'Inscrire Joueur',
    3: 'Supprimer un Joueur du tournoi',
    4: 'Voir ou Reprendre Tournois',
    5: 'Retour menu principal <--',
}

form_player = [('lastname', 'le Nom ', str), ('firstname', 'le Prénom  ', str),
               ('gender', 'le Genre (M ou F)  ', str),
               ('birthdate', 'la date de naissance (AAAA-MM-JJ)  ', str),
               ('rank', 'le Rang  ', int)]


tmnt_form = [('name', 'le Nom du tournoi', str), ('place', 'le lieu du tournoi', str),
             ('start_date', 'la date de début prévue (AAAA-MM-JJ)', str),
             ('end_date', 'la date de fin prévisionnelle (AAAA-MM-JJ)', str),
             ('time_control', 'la gestion du temps ( rapide, eclair ou normal)', str),
             ("", 'Retour menu principal <--', str)]


player_tmnt_registering = [('id_tnmt', 'ID tournoi ', str),
                           ('id', 'ID du joueur ', str)]


def display_menu_obj(title, data_menu):
    # display the mneu with an object
    My_menu = MenuPrincipal(title, data_menu)
    My_menu.show()
    My_menu.display_menu()
    option = My_menu.saisie_donne()
    return option


def view_choice(option):
    # display the choice
    print('choix option \'Option\'', option)
    print('')


def data_resquested(title, form_player):
    # request section and using the form object
    data_m = {}
    data_m = Form(title, form_player).show()

    print('fin de saisie')
    return data_m


def option_J1():
    # creation of the new player in db base
    # return to db data type {id, , lastname, firstname, birth, gender, rank, score}
    my_new_player = models.Player_Chess({'id': 1000, 'lastname': "", 'firstname': "", 'birthdate': "", "gender": "M",
                                        'rank': 0, 'score': 0})

    data = data_resquested("Création de joueur", form_player)
    my_new_player.lastname = data['lastname']
    my_new_player.firstname = data['firstname']
    my_new_player.birthdate = data['birthdate']
    my_new_player.gender = data['gender'].upper()
    my_new_player.rank = data['rank']

    return my_new_player.serialized()


def option_player_inscription_tnmt():
    # creation of player

    data = data_resquested("Inscription d'un joueur au tournoi", player_tmnt_registering)

    player_inscription(data)
    result = players_database_list(db='dbplayer_tnmt', sort="")
    print_players_database(result, '', 'Liste des joueurs inscrits')


def option_tnmt_creat():
    # ihm information tournament
    print('choix option \'Option creation tournament\'')
    t_data = {'id': 1000, 'name': "", 'place': ""}
    my_tmnt = models.Tournament(**t_data)
    try:
        data = data_resquested("Ouverture d'un tournoi", tmnt_form)
        my_tmnt.name = data['name']
        my_tmnt.place = data['place']
        my_tmnt.start_date = data["start_date"]
        my_tmnt.end_date = data['end_date']
        my_tmnt.time_control = data['time_control']
        my_tmnt.round_number = 0
        return my_tmnt.serialized_tnmt()

    except ValueError:
        pass


def option3():
    print('choix option \'Option 3\'')


def option4():
    print('mode graphique tkinter activé')
    graphic_mode()


def option10():
    print('choix option \'Option 10\'')


def menu_base():

    while(True):
        print('')

        option = display_menu_obj("Chess Tournament", menu_options)
        # ----------------------------------------
        #         player menu
        # ----------------------------------------
        if option == 1:
            view_choice(option)
            option = ''

            option = display_menu_obj("Menu_joueurs", menu_options_joueurs)

            view_choice(option)
            if option == 1:
                # saisie joueur
                # creation of the player
                data = option_J1()
                player_register(data)

            elif option == 2:
                # modification of player rank
                result = players_database_list(db='dbplayers', sort="")
                print_players_database(result, '')
                id_player = input("saisir l'id du joueur à modifier: ")
                new_rank = input("Saisir le nouveau score de classement: ")
                modify_player(int(id_player), int(new_rank))
                result = players_database_list(db='dbplayers', sort="")
                print_players_database(result, '')

            elif option == 3:
                result = players_database_list(db='dbplayers', sort="")
                print_players_database(result, '')

        # ----------------------------------------
        #         tournament menu
        # ----------------------------------------
        elif option == 2:
            view_choice(option)
            option = ''

            option = display_menu_obj("Menu Tournoi", menu_options_tournois)
            view_choice(option)

            if option == 1:
                # creation tournoi dans la base
                data = option_tnmt_creat()
                tournament_register(data)

            elif option == 2:
                # registering the player into a tournament
                result = players_database_list(db='dbplayers', sort="")
                print_players_database(result, title2='')
                result2 = tmnt_database_list()
                print_tournament_database(result2, 'open', "Tournoi disponible")
                data = option_player_inscription_tnmt()

            elif option == 3:
                # demarrer ou reprendre un tournoi
                result = players_database_list(db='dbplayer_tnmt', sort="")
                print_players_database(result, title2='')
                result2 = int(input("Saisir l'iD du joueur à retirer de la liste :"))
                player_unscription(result2)
                result = players_database_list(db='dbplayer_tnmt', sort="")
                print_players_database(result, title2='')

            elif option == 4:
                # demarrer ou reprendre un tournoi
                main()

        # ----------------------------------------
        #         rapports
        # ----------------------------------------
        elif option == 3:
            option = ''

            option = display_menu_obj("Menu Rapports", menu_options_rapports)

            if option == 1:
                # player sorted by alpah
                result = players_database_list(db='dbplayers', sort="alpha")
                print_players_database(result, 'alpha')

            elif option == 2:
                # player sorted by rank
                result = players_database_list(db='dbplayers', sort="rank")
                print_players_database(result, 'rank')

            elif option == 3:
                # tournament players list alphad sorted
                result = tmnt_database_list()
                print_tournament_database(result, 'all')
                id_tournament = input("Saisir l'id  du tournoi  pour l'affichage des informations :")
                # result2 = players_database_list(db='dbplayer_tnmt', sort="alpha")
                result2 = player_of_tmnt_to_report(int(id_tournament), sort="alpha")
                print_players_database(result2, 'alpha', 'Liste des joueurs inscrit')

            elif option == 4:
                # tournament players list rank sorted

                result = tmnt_database_list()
                print_tournament_database(result, 'all')
                id_tournament = input("Saisir l'id  du tournoi  pour l'affichage des informations :")

                result2 = player_of_tmnt_to_report(int(id_tournament), sort="rank")
                print_players_database(result2, 'rank', 'Liste des joueurs inscrit')

            elif option == 5:
                # all tournament list
                result = tmnt_database_list()
                print_tournament_database(result, 'all')

            elif option == 6:
                # all round of a selected tournament
                result = tmnt_database_list()
                print_tournament_database(result, 'all')
                id_tournament = input("Saisir l'id  du tournoi  pour l'affichage des informations ")
                data_serialized = round_report_by_id(id_tournament, id_name='id_tournament')
                print_round_tmnt_datase(data_serialized, title2="", title="Liste des Round ou Tours")

            elif option == 7:
                # all match of a selected tournament
                result = tmnt_database_list()
                print_tournament_database(result, 'all')
                id_tournament = input("Saisir l'id  du tournoi  pour l'affichage des informations ")
                data_serialized = match_report_with_name(id_value=id_tournament, id_name='id_tournament')
                print_match_tmnt_datase(data_serialized, title2="", title="Liste des match")

        # ----------------------------------------
        #         escape menu
        # ----------------------------------------
        elif option == 4:
            option4()
            # print('Au revoir et Merci !')
            # exit()

        elif option == 5:
            # option5()
            print('Au revoir et Merci !')
            exit()

        elif option == 10:
            print('Au revoir et Merci !')
            exit()
        else:
            print('Invalide option. SVP, entrez un chiffre dans la bonne plage affichée ci dessus.')


if __name__ == '__main__':
    menu_base()
