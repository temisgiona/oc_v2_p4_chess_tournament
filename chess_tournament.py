import itertools
from operator import itemgetter  # , attrgetter


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
    return players_t0


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
    scission en 2 groupes de la liste , et 1er de chaque groupe en confrontation et iteration jusqu'au dernier de chaque groupe
    """
    a = len(players_list)

    # base pour recuperer le nombre de parties au tour 0 , nb participants / 2, parties à 1 contre 1'
    a = int(a/2)
    round_0_list = []
    for i in range(a):
        if (a % 2 == 0):
            if a == 4:
                #round_0_list(i) = [players_list[(i)], players_list[(i+a)]]
                round_0_list.append("E"+ str(i+1))
                round_0_list.append(players_list[(i)][3])
                round_0_list.append(players_list[(i+a)][3])
                round_0_list.append(10)
                # print(round_0_list)
    for l in enumerate(round_0_list):
        print(l)

    return round_0_list
    

def results_T0 (T0, d):
    """
    """
    # print("Tour 0 : Donner le nom du joueur gagnant")

    a = input("Tour 0 : Donner l'indice alphabetique du joueur gagnant: ")
    a= a.upper()
    for i in range(int(d)):
        if (a in T0[i]):
            b = input("taper G pour gagnant ou N pour null exaequo ou P: ")
            b = b.upper()
            
            if b == "G":
                "test"
                result_maker = search_player(T0, a)

            elif b == "N":
                "test"
            else:

                b = input("taper G pour gagnant ou N pour null exaequo ou P")
        """else:
            a = input("Tour 0 : Donner le nom du joueur gagnant ou taper exit")
            if a == "exit":
                "test"
            else:
                a = input("Tour 0 : Donner le nom du joueur gagnant ou taper exit")"""

def search_player(player_list, player):
    """
    cherche le joueur  dans la liste

    """
    a = player_list.index(player)
    test = len(player_list[(a-1)])
    if player_list[(a-1)][0] =="E" and len(player_list[(a-1)]) == 2:
        "test"
        print(player_list[(a-1)][0])
        b =(a-1)+3
        player_list[b] = player
        print(player_list)

    elif player_list((a-2))[0] =="E" and len(player_list[(a-1)]) == 2 :          #position 2 dans la liste
        "test"
        b =(a-2)+3
        player_list[b] = player
        print(player_list)
    elif player_list((a-3))[0] == "E" and len(player_list[(a-1)]) == 2 :          # a déjà gagné ! modifier  ?
        "test"
        b =(a-3)+3
        player_list[b] = player
        print(le resultat est modifié par ", player_list)
    else :                                      # le joueur n'existe pas
        "est"
    for p in player_list :
        player_list.index(player)
def score_upgrade(player):
    """
    inscription du score supplementaire dan la fiche du player 

    """
    

def main():
    """
    """
    players_t0 = players_list()
    players_t0 = tri_players(players_t0)
    print(players_t0)

    d = len(players_t0) #/2
    d = d*0.5
    print(int(d))
    if d is not int:
        print("Creation des parties tour 0")
        T0 =[]
        T0 = couple_list_T0(players_t0)

        # print("liste round0", T0)
        print(len(T0))
        e = results_T0(T0, d)
        print(e)

if __name__ == '__main__':
    main()
