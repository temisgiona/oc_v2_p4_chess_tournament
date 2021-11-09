from itertools import combinations, count
from operator import itemgetter, attrgetter
from typing import Optional
from pydantic import BaseModel
from tinydb import *
from tinydb import database
from manager_txt import Manager
import models
from view import *
from view_chess_tk import maintk
from rapport import *
from datetime import date

# from time import time
global DATAPATH
global DB_PLAYERS
global DB_PLAYER_TNMT
global DB_TOURNAMENTS
global DB_MATCH_TMNT

DATAPATH = './data_players2.json'
DB_PLAYERS = 'players_list'
DB_PLAYER_TNMT = 'players_tournament'
DB_TOURNAMENTS = 'tournaments'
DB_MATCH_TMNT = 'match'


def set_global_var():
    global DATAPATH
    global DB_PLAYERS
    global DB_PLAYER_TNMT
    global DB_TOURNAMENTS

    DATAPATH = './data_players2.json'
    DB_PLAYERS = 'players_list'
    DB_PLAYER_TNMT = 'players_tournament'
    DB_TOURNAMENTS = 'tournaments'


def player_register(data):
    player_manager = Manager(DATAPATH, DB_PLAYERS)
    player_manager.data_insert(data)
    player_manager.id_readjust()


def modify_player():
    # to modify the rank of the player
    print("a finir")


def match_db_update(t_round, players_t0, round):
    # update the db tmnt by match making
    # create linear list of _macth to a list of list of all match
    match_tmnt_manager = Manager(DATAPATH, DB_MATCH_TMNT)
    match_data_formated = match_tmnt_database_list(t_round, players_t0, round)

    match_serialized_list = match_tmnt_manager.match_db_serialising(match_data_formated)
    
    m_data = match_tmnt_manager.match_querying_by_id(2, 'id_tournament')


def match_tmnt_database_list(t_round, players_t0, round, nb_match=4,  play1_result="", play2_result="", st_date="", end_date=""):
    # 
    data_round_list = []
    data_round = []
    """for dat in range(13):
        data_round.append(0)"""
        
    nb_match_t = int(len(t_round)/4)
    nb_round = int(len(players_t0)/2)
    
    """
    for item in range(13):
        data_round.append(0)
        data_round[item] = ""
        """
    a = 0

    """for it in range(nb_match_t):
        data_round_list.append(0)"""
    match = 0
    start_round = round * nb_match * nb_round
    for a in range(start_round, len(t_round), nb_match):

        if t_round[a+3] != 10:
            data_round_list.append(0)
            
            for item in range(13):
                data_round.append("")
                # data_round[item] = ""
            data_round[0] = 1 + int(a/nb_match)
            data_round[1] = round
            data_round[2] = players_t0[search_player_by_indice(players_t0, t_round[a+1])][6]              # id_tnmt
            data_round[3] = t_round[a]      # name
            
            data_round[4] = players_t0[search_player_by_indice(players_t0, t_round[a+1])][5]              # player1
            data_round[5] = players_t0[search_player_by_indice(players_t0, t_round[a+2])][5]              # player2
            data_round[6] = t_round[a+1]
            data_round[7] = t_round[a+2]
            if t_round[a+3] == 0:
                data_round[8] = 0.5
                data_round[9] = 0.5
            elif t_round[a+3] == t_round[a+1]:
                data_round[8] = 1
                data_round[9] = 0
            elif t_round[a+3] == t_round[a+2]:
                data_round[8] = 0
                data_round[9] = 1
            else:
                data_round[8] = ""
                data_round[9] = ""

            if data_round[10] == "":
                data_round[10] = str(date.today())
            if t_round[a+3] != 10:
                data_round[11] = str(date.today())

            else:
                data_round[11] = ""
            data_round[12] = ""
            
            data_round_list[match] = data_round.copy()
            match += 1

        
        
    return data_round_list


def query_id_open_state_tnmt():
    # query id tnmt with statut open 
    
    tnmt_manager = Manager(DATAPATH, DB_TOURNAMENTS)
    query_tmnt = tnmt_manager.search_to_tiny_is_open()
    id_tmnt = query_tmnt[0]["id"]
    return id_tmnt


def assign_id_tnmt(players_t0):
    # assign id tnmt with state open to player list
    id_tmnt = query_id_open_state_tnmt()
    for row in range(len(players_t0)):
        players_t0[row][6] = id_tmnt
    
    return(players_t0)
    

