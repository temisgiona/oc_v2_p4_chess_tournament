from manager_txt import *
from chess_tournament import *
import tournament_controler
from datetime import datetime, date, timedelta



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
    3: "liste de tous les joueurs d'un tournois par ordre alphabetique",
    4: "liste de tous les joueurs d'un tournois par classement",
    5: "liste de tous les joueurs d'un tournois par classement",
    6: "liste de tous les tournois",
    7: "liste de tous les tours d'un tournois",
    8: "liste de tous les match d'un tournois par classement",
    9: 'Retour menu principal <--',
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
    3: 'Voir ou Reprendre Tournois',
    4: 'Retour menu principal <--',
}

menu_options_creation_joueur = {
    1: 'le Nom',
    2: 'le Prénom',
    3: 'le Genre (M ou F)',
    4: 'la date de naissance (AAAA-MM-JJ)',
    5: 'le Rang',
    6: 'Retour menu principal <--',
}

variable_player = {
    1: 'lastname',
    2: 'firstname',
    3: 'gender',
    4: 'birthdate',
    5: 'rank',
    6: 'score',
}

menu_options_creation_tnmt = {
    1: 'le Nom du tournois',
    2: 'le lieu du tournois',
    3: 'la date de début prévue (AAAA-MM-JJ)',
    4: 'la date de fin prévisionnelle (AAAA-MM-JJ)',
    5: 'la gestion du temps ( rapide, eclair ou normal)',
    6:'Retour menu principal <--',
}
variable_tnmt = {
    1: 'name',
    2: 'place',
    3: 'start_date',
    4: 'end_date',
    5: 'time_control',
    6: 'round_number',
    }

menu_options_player_register_tnmt = {
    1: 'le Nom du tournoi',
    2: 'ID tournoi',
    3: 'le nom du joueur',
    4: 'ID du joueur',
    5: 'Retour menu principal <--',
    }

variable_player_register_tnmt = {
    1: 'name',
    2: 'id',
    3: 'name',
    4: 'id',
    } 
    


def display_menu(menu):
    for key in menu.keys():
        print(key, '--', menu[key])

def view_choice(option):
    #display the choice
    print('choix option \'Option\'', option)

def data_resquested(question_list, var_list):
    
    data = {}
    #data[0] = 'id'
    for key in question_list:
        if key == 1:
            # data.append("id": 1000)
            data['id'] = 1000
            
        elif question_list[key] == 'Retour menu principal <--':
            if var_list == variable_player:
                # le score est initialisé à zero
                data[key[6]] = "0"
            elif var_list == variable_tnmt:
                # le nb de round passe a 8 par defaut
                
                if data["start_date"] == "":
                    data['start_date'] = str(date.today())
                    
                    # data['start_date'] = datetime.now()
                    print(data['start_date'])
                    m_date = data['start_date']
                    date_1 = datetime.strptime(m_date, "%y-%m-%d")
                    # end_date = m_date + timedelta(days=4)
                    end_date = (m_date)
                    data['end_date'] = end_date
                data["round_number"] = 8


            print('fin de saisie')
            return data
        print('Saisir', question_list[key])
        my_data = input("test")
        # data[key] = input()
        # data.append(my_data)
        if key == 6 and var_list[key] == 'score':
            data[var_list[key]] = 0
        else :
            data[var_list[key]] = my_data
        
    return data        

def option_J1():
    print('bonjour')
    data = data_resquested(menu_options_creation_joueur, variable_player)
    return data
    
def option_T1():
    #creation of player
    #print('choix option \'Option 1\'')
    
    player_inscription(1)


def option_tnmt_creat():
    #option2():
    #ihm information tournament
    print('choix option \'Option creation tournament\'')
    data = data_resquested(menu_options_creation_tnmt, variable_tnmt)
    return data


def option3():
    print('choix option \'Option 3\'')


def option4():
    print('choix option \'Option 10\'')


def option10():
    print('choix option \'Option 10\'')


def saisie_donne(max_value):
    while(True):
        try:
            choice = int(input('Entrez votre choix: '))
            #return option
        except:
            print('Mauvaise saisie ! SVP, entrez un chiffre...')
        if choice > max_value:
            print('Mauvaise saisie ! SVP, entrez un chiffre dans la plage')
        else:
            return choice


def menu_base():
    while(True):
        display_menu(menu_options)
        
        option = saisie_donne(len(menu_options))
        # ----------------------------------------
        #         player menu
        # ----------------------------------------
        if option == 1:
            view_choice(option)
            option = ''
            display_menu(menu_options_joueurs)
            option = saisie_donne(len(menu_options_joueurs))
            view_choice(option)
            if option == 1:
                # saisie joueur 
                # creation of the player 
                
                data = option_J1()
                player_register(data)
                
        # ----------------------------------------
        #         tournament menu
        # ----------------------------------------
        elif option == 2:
            view_choice(option)
            option = ''
            
            display_menu(menu_options_tournois)
            option = saisie_donne(len(menu_options_tournois))
            view_choice(option)
            if option == 1:
                # creation tournoi dans la base
                data = option_tnmt_creat()
                tournament_register(data)
            elif option == 3:
                # demarrer ou reprendre un tournoi
                main()
                    

        elif option == 3:
            option = ''
            display_menu(menu_options_rapports)
            saisie_donne(len(menu_options_rapports))
            option3()

        elif option == 4:
            option4()
            print('Au revoir et Merci !')
            #exit()

        elif option == 5:
            #option5()
            print('Au revoir et Merci !')
            exit()

        elif option == 6:
            option6()

        elif option == 7:
            option7()

        elif option == 8:
            option8()

        elif option == 10:
            print('Au revoir et Merci !')
            exit()
        else:
            print('Invalide option. SVP, entrez un chiffre dans la bonne plage affichée ci dessus.')


if __name__=='__main__':
    print(chr(27) + '[2J')

    menu_base()