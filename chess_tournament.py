from itertools import combinations, count, permutations
from operator import itemgetter, attrgetter
from typing import Optional
import tkinter
import time

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
    rempli la liste scenario de tournoi T1 des joueurs devant s'affronter 
    (méthode tournoi suisse) 
    2eme partie
    saisi du numero chronologique d'echiquier  puis du player 1 et du player 2

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
        print("erreur sur la liste Tournoi secondaire")
    return T1


def results_T0(T0, round=0):
    """
    recupere la saisie du  resultat  du gagnant
    jusqu'a ce que tous les gagnants soient saisi
    """
    # print("Tour 0 : Donner le nom du joueur gagnant")
    player_exist = False

    while player_exist is False:
        ind_player_1 = (input("Tour "+ str(round) + " : Donner l'indice alphabétique du joueur gagnant : ")).upper()
        player_exist = search_player(T0, ind_player_1)
        #print("Ce joueur n'a pas été trouvé ! ")
    gain = 0
    dim_list = len(T0)
    for pos in range(dim_list):
        if (ind_player_1 == T0[pos]):
            while gain < 0.5:
                b = input("taper G pour gagnant ou N pour null ex-aequo : ")
                b = b.upper()
                gain = 0
                
                if b == "G":
                    "test"
                    # result_maker = search_player(T0, a)
                    gain = 1
                    
                elif b == "N":
                    gain = 0.5
                
                else:
                    b = "G"
                    gain = 1
            
            player_exist, pos_result, ind_player_2 = search_player(T0, ind_player_1, round)
            if player_exist:
                
                if b == 'G':
                    T0[pos_result] = ind_player_1
                else:
                    T0[pos_result] = 0
                break
            else:
                print("le joueur n'a pas été trouvé ! ")
    return(T0, ind_player_1, gain, ind_player_2)


def search_player(player_list, player, round=0):
    """
    cherche le joueur  dans la liste

    """
    try:
        if round > 0:
            start_search = round * 4 * 4
        else:
            start_search = 0

        end_list = len(player_list)-1
        # a = player_list.index(player[start_search:end_list])  # position juste apres e+1
        a = player_list.index(player, start_search, end_list)  # position juste apres e+1
    
        p_exist = True
        ind_player2 = None
        if player_list[(a-1)][0] == "E" and len(player_list[(a-1)]) >= 2:
            "test"
            # print(player_list[(a-1)][0])
            b = (a-1)+3
            nom_echiq = player_list[(a-1)]
            # pos_play2 = a+1
            ind_player2 = player_list[(a+1)]
            print("Le joueur", ind_player2, "est trouvé dans l'échiquier", nom_echiq)
            #print(player_list)

        elif player_list[(a-2)][0] == "E" and len(player_list[(a-2)]) >= 2:          # position 2 dans la liste
            "test"
            b = (a-2)+3
            nom_echiq = player_list[(a-2)]
            # pos_play2 = a-1
            ind_player2 = player_list[(a-1)]
            #print(player_list)
            print("Le joueur", ind_player2, "est trouvé dans l'échiquier", nom_echiq)
            
        elif player_list[(a-3)][0] == "E" and len(player_list[(a-3)]) >= 2:          # a déjà gagné ! modifier  ?
            "test"
            b = a
            if a == 10:
                print("le tour n'est pas fini")

            else:
                print("le résultat est modifié par ", player_list)
                b = 0
        pos_result = b
            
        return(p_exist, pos_result, ind_player2 if ind_player2 else None)

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
    players_t0[array_pos][4] = players_t0[array_pos][4] + pt_gain
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