def player_inscription(data):
    # writing the list of player for the game
    # send to players_t0  the player ready for the tournament

    players_list_init = []
    player_manager_tnmt = Manager(DATAPATH, DB_PLAYER_TNMT)
    player_manager = Manager(DATAPATH, DB_PLAYERS)
    tnmt_manager = Manager(DATAPATH, DB_TOURNAMENTS)

    try:
        player_query = player_manager.search_to_tinydb_by_id(int(data['id']))
        tmnt_query = tnmt_manager.search_to_tinydb_by_id(int(data['id_tnmt']))
        player_query_tmnt = player_manager_tnmt.search_to_tinydb_by_id(int(data['id']))

        if len(player_query) == 1 and len(tmnt_query) == 1:
            if len(player_query_tmnt) > 0:
                print("ce joueur est déjà inscrit !")
            # on transfere les données de la base player en la formattant
            else:
                player_query_serialised = player_manager.serialize_query(player_query)
                player_manager_tnmt.data_insert(player_query_serialised)

        else:
            print("valeur absente")
    except ValueError:
        print("valeur absente")
        raise
    
    # player_manager_tmnt.id_readjust()


def players_list_old():
    """
    list of player for the tournament
    affectation d'un id  compliant , dictionnaire 

    """
    players_t0 = []
    # players_t0.append(player_tnmt)

    # player [lastname, firstname, rank, score, ind, id,id tournament]
    # """if len(players_t0) < 3:  
    players_t0 = []
    
    players_t0 = [
        ['temis', 'giona', 4, 0, 0, 0],
        ['eric', 'fortunato', 8, 0, 0, 0],
        ['a', 'b', 3, 0, 0, 0],
        ['k', 'l', 15, 0, 0, 0],
        ['m', 'n', 1000, 0, 0, 0],
        ['o', 'r', 100, 0, 0, 0],
        ['q', 's', 16, 0, 0, 0],
        ['p', 't', 16, 0, 0, 0]
        ]
        
    a = len(players_t0)
    print("la liste comporte", a, "joueurs inscrits")
    # print_row_tab_player(players_t0)
    return players_t0  # , a as Optional


def players_database_list(db='dbplayers', sort=""):
    # catch list player in a db , and sorted by
    # alphabetical name , rank or by chronology
    if db == 'dbplayers':
        database_name = DB_PLAYERS
    elif db == 'dbplayer_tnmt':
        database_name = DB_PLAYER_TNMT
    
    player_manager = Manager(DATAPATH, database_name)
    players_all_db = []
    players_all_db = player_manager.players_all_data_serialized()
    if sort == 'alpha':
        # alphabetical name sorted
        players_alpha_sorted = sorted(players_all_db, key=itemgetter(1, 5))
        return players_alpha_sorted
    elif sort == 'rank':
        # rank  sorted
        players_rank_sorted = sorted(players_all_db, key=itemgetter(5, 0), reverse=True)
        return players_rank_sorted
    else:
        # not sorted, or sorted by id
        players_all_db
    # print(players_all_db)
        return players_all_db


def tmnt_database_list():
    tmnt_manager = Manager(DATAPATH, DB_TOURNAMENTS)
    tmnt_all_db = []
    tmnt_all_db = tmnt_manager.tmnt_all_datadb_serialized()
    return tmnt_all_db


def tmnt_match_database_serialising(data):
    # send info to the database
    tmnt_match_manager = Manager(DATAPATH, DB_MATCH_TMNT)
    tmnt_match_manager.match_db_serialising(data)


def update_math_db(T0_s, players_t0):
    # update the match base 
    print("test match_update")


def tmnt_match_database_to_matchmaking():
    # send info to the database
    tmnt_match_manager = Manager(DATAPATH, DB_MATCH_TMNT)
    tmnt_match_manager.match_db_unserialising()


def match_report_with_name(id_value=23, id_name='id'):
    # mastering data for displaying information with the name of player

    match_with_name = []
    match_with_name_list = []
    match_tmnt_manager = Manager(DATAPATH, DB_MATCH_TMNT)
    # m_data = match_tmnt_manager.match_querying_by_id(2, 'id_tournament')
    m_data = match_tmnt_manager.match_querying_by_id(id_value, id_name)
    for play in range(len(m_data)):
        my_match = models.Match(**m_data[play])
        print(my_match.name)
        player_manager = Manager(DATAPATH, DB_PLAYERS)
        my_player_data1 = player_manager.search_to_tinydb_by_id(my_match.player1_id)
        my_player_data2 = player_manager.search_to_tinydb_by_id(my_match.player2_id)

        my_player1 = models.Player(**my_player_data1[0])
        my_player2 = models.Player(**my_player_data2[0])

        match_with_name = match_tmnt_manager.match_object_db_unserialising(my_match)
        
        match_with_name[0][4] = my_player1.lastname + " " + my_player1.firstname
        match_with_name[0][5] = my_player2.lastname + " " + my_player2.firstname
        
        match_with_name_list.append(*match_with_name)

    return match_with_name_list
 

