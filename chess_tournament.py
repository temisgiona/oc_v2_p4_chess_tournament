from itertools import combinations, permutations
from operator import itemgetter, attrgetter
from typing import Optional
import tkinter
# from typing_extensions import TypeVarTuple


def players_list():
    """
    list of player for the tournament
    affectation d'un id  compilant , dictionnaire 

    """
    players_t0 = [
        ['t', 'g', 4, 0, 0],
        ['e', 'f', 8, 0, 0],
        ['a', 'b', 3, 0, 0],
        ['k', 'l', 15, 0, 0],
        ['m', 'n', 1000, 0, 0],
        ['o', 'r', 100, 0, 0],
        ['q', 's', 16, 0, 0],
        ['p', 't', 16, 0, 0]
        ]
    a = len(players_t0)
    print("la liste comporte", a, "joueurs")
    return players_t0  # , a as Optional


def tri_players(players_list, column=3):
    """
    affecte un indice alphabetique en vue  du
    tri des joueurs par rang (2) et eventuellement par pt
    du plus grand au plus petit
     
    """
    players_list2 = sorted(players_list, key=itemgetter((column-1)), reverse=True)   
    return players_list2


def assign_id(players_list, column=3):
    """
    assigne ou affecte un indice alphabetique
    en vue de tracer les rencontres facilement
    
    making alphabetical ID to trace the meeting match

    """
    d = "A"
    # si column == 3 le rang du joueur , 
    # pour linstant ca a l'air decalé , comme si il n'y avait pas de zero
    list_ind = []
    for i in range(len(players_list)):
        # players_list[i][3] = chr(ord(d) + i)
        players_list[i][column] = chr(ord(d) + i)
        list_ind.append(chr(ord(d) + i))
        print(players_list[i][column])
    return players_list, list_ind


def tri_players_T1(players_list, column=4):
    """
    affecte un indice alphabetique en vue  du
    tri des joueurs par rang (2) et eventuellement par pt
    du plus grand au plus petit pour les tours suivant T0
     
    """
    players_list2 = sorted(players_list, key=itemgetter((column)), reverse=True)   
    
    return players_list2


def couple_list_T0(players_list):
    """
    création de la liste des joueurs devant s'affronter selon methode tournoi suisse , 
    scission en 2 groupes de la liste , et 1er de chaque groupe en confrontation 
    et iteration jusqu'au dernier du groupe
    """
    a = len(players_list)

    # base pour recuperer le nombre de parties au tour 0 , nb participants / 2, parties à 1 contre 1'
    
    a = int(a/2)
    round_0_list = []
    for i in range(a):
        if (a % 2 == 0):

            round_0_list.append("E" + str(i+1))
            round_0_list.append(players_list[(i)][3])
            round_0_list.append(players_list[(i+a)][3])
            round_0_list.append(10)
            # print(round_0_list)
    for j in enumerate(round_0_list):
        print(j)

    return round_0_list
    

def couple_list_T1_write(T1, player1, player2):
    """
    rempli la liste T1 des joueurs devant s'affronter selon methode tournoi suisse , 
    2eme partie

    """
    a = len(T1)

    # base pour recuperer le nombre de parties au tour 0 , nb participants / 2, parties à 1 contre 1'
    # a = int(a/2)
    # T1 = []
    
        
    if (a % 2 == 0):
        T1.append("E" + str(int(a/4+1)))
        T1.append(player1)
        T1.append(player2)
        T1.append(10)
    else: 
        print("erreur sur la liste T1")
                
    for j in enumerate(T1):
        print(j)

    return T1


def results_T0(T0, d):
    """
    recupere la saisie du  resultat  du gagnant
    jusqu'a ce que tous les gagnants soient saisi
    """
    # print("Tour 0 : Donner le nom du joueur gagnant")

    a = input("Tour 0 : Donner l'indice alphabetique du joueur gagnant : ")
    a = a.upper()
    gain = 0
    dl = len(T0)
    for pos in range(dl):
        if (a == T0[pos]):
            while gain < 0.5:
                b = input("taper G pour gagnant ou N pour null ex-aequo : ")
                b = b.upper()
                gain = 0
                
                if b == "G":
                    "test"
                    # result_maker = search_player(T0, a)
                    gain = 1
                    
                if b == "N":
                    gain = 0.5

            player_exist, pos_player, ind_player2 = search_player(T0, a)
            if player_exist:
                
                if b == 'G':
                    T0[pos_player] = a
                else:
                    T0[pos_player] = 0
            break
    return(T0, a, gain, ind_player2)