def round_tournament(player_lists, list_tmp_tournament, T0_results, round=0, col=3):
    """
    algo deroulement du tournoi sur la base des points accumulés au fur a mesure des parties
    
    """
    T1 = []  # liste des parties apres le 1er tour avec appariement par  piorité resultats
    T1.extend(T0_results)
    player_lists2 = tri_players_T1(player_lists)
    couple_list_temp = []
    couple_list_temp2 = []
    list_temp = []
    list_temp3 = []
    list_combinaison2 = []
    list_classement = []
    list_temp4b = []
    print(player_lists2)

    for i in range(len(player_lists)):
        list_temp.append(player_lists[i][col])

    list_temp2 = list(combinations(list_temp, 2))

    list_temp3 = ["".join(item) for item in list_temp2]

    for i in range(len(list_temp3)):
        if test_couple_ind_all(list_tmp_tournament, list_temp3[i]) is False: 
            couple_list_temp2.append(list_temp3[i])

    list_combinaison = list(combinations(list_temp3, int(len(player_lists2)/2))
    start = time.time()
    for item in range(len(list_combinaison)):
        var_temp401 = ""

        list_temp4 = list_combinaison[item]

        for item2 in list_temp4:
            var_temp401 = var_temp401 + item2
        list_temp6 = set(var_temp401)

        if len(var_temp401) == len(list_temp6):
            list_combinaison2.append(list_combinaison[item])
        #list_temp6 = set(list_temp401)
        #list_temp4b = [.split(item) for item in list_combinaison]
    
    end = time.time()
    print("la fonction a pris : ", end - start, "s")
    
    list_combinaison_charg = []
    for i in range(len(list_combinaison2)):
        point_echiquier_total = 0
        liste_advers = list(list_combinaison2[i])
        for j in liste_advers:
            
            player1 = j[0]
            player2 = j[1]
            
            for players in range(len(player_lists2)):
                if player1 == player_lists2[players][3]:
                    point_player1 = player_lists2[players][4] + (player_lists2[players][4]/1000)
                if player2 == player_lists2[players][3]:
                    point_player2 = player_lists2[players][4] + (player_lists2[players][4]/1000)
            
            point_ech_partiel = point_player1 * point_player2
            point_echiquier_total = point_echiquier_total + point_ech_partiel

        liste_advers.append(point_echiquier_total)
        list_combinaison2[i] = liste_advers
    
    list_combinaison_charg = tri_players_T1(list_combinaison2, 4)
    print("fin de calcul_echiquier")
    for i in range(int(len(player_lists)/2)):
        players = (list_combinaison_charg[0])[i]
        T1 = couple_list_T1_write(T1, players[0], players[1])
        list_tmp_tournament = add_couplelist(list_tmp_tournament, players[0], players[1])
    return T1, list_tmp_tournament


def round_tournament2(player_lists, list_tmp_tournament, T0_results, round=0, col=3):
    """
    algo deroulement du tournoi sur la base des points accumulés au fur a mesure des parties
    
    """
    T1 = []  # liste des parties  avec appariement par  piorité resultats
    T1.extend(T0_results)
    player_lists2 = tri_players_T1(player_lists)
    couple_list_temp = []
    print(player_lists2)
    i = 0
    j = 0
    k = 0
    #couple_list_temp = 

    while(len(player_lists2)) >= 2:
        
        for i in range(int((len(player_lists2))/2)-1):
            
            for j in range(len(player_lists2)-1):
                
                if j <= (len(player_lists2)-1):
                    i = i+1
                else:
                    print("en cours de resolution")

                if test_couple_ind(list_tmp_tournament, player_lists2[i][col], player_lists2[j][col]) is False:
                    if player_lists2[i][col] != player_lists2[j][col]:
                        couple_list_temp.append(player_lists2[i][col] + player_lists2[j][col])
                    #else :
                        
                    
                    T1 = couple_list_T1_write(T1, player_lists2[i][col], player_lists2[j][col])
                    list_tmp_tournament = add_couplelist(list_tmp_tournament, player_lists2[i][col], player_lists2[j][col])
                    
                    # player_lists2.pop(j)
                    if j == len(player_lists2): 
                        
                        player_lists2.pop(i)
                        #i = 0

            else:
                k = k + 1
                j += 1
                if k == 4:
                # 4 = valeur nb_chess pour les test
                    print("erreur de resolution")
            
    return T1, list_tmp_tournament
    

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
        T0_list = []
    T0_list.append(player1 + player2)
    T0_list.append(player2 + player1)
    return T0_list


def test_couple_ind(my_list, player_ind_1, player_ind_2):
    """
    this section is checking if the couple exists in the meeting_list
    if yes it returns true
    if not   error retuned  so the association has the agrement

    """
    
    couple_player = player_ind_1 + player_ind_2
    try:
        # for i in range(len(my_list)):
        if my_list.index(couple_player) >= 0:
            print("ok")
            return True
    except:
        print("le couple", couple_player, "n'a pas joué ensemble")
        
        return False


def test_couple_ind_all(my_list, couple_player):
    """
    
    this section is checking if the couple exists in the meeting_list
    if yes it returns true
    if not   error retuned  so the association has the agrement
    """
    try:
        # for i in range(len(my_list)):
        if my_list.index(couple_player) >= 0:
            #print("ok")
            return True
    except:
        #print("le couple", couple_player, "n'a pas joué ensemble")
        
        return False
    


def score_up(players_T0, player1, player2, gain):
    """
    send message for the statut of score added for player
    """
    if gain == 0.5:
        player_score_up(players_T0, player1, gain)
        player_score_up(players_T0, player2, gain)

        print("le joueur", player1, "gagne", gain, "point")
        print("le joueur", player2, "gagne", gain, "point")
    else:
        player_score_up(players_T0, player1, gain)

        print("le joueur", player1, "gagne", gain, "point")
        print("le joueur", player2, "gagne 0 point")
    
    return players_T0


def deroulement(players_t0, T_round, list_ind_tournament, nb_chess, round):
    """

    """
    nb_free = 1
    
    while nb_free > 0:
        # print("liste round0", T0)
        print(len(T_round))
        print(T_round)
        T0_results, player_indice, pt_gain, player_indice2 = results_T0(T_round, round)
        list_ind_tournament = add_couplelist(list_ind_tournament, player_indice, player_indice2)
        players_t0 = score_up(players_t0, player_indice, player_indice2, pt_gain)
        nb_free = test_search(T0_results)  # trying to find "10", is the flag to chess party is not 
    print("fin de la partie Round " + str(round))
    # print(players_t0)
    for i in range(len(players_t0)):
        print(players_t0[i])

    return T0_results, list_ind_tournament


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
    first_menu = tkinter.Menu(app, tearoff=0)

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

    #  window_menu()
    # list_ind__tournament = permutation_cpl(list_ind)
    # print(list_ind__tournament)
    # test_couple_ind(list_ind_tournament, 'A','Z')
    print(players_t0)
    
    nb_chess = int((len(players_t0))*0.5)   # ex d
    T0 = []
    T1 = []
    if (nb_chess % 2) == 0:        # test si nb_chess est paire via le modulo == 0
    
        for round in range(nb_chess):    
            print("Creation des parties tour " + str(round))
            if round == 0:
                
                T0 = couple_list_T0(players_t0)
                # T0_results, player_indice, pt_gain, player_indice2 = results_T0(T0, nb_chess)
                T0_results, list_ind_tournament = deroulement(players_t0, T0, list_ind_tournament, nb_chess, round)
            else:
                if len(T1) > 16:

                    T1, list_ind_tournament = round_tournament(players_t0, list_ind_tournament, T1, round)
                    
                    T1_temp = T1[:]
                    del T1_temp[0:15]
                    print(T1_temp)
                else:
                    T1, list_ind_tournament = round_tournament(players_t0, list_ind_tournament, T0_results, round)
                
                deroulement(players_t0, T1, list_ind_tournament, nb_chess, round)

            #  tour0 =  1 quand tous les resultats sont saisi dans le T0_results
            #tour0 = 0

    else:
        exit
            

if __name__ == '__main__':
    main()