def players_list():
    # catch the player document in db to list for match making
    player_manager_tmnt = Manager(DATAPATH, DB_PLAYER_TNMT)
    players_t0_tmnt = []

    players_t0_tmnt = player_manager_tmnt.player_serialized()

    # print(players_t0_tmnt)
    return players_t0_tmnt


def player_update_to_db(players_T0):
    # update the score to the db with manager
    # print("test")
    player_tmnt_manager = Manager(DATAPATH, DB_PLAYER_TNMT)
    
    for row in range(len(players_T0)):
    
        player_tmnt_manager.update_player_tmnt(players_T0[row])


def tournament_register(data):
    # to create the database with data from view
    tnmt_manager = Manager(DATAPATH, DB_TOURNAMENTS)
    tnmt_manager.data_tmnt_insert(data)
    tnmt_manager.id_readjust()


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
        # affichage debug
        # print(players_list[i][column])
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
    tab_round_all_match = []
    a = int(a/2)
    round_0_list = []
    round_0_listb = []
    for i in range(a):
        if ((len(players_list)) % 2 == 0):

            round_0_list.append("E" + str(i+1))
            round_0_list.append(players_list[(i)][3])
            round_0_list.append(players_list[(i+a)][3])
            round_0_list.append(10)
            # print(round_0_list)
        if (a % 4 == 0):
            # second_list to remplace  T0
            round_0_listb.append("E" + str(i+1))
            round_0_listb.append(players_list[(i)][3])
            round_0_listb.append(players_list[(i+a)][3])
            round_0_listb.append(10)
            round_0_listb.append(players_list[(i)][0])
            round_0_listb.append(players_list[(i+a)][0])
            round_0_listb.append(1)                         # this the round number
            tab_round_all_match.append(round_0_listb)
            round_0_listb = []
    """for j in enumerate(round_0_list):
        print(j)"""
    return round_0_list, tab_round_all_match


def convert_T0_2_T0_s(T0, T0_s, players_t0, round):
    # convert T0 (linear list) to  list of list with more information
    a = len(T0)
    tab_round_all_match = []
        
    round_0_listb = []
    j = 0
    for i in range(0, a, 4):
        
        if (i % 4 == 0):
            j = int(i/4)   # 1 match of T0 is writed with 4 elements
            # second_list to remplace  T0
            round_0_listb.append(T0[i])
            round_0_listb.append(T0[i+1])
            round_0_listb.append(T0[i+2])
            round_0_listb.append(T0[i+3])
            p_name1 = search_player_by_indice(players_t0, T0[i+1])
            name1 = players_t0[p_name1][0]
            p_name2 = search_player_by_indice(players_t0, T0[i+2])
            name2 = players_t0[p_name2][0]
            round_0_listb.append(name1)
            round_0_listb.append(name2)
            round_0_listb.append(round+1)                         # this is the round number
            tab_round_all_match.append(round_0_listb)
            round_0_listb = []
    return tab_round_all_match


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
    T1_s = []
        
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
        ind_player_1 = (input("Tour " + str(round+1) + " : Donner l'indice alphabétique du joueur gagnant : ")).upper()
        player_exist = search_player(T0, ind_player_1, round)
        """#print("Ce joueur n'a pas été trouvé ! ")"""
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


def results2_T0(T0, round=0):
    """
    recupere la saisie du  resultat  du gagnant
    jusqu'a ce que tous les gagnants soient saisi
    """
    # print("Tour 0 : Donner le nom du joueur gagnant")
    player_exist = False

    while player_exist is False:
        ind_player_1 = (input("Tour " + str(round+1) + " : Donner l'indice alphabétique du joueur gagnant : ")).upper()
        player_exist = search_player(T0, ind_player_1, round)

        """#print("Ce joueur n'a pas été trouvé ! ")"""
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
        nb_round = int(len(player_list)/4)
        nb_round = int(nb_round/(round+1))
        if round > 0:
            
            start_search = round * 4 * nb_round
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
            # print(player_list)

        elif player_list[(a-2)][0] == "E" and len(player_list[(a-2)]) >= 2:          # position 2 dans la liste
            "test"
            b = (a-2)+3
            nom_echiq = player_list[(a-2)]
            # pos_play2 = a-1
            ind_player2 = player_list[(a-1)]
            # print(player_list)
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
    search the player by "ind" and send the "player pos" in the list players_t0
    resend the position in the data list
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