def search_player(player_list, player):
    """
    cherche le joueur  dans la liste

    """
    try:
        a = player_list.index(player)  # position juste apres e+1
    
        p_exist = True
        ind_player2 = None
        if player_list[(a-1)][0] == "E" and len(player_list[(a-1)]) == 2:
            "test"
            print(player_list[(a-1)][0])
            b = (a-1)+3
            nom_echiq = player_list[(a-1)]
            # pos_play2 = a+1
            ind_player2 = player_list[(a+1)]
            print("Le joueur est trouvé dans l'échiquier", nom_echiq)
            print(player_list)

        elif player_list[(a-2)][0] == "E" and len(player_list[(a-2)]) == 2:          # position 2 dans la liste
            "test"
            b = (a-2)+3
            nom_echiq = player_list[(a-2)]
            # pos_play2 = a-1
            ind_player2 = player_list[(a-1)]
            print(player_list)
            print("Le joueur est trouvé dans l'échiquier", nom_echiq)
            
        elif player_list[(a-3)][0] == "E" and len(player_list[(a-3)]) == 2:          # a déjà gagné ! modifier  ?
            "test"
            b = (a-3)+3
            if a == 10:
                print("le tour n'est pas fini")

            else:
                
                print("le résultat est modifié par ", player_list)
            
        return(p_exist, b, ind_player2 if ind_player2 else None)

    except ValueError:
        print("le tour est fini")
        p_exist = False
        return(p_exist)


def player_score_up(players_t0, player_indice, pt_gain):
    """
    upgrade score player 
    ajoute les points des gagnants dans la fiche joueur

    """
    array_pos = search_player_by_indice(players_t0, player_indice)
    players_t0[array_pos][4] = +pt_gain
    return players_t0


def search_player_by_indice(players_t0, player_indice):
    """
    cherche le joueur selon son identifiant alphabetique
    """
    r = len(players_t0)
    for i in range(r):
        if player_indice == players_t0[i][3]:
            player_pos = i
            return player_pos


def test_search(T0, value=10):
    """
    test la presence d'une valeur dans la chaine
    pour savoir si il reste des partie a clore
    """
    nb_value = T0.count(value)
    return nb_value


def read_player_file():
    """
    lecture de la fiche joueur  et comptage de point
    """


def round_tournament(player_lists, list_tmp_tournament,T0_results, col=3):
    """
    algo deroulement du tournoi sur la base des points accumulés au fur a mesure des parties
    
    """
    T1 = []
    T1.extend(T0_results)
    player_lists2 = tri_players_T1(player_lists)
    print(player_lists2)
    j=1
    while(len(player_lists2)) >= 2:
        i= 0    
    
        j = +1
        if  test_couple_ind(list_tmp_tournament,player_lists2[i][col],player_lists2[j][col]) is False:
            
            T1 = couple_list_T1_write(T1, player_lists2[i][col], player_lists2[j][col])
            list_tmp_tournament = add_couplelist(list_tmp_tournament, player_lists2[i][col], player_lists2[j][col])
            player_lists2.pop(j)
            player_lists2.pop(i)
            i = 0

        else :
            
            j = +1
    return T1,list_tmp_tournament
    

              

def permutation_cpl(iterable, r=2):
    """
    creation of the iteration about to listing all possibilities of meeting in the tournament
    """
    n = len(iterable)
    my_list = []
    # my_list = list(combinations(iterable, r))
    my_list = list(permutations(iterable, r))
    for i in range(len(my_list)):
        my_list[i] = my_list[i][0] + my_list[i][1]
    return my_list 


def add_couplelist(T0_list, player1, player2):
    """
    create the list and add couple of player
    remplace combination
    read T0 an extract couple
    make a list after round  0

    """
    if len(T0_list) == 0:
        T0_list =[]
    T0_list.append(player1 + player2)
    T0_list.append(player2 + player1)
    return T0_list


