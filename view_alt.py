from typing import Any

class console_menu:
    def __init__(self, collection_type: Any):
        self.collection = {}
        self.collection_type = {}


    def display_menu(self):
        for key in self.keys():
           print(key, '--', self[key])
    
    
    def saisie_donne(max_value):
        while(True):
            try:
                option = int(input('Entrez votre choix: '))
                #return option
            except:
                print('Mauvaise saisie ! SVP, entrez un chiffre...')
            if option > max_value:
                print('Mauvaise saisie ! SVP, entrez un chiffre dans la plage')
            else:
                return option




menu_options = {
    1: 'Joueurs',
    2: 'Tournoi',
    3: 'Rapports',
    10: 'Quitter',
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
    10: 'Retour menu principal <--',
}

menu_options_joueurs = {
    1: 'Créer ou inscrire Joueurs',
    2: 'Modifier Joueur',
    3: 'Voir Joueurs',
    10: 'Retour menu principal <--',
}

menu_options_tournois = {
    1: 'Créer Tournoi',
    2: 'Modifier Tournoi',
    3: 'Voir ou Reprendre Tournois',
    10: 'Retour menu principal <--',
}


"""def display_menu(menu):
    for key in menu.keys():
        print(key, '--', menu[key])"""


def option1():
    print('choix option \'Option 1\'')


def option2():
    print('choix option \'Option 2\'')


def option3():
    print('choix option \'Option 3\'')


def option4():
    print('choix option \'Option 10\'')


def option10():
    print('choix option \'Option 10\'')


def saisie_donne(max_value):
    while(True):
        try:
            option = int(input('Entrez votre choix: '))
            #return option
        except:
            print('Mauvaise saisie ! SVP, entrez un chiffre...')
        if option > max_value:
            print('Mauvaise saisie ! SVP, entrez un chiffre dans la plage')
        else:
            return option


def menu_base():
    while(True):
        display_menu(menu_options)
        
        option = saisie_donne(len(menu_options))

        if option == 1:
            option1()
            option = ''
            display_menu(menu_options_joueurs)
            saisie_donne(len(menu_options_joueurs))
            option1()

        elif option == 2:
            option = ''
            
            display_menu(menu_options_tournois)
            saisie_donne(len(menu_options_tournois))
            option2()

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