def test_search_2(T0_s, value=10):
    # search the value into list of list
    nb_value = 0
    for row in range(len(T0_s)):
        if T0_s[row][3].count(value) == 1:
            nb_value += 1
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
    #list_combinaison = []
    list_combinaison2 = []
    list_classement = []
    list_temp4b = []
    
    #print(player_lists2)
    
    #recuperation generique de la liste des indices joueurs
    for i in range(len(player_lists)):
        list_temp.append(player_lists[i][col])
    
    #creation des combinaisons mathematiquement possible avec les indices
    list_temp2 = list(combinations(list_temp, 2))
    #creation des couples indices formatée sur 2 catacteres
    list_temp3 = ["".join(item) for item in list_temp2]

    #tri des couples deja joués dans un tour precedent et ajout a une liste de recensement
    for j in range(len(list_temp3)): 
        if test_couple_ind_all(list_tmp_tournament, list_temp3[j]) is False:
            couple_list_temp2.append(list_temp3[j])
    # creation des combinaisons sur un tour ou round complet
    list_combinaison = list(combinations(couple_list_temp2, int(len(player_lists2)/2)))
    # start_time = time.time()
    # nettoyage des doublons pour avoir 1 seul joueur / tour
    for item in range(len(list_combinaison)):
        var_temp401 = ""

        list_temp4 = list_combinaison[item]

        for item2 in list_temp4:
            var_temp401 = var_temp401 + item2
        list_temp6 = set(var_temp401)

        if len(var_temp401) == len(list_temp6):
            list_combinaison2.append(list_combinaison[item])
        
    print("il y a", len(list_combinaison2), "possibilités")
        # list_temp6 = set(list_temp401)
        # list_temp4b = [.split(item) for item in list_combinaison]
    
        # end_time = time.time()
        # print("la fonction a pris : ", (end_time - star_time), "s")
    
    list_combinaison_charg = []
    for i in range(len(list_combinaison2)):
        point_echiquier_total = 0
        liste_advers = list(list_combinaison2[i])
        for j in liste_advers:
            
            player1 = j[0]
            player2 = j[1]
            # formule de calcul  on associe le point de chaque joueur + son rang divisé par mille
            for players in range(len(player_lists2)):
                if player1 == player_lists2[players][3]:
                    point_player1 = player_lists2[players][4] + (int(player_lists2[players][2])/10000)
                
                if player2 == player_lists2[players][3]:
                    point_player2 = player_lists2[players][4] + (int(player_lists2[players][2])/10000)
            
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
            # print("ok")
            return True
    except ValueError:
        # print("le couple", couple_player, "n'a pas joué ensemble")     
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

def init_match_db(nb_chess, my_match, id_tournament=2):
    # initialisation of the matrice of match an round
    match_tmnt_manager = Manager(DATAPATH, DB_MATCH_TMNT)
    # match_tmnt_manager.truncate()
    for match in range(nb_chess*nb_chess):
        data = [match, "", id_tournament,"", "", "", "","","","","","",""]
        match_tmnt_manager.data_match_tmnt_insert_by_objet(my_match)
        match_tmnt_manager.id_readjust()

def deroulement(players_t0, T_round, list_ind_tournament, nb_chess, round, T0_s):
    """

    """
    nb_free = 1
    nb_free_2 = 1
    while nb_free > 0:

        if not T0_s:
            print_row_tab_round(round, T_round)
        else:
            print_row_tab_round_2(round, T0_s)

        T0_results, player_indice, pt_gain, player_indice2 = results_T0(T_round, round)
        T0_s = convert_T0_2_T0_s(T0_results, T0_s, players_t0, round)
        
        list_ind_tournament = add_couplelist(list_ind_tournament, player_indice, player_indice2)
        players_t0 = score_up(players_t0, player_indice, player_indice2, pt_gain)
        player_update_to_db(players_t0)
        # ================================
        data_round = match_tmnt_database_list(T0_results, players_t0, round, nb_match=4,  play1_result="", play2_result="", st_date="", end_date="")

        match_tmnt_manager = Manager(DATAPATH, DB_MATCH_TMNT)
        data_round_s = match_tmnt_manager.match_db_serialising(data_round)
        for row in range(len(data_round_s)):
            m_query = Query()
            #print(data_round_s[row]['id'])
            match_exist = match_tmnt_manager.search_to_tinydb_by_id(data_round_s[row]['id'])
            match_tmnt_manager.match_updating_2(data_round_s[row]['id'],data_round_s[row])
            """if match_exist == 1 :
                match_tmnt_manager.update(data_round_s[row]), m_query.id == data_round_s[row][element]
            else:
                match_tmnt_manager.insert(data_round_s[row])"""
        
        # ==================================================

        nb_free = test_search(T0_results)  # trying to find "10", is the flag to chess party is not
        # nb_free_2 = test_search_2(T0_results)  # trying to find "10", is the flag to chess party is not
    print("fin de la partie Round " + str(round+1))
    # print(players_t0)
    """for i in range(len(players_t0)):
        print(players_t0[i])
    """

    return T0_results, list_ind_tournament