def test_couple_ind(my_list, ind_1, ind_2):
    """
    this section is checking if the couple exists in the meeting_list
    if yes it returns true

    """
    ind_3 = ind_1+ind_2
    try:
        # for i in range(len(my_list)):
        if my_list.index(ind_3) >= 0:
            print("ok")
            return True
    except:
        print("not ok")
        return False

def score_up(players_T0, player1, player2, gain):
    """
    send message for the statut of score added for player
    """
    if gain == 0.5:
            player_score_up(players_T0, player1, gain)
            player_score_up(players_T0, player2, gain)

    else:
        player_score_up(players_T0, player1, gain)

    print("le joueur", player1, "gagne", gain, "point")
    if gain == 0.5:
        print("le joueur", player2, "gagne", gain, "point")
    return players_T0


def deroulement(T_round,list_ind_tournament):
    """

    """
    tour0 = 0
    
    while tour0 < 1:
        # print("liste round0", T0)
        print(len(T_round))
        T0_results, player_indice, pt_gain, player_indice2 = results_T0(T_round, d)
        list_ind_tournament = add_couplelist(list_ind_tournament, player_indice, player_indice2)
        players_t0 = score_up(players_t0, player_indice, player_indice2, pt_gain)
        nb_free = test_search(T0_results)
        if nb_free < 1:
            tour0 = 1
            print("fin de la partie")
            print(players_t0)

def show_about():
    
    # about_window = tkinter.Toplevel(app)
    about_window = tkinter.Toplevel()
    about_window.title("A propos")
    lb = tkinter.Label(about_window, text="\n écrit et conçu par: \n TGIONA pour OpenclassRooms prj4! \n Tous droits reservés 2021.")
    lb.pack()

def window_menu():

    # Création de la fenetre  + parametrage

    app = tkinter.Tk()
    app.geometry("640x480")
    app.title("Chess Tournament Master")


    # Widgets...
    mainmenu = tkinter.Menu(app)
    first_menu = tkinter.Menu(app,tearoff=0)

    first_menu.add_command(label="Création tournoi")
    first_menu.add_command(label="Saisie des résultats")
    first_menu.add_separator()
    first_menu.add_command(label="Quitter", command=app.quit)

    second_menu = tkinter.Menu(mainmenu, tearoff=0)
    second_menu.add_command(label="Impression résultats")
    second_menu.add_command(label="Mode texte")
    second_menu.add_command(label="A propos", command=show_about)

    mainmenu.add_cascade(label="Tournoi", menu=first_menu)
    mainmenu.add_cascade(label="Divers", menu=second_menu)

    # Boucle prinicpale
    app.config(menu=mainmenu)
    app.mainloop()


def main():
    """
    """
    players_t0 = players_list()
    players_t0 = tri_players(players_t0)
    list_ind = []
    list_ind_tournament = [] 
    players_t0, list_ind = assign_id(players_t0)

    window_menu()
    # list_ind__tournament = permutation_cpl(list_ind)
    # print(list_ind__tournament)
    # test_couple_ind(list_ind_tournament, 'A','Z')
    print(players_t0)
    
    d = (len(players_t0))*0.5
    # d = (d*0.5)
    # print(d)
    if (d % 2) == 0:        # test si d est paire via le modulo == 0
    #  if d is int:
        print("Creation des parties tour 0")
        T0 = []
        T0 = couple_list_T0(players_t0)

    #  tour0 =  1 quand tous les resultats sont saisi dans le T0_results
    tour0 = 0
    
    while tour0 < 1:
        # print("liste round0", T0)
        print(len(T0))
        T0_results, player_indice, pt_gain, player_indice2 = results_T0(T0, d)
        list_ind_tournament = add_couplelist(list_ind_tournament, player_indice, player_indice2)
        players_t0 = score_up(players_t0, player_indice, player_indice2, pt_gain)
        nb_free = test_search(T0_results)
        if nb_free < 1:
            tour0 = 1
            print("fin de la partie")
            print(players_t0)
        
    T1, list_ind_tournament = round_tournament(players_t0, list_ind_tournament, T0_results)
    print(T1)
    deroulement(T1, list_ind_tournament)
            

if __name__ == '__main__':
    main()
