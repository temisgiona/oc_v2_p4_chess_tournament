import itertools
from operator import itemgetter
from typing import Optional  # , attrgetter


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
    return players_t0 # , a as Optional


def tri_players(players_list):
    """
    tri des joueurs par rang (2) et eventuellement par pt
    du plus grand au plus petit

    """
    c = len(players_list)
        
    d = "A"
    for i in range(c):
        # players_list[i][3] = chr(ord(d) + i)
        players_list[i][3] = chr(ord(d) + i)
        print(players_list[i][3])

    return players_list


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
            if a == 4:
                # round_0_list(i) = [players_list[(i)], players_list[(i+a)]]
                round_0_list.append("E" + str(i+1))
                round_0_list.append(players_list[(i)][3])
                round_0_list.append(players_list[(i+a)][3])
                round_0_list.append(10)
                # print(round_0_list)
    for j in enumerate(round_0_list):
        print(j)

    return round_0_list
    

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
                else :
                    T0[pos_player] = 0
            

            break
    return(T0, a, gain, ind_player2)


def search_player(player_list, player):
    """
    cherche le joueur  dans la liste

    """
    try:
        a = player_list.index(player)  #position juste apres e+1
    
        p_exist = True
        ind_player2 = None
        if player_list[(a-1)][0] == "E" and len(player_list[(a-1)]) == 2:
            "test"
            print(player_list[(a-1)][0])
            b = (a-1)+3
            nom_echiq = player_list[(a-1)]
            pos_play2 = a+1
            ind_player2 = player_list[(a+1)]
            print("Le joueur est trouvé dans l'échiquier", nom_echiq)
            print(player_list)
            

        elif player_list[(a-2)][0] == "E" and len(player_list[(a-2)]) == 2:          # position 2 dans la liste
            "test"
            b = (a-2)+3
            nom_echiq = player_list[(a-2)]
            pos_play2 = a-1
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
    ajouter les points des gagnant dans la fiche joueur

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


def test_search(T0, value = 10):
    """
    test la presence d'une valeur dans la chaine
    pour savoir si il reste des partie a clore
    """
    nb_value = T0.count(value)
    return nb_value


def main():
    """
    """
    players_t0 = players_list()
    players_t0 = tri_players(players_t0)
    print(players_t0)
    
    d = len(players_t0)     
    d = int(d*0.5)
    print(int(d))
    if d is not int:
        print("Creation des parties tour 0")
        T0 = []
        T0 = couple_list_T0(players_t0)

    #  tour0 =  1 quand tous les resultats sont saisi dans le T0_results
    tour0 = 0
    for i in range(d):
        # while tour0 < 1:
        # print("liste round0", T0)
        print(len(T0))
        T0_results, player_indice, pt_gain, player_indice2 = results_T0(T0, d)
        if pt_gain == 0.5:
            player_score_up(players_t0, player_indice, pt_gain)
            player_score_up(players_t0, player_indice2, pt_gain)
            print(T0_results, "le joueur", player_indice, "gagne", pt_gain, "point")
            print(T0_results, "le joueur", player_indice2, "gagne", pt_gain, "point")
        else:
            player_score_up(players_t0, player_indice, pt_gain)

            print(T0_results, "le joueur", player_indice, "gagne", pt_gain, "point")
            print(T0_results, "le joueur", player_indice2, "gagne", 0, "point")
        fin_tour = 0

        nb_free = test_search(T0_results)
        if nb_free < 1:
            tour0 = 1
            print("fin de la partie")
            
        """
        try :
            fin_tour, pos_m, player_indice2 = search_player(T0, 10)
            if fin_tour:
                print("Il reste des parties non saisies")
            else:
                tour0 = 1
        except TypeError :
            print("fin de la partie")
            raise
            """

if __name__ == '__main__':
    main()