def show_about():
    # about_window = tkinter.Toplevel(app)
    about_window = tkinter.Toplevel()
    about_window.title("A propos")
    lb = tkinter.Label(about_window, text="\n écrit et conçu par: \n TGIONA pour OpenclassRooms prj4! \n Tous droits reservés 2021.")
    lb.pack()


def graphic_mode():
    maintk()


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
    set_global_var()
    #menu_base()
    # player_t0_bis = []
    # players_t0 = players_list_old()
    # player_t0_bis = players_list()
    players_t0 = players_list()
    
    players_t0 = tri_players(players_t0)
    list_ind = []
    list_ind_tournament = []
    players_t0 = assign_id_tnmt(players_t0)
    players_t0, list_ind = assign_id(players_t0)

    #  window_menu()
    # list_ind__tournament = permutation_cpl(list_ind)
    # print(list_ind__tournament)
    # test_couple_ind(list_ind_tournament, 'A','Z')
    # print(players_t0)

    print_row_tab_player(players_t0)
    
    nb_chess = int((len(players_t0))*0.5)   # ex d
    T0 = []
    T0_s = []  # matrice of match , it will remplace T0
    T1 = []
    match_data = {'id': 1, 'id_turn': 1, 'id_tournament': 1,
                  'name': "", 'player1_id': 1, "player2_id": 2}
    """,
                  "player1_ind": "", "player2_ind": "",
                  "player1_result": 0, "player2_result": 0,
                  "start_date": "", "end_date": "", 'time_control': "Coups rapide"}"""

    my_match = models.Match(**match_data)

    test_saisie = input("un tournoi est en cours , continuer ? (Oui= O, Non=N)")
    test_saisie = test_saisie.upper()
    if test_saisie == "O":
        
        my_match.id_tournament = query_id_open_state_tnmt()
        print('ok')
    else: 
        init_match_db(nb_chess, my_match)
        
        print( "test")

    if ((len(players_t0)) % 2) == 0:        # test si nb_chess est paire via le modulo == 0

        for round in range(nb_chess):
            print("Creation des parties Round " + str(round+1))
            if round == 0:
                # matchs creation in a round
                T0, T0_s = couple_list_T0(players_t0)

                # print_row_tab_round(round, T0)
                # print_row_tab_round_2(round, T0_s)
                # T0_results, player_indice, pt_gain, player_indice2 = results_T0(T0, nb_chess)
                T0_results, list_ind_tournament = deroulement(players_t0, T0, list_ind_tournament, nb_chess, round, T0_s)
                print_row_tab_player(players_t0)
            else:
                if len(T1) > (len(players_t0)/2*4):

                    T1, list_ind_tournament = round_tournament(players_t0, list_ind_tournament, T1, round)
                    T0_s = convert_T0_2_T0_s(T1, T0_s, players_t0, round)
                    player_update_to_db(players_t0)
                    """T1_temp = T1[:]
                    del T1_temp[0:17]
                    # print(T1_temp, "test") """
                    print_row_tab_player(players_t0)

                else:
                    T1, list_ind_tournament = round_tournament(players_t0, list_ind_tournament, T0_results, round)
                    T0_s = convert_T0_2_T0_s(T1, T0_s, players_t0, round)
                    player_update_to_db(players_t0)
                deroulement(players_t0, T1, list_ind_tournament, nb_chess, round, T0_s)
                print_row_tab_player(players_t0)

            #  tour0 =  1 quand tous les resultats sont saisi dans le T0_results
            # tour0 = 0

    else:
        exit


if __name__ == '__main__':
    # menu_base()
    main()
