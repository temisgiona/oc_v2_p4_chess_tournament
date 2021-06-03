import itertools
from operator import itemgetter  # , attrgetter


def players_list():
    """
    list of player for the tournament
    affectation d'un id  compilant , dictionnaire 

    """
    players_t0 = [
        ['t', 'g', 4, 3],
        ['e', 'f', 8, 2],
        ['a', 'b', 3, 1],
        ['k', 'l', 15, 0],
        ['m', 'n', 1000, 0],
        ['o', 'r', 100, 0],
        ['q', 's', 16, 2],
        ['p', 't', 16, 3]
        ]
    a = len(players_t0)
    print("la liste comporte", a, "joueurs")
    return players_t0


def tri_players(players_list):
    """
    """
    c = sorted(players_list, key=itemgetter(2, 3), reverse=True)
    return c

def couple_list_T0(players_list):
    """
    """
    a = len(players_list)

    # base pour recuperer le nombre de parties au tour 0 , nb participants / 2, parties à 1 contre 1'
    a = int(a/2)
    
    for i in range(a):
        if a == 4:
            round_0 = (players_list[(i)], players_list[(i+a)])
            print(round_0)


def main():
    """
    """
    players_t0 = players_list()
    players_t0 = tri_players(players_t0)
    print(players_t0)

    d = (int(len(players_t0)))  #/2
    d = d*0.5
    print(int(d))
    if d is not int:
        print("Creation des parties tour 0")
        T0 = (couple_list_T0(players_t0))


if __name__ == '__main__':
    main()

