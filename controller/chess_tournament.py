from itertools import combinations, permutations
from operator import itemgetter
from datetime import date
import sys
from os.path import dirname, join, abspath
import model
from model import models
from model.manager_txt import Manager
from view import rapport
from view.view_chess_tk import maintk
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
# from root_folder import file_name
sys.path.append('..model')
sys.path.append('..view')

global DATAPATH
global DB_PLAYERS
global DB_PLAYER_TNMT
global DB_TOURNAMENTS
global DB_MATCH_TMNT
global DB_TURN_TMNT
global DB_temp
DATAPATH = './data_players2.json'
DB_PLAYERS = 'players_list'
DB_PLAYER_TNMT = 'players_tournament'
DB_TOURNAMENTS = 'tournaments'
DB_MATCH_TMNT = 'match'
DB_TURN_TMNT = 'turn'
DB_TEMP = 'temp'


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
    """registering a player in a db"""
    player_manager = Manager(DATAPATH, DB_PLAYERS)
    player_manager.data_insert(data)
    player_manager.id_readjust()


def modify_player(id, new_rank):
    """to modify the rank of the player"""

    try:
        player_manager = Manager(DATAPATH, DB_PLAYERS)
        player_data = player_manager.search_to_tinydb_by_id(id)

        my_player = models.Player(**player_data[0])
        print("Le nouveau classement sera :", new_rank)
        my_player.rank = new_rank
        player_manager.update_player_rank(my_player)

    except ValueError:
        print("Le joueur n'existe pas !")


def game_loader():

    """ load temporary data of the game"""
    game_manager = Manager(DATAPATH, DB_TEMP)
    temp_game_data = game_manager.load_game_temp()
    temp_data = []
    a = 0
    for key in temp_game_data:
        temp_data.append(temp_game_data[key])
        a += 1
    return temp_data


def game_init():
    """initialisation of temp data
    # replace all by a zero"""
    game_manager = Manager(DATAPATH, DB_TEMP)
    game_manager.init_game_temp()


def game_update(data):
    """save game_temp data in the db to restore later"""
    game_manager = Manager(DATAPATH, DB_TEMP)
    game_manager.updgrade_game_temp(data)


def serialised_game(data):
    """formating the liste  to dict , neccessary to send in json"""
    data_s = {}
    for a in range(len(data)):
        key = str(a)
        value = data[a]
        data_s[key] = value
    return data_s


def match_tmnt_database_list(t_round, players_t0, round, nb_match=4,
                             play1_result="", play2_result="", st_date="", end_date=""):

    data_round_list = []
    data_round = []

    nb_round = int(len(players_t0)/2)  # total number of round and is number of chess per round
    leng_by_rd = nb_match * nb_round

    a = 0
    match = 0

    start_round = len(t_round) - leng_by_rd
    for a in range(start_round, len(t_round), nb_match):

        if t_round[a+3] != 10:
            data_round_list.append(0)
            for item in range(13):
                data_round.append("")
            data_round[0] = 1 + int(a/nb_match)
            data_round[1] = round
            data_round[2] = players_t0[search_player_by_indice(players_t0, t_round[a+1])][6]              # id_tnmt
            data_round[3] = t_round[a]                                                                     # name
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


def list_indice_constructor(T_round):
    """generate à list indice with"""
    my_couple_list = []
    for a in range(0, len(T_round), 4):
        if T_round[a+3] != 10:
            my_couple_list.append(T_round[a+2] + T_round[a+1])
            my_couple_list.append(T_round[a+1] + T_round[a+2])
    return my_couple_list


def score_constructor(T_round, players_T0):
    """upgrade the score , using the list T_round
     compare ind of player with indice in the the result
     when it mach with player 1 , i t search in player list and upgrade the right score"""
    for a in range(0, len(T_round), 4):
        player1 = T_round[a+1]
        player2 = T_round[a+2]
        sc_play2 = 0
        sc_play1 = 0

        if T_round[a+3] != 10:
            if T_round[a+3] == T_round[a+1]:
                # (' score   joueur 1')
                sc_play1 = 1

            elif T_round[a+3] == T_round[a+2]:
                # (' score  joueur 2')
                sc_play2 = 1

            else:
                # ('match nul, 0.5 pour chacun')
                sc_play1 = 0.5
                sc_play2 = 0.5

            if sc_play1 > 0.5:
                players_T0[search_player_by_indice(players_T0, player1)][4] += 1
            if sc_play2 > 0.5:
                players_T0[search_player_by_indice(players_T0, player2)][4] += 1
            if sc_play1 == 0.5:
                players_T0[search_player_by_indice(players_T0, player2)][4] = players_T0[search_player_by_indice(
                                                                                         players_T0, player2)][4] + 0.5
                players_T0[search_player_by_indice(players_T0, player1)][4] = players_T0[search_player_by_indice(
                                                                                         players_T0, player1)][4] + 0.5
    return players_T0


def query_id_open_state_tnmt():
    """query id tnmt with statut open
    return the id number of active tnmt"""

    tnmt_manager = Manager(DATAPATH, DB_TOURNAMENTS)
    query_tmnt = tnmt_manager.search_to_tiny_is_open()
    if len(query_tmnt) != 0:
        id_tmnt = query_tmnt[0]["id"]
        return id_tmnt
    id_tmnt = (-1)
    return id_tmnt


def assign_id_tnmt(players_t0):
    # assign id tnmt with state open to player list
    id_tmnt = query_id_open_state_tnmt()
    if id_tmnt != (-1):
        for row in range(len(players_t0)):
            players_t0[row][6] = id_tmnt
    else:
        print("Il n'y a pas de tournoi en cours, ")
        print("il faut declarer un nouveau tournoi")
        exit

    return(players_t0)


def player_inscription(data):
    """writing the list of player for the game
     send to players_t0  the player ready for the tournament"""

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


def player_unscription(id):
    """delete a player on the list of tournament"""
    player_tmnt_manager = Manager(DATAPATH, DB_PLAYER_TNMT)

    player_tmnt_manager.del_by_id(id)


def players_database_list(db='dbplayers', sort=""):
    """ catch list player in a db , and sorted by
    alphabetical name , rank or by chronology"""
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

        return players_all_db


def sorting_player_list(data_list, sort):
    """sorting list of list  by alphabetical or rank number"""
    if sort == "alpha":
        players_alpha_sorted = sorted(data_list, key=itemgetter(1, 5))
        return players_alpha_sorted
    else:
        # rank  sorted
        players_rank_sorted = sorted(data_list, key=itemgetter(5, 0), reverse=True)
        return players_rank_sorted


def player_tmnt_constructor_list(id_tmnt):
    """creat a list of player with a extraction from db_match
    return a list of list [lastname, firstname, birth, gender,rank, score]"""

    player_match_manager = Manager(DATAPATH, DB_MATCH_TMNT)
    data_match = player_match_manager.match_querying_by_id2(2, "id_turn", id_tmnt)
    player_list_ind = []
    m_player_data = []
    for n in range(len(data_match)):
        m_player = data_match[n]['player1_id']
        player_list_ind.append(m_player)
        m_player = data_match[n]['player2_id']
        player_list_ind.append(m_player)
    player_list_ind = [i for i in set(player_list_ind)]
    print(player_list_ind)
    player_manager = Manager(DATAPATH, DB_PLAYERS)
    dataprint_player = []
    for ind in range(len(player_list_ind)):
        data = player_manager.search_to_tinydb_by_id(player_list_ind[ind])
        m_player_data.append(data[0])

        my_player_base = models.Player_Chess(m_player_data[ind])
        dataprint_player.append([my_player_base.id,
                                my_player_base.lastname,
                                my_player_base.firstname,
                                my_player_base.birthdate,
                                my_player_base.gender,
                                int(my_player_base.rank),
                                my_player_base.score])
    return dataprint_player


def player_of_tmnt_to_report(id_tmnt, sort):
    """formated data to report info to print on screen"""
    data_list = player_tmnt_constructor_list(id_tmnt)
    return sorting_player_list(data_list, sort)


def tmnt_database_list():
    """creation of data list from db"""
    tmnt_manager = Manager(DATAPATH, DB_TOURNAMENTS)
    tmnt_all_db = []
    tmnt_all_db = tmnt_manager.tmnt_all_datadb_serialized()
    return tmnt_all_db


def turn_creation_db_old(my_turn_obj, round):
    """creation turn of the initialisation of the db"""

    db_turn = Manager(DATAPATH, DB_TURN_TMNT)
    for nb in range(1, round + 1, 1):
        db_turn.data_turn_init_insert_by_object(my_turn_obj)
        val = my_turn_obj.id
        my_turn_obj.id = val + 1


def turn_creation_db_init(id_tnmt, round):
    """creation turn of the initialisation of the db"""
    turn_data = {"id": 1, "id_tournament": id_tnmt, "number": 1, "start_date": date.today(), "end_date": date.today()}
    my_turn_obj = models.Turn(turn_data)
    db_turn = Manager(DATAPATH, DB_TURN_TMNT)
    for nb in range(1, round + 1, 1):
        db_turn.data_turn_init_insert_by_object(my_turn_obj)
        val = my_turn_obj.id
        my_turn_obj.id = val + 1
        my_turn_obj.number = val + 1


def turn_creation_db(id_tnmt, round):
    """creation turn of the initialisation of the db"""
    turn_data = {"id": round, "id_tournament": id_tnmt, "number": round,
                 "start_date": date.today(), "end_date": date.today()}
    my_turn_obj = models.Turn(turn_data)
    db_turn = Manager(DATAPATH, DB_TURN_TMNT)
    db_turn.data_turn_init_insert_by_object(my_turn_obj)
    return my_turn_obj


def turn_object_database_(id, id_tnmt):
    """send a turn object found in the db by id & id_tmnt"""
    turn_manager = Manager(DATAPATH, DB_TURN_TMNT)
    turn_all_db = []
    turn_all_db = turn_manager.turn_data_serialized_by_id(id, id_tnmt)
    return turn_all_db


def turn_upgrade_date_internal(turn_object, date='start'):
    """date upgrade  to tiny db"""
    turn_manager = Manager(DATAPATH, DB_TURN_TMNT)
    # data = turn_manager.search_to_tinydb_by_id_2(turn_object.id, turn_object.id_tournament)
    turn_manager.turn_upgrade_date(turn_object, date='start')
    # print("test")


def del_turn(id, id_tournament):
    """delete a selected occurs of"""
    db_turn = Manager(DATAPATH, DB_TURN_TMNT)

    data_doc_id = db_turn.search_by_doc_id(id, id_tournament)

    db_turn.del_by_doc_id(data_doc_id)


def del_all_turn_id(id_tournament, DATAPATH, DB):
    """delete all ref by_doc_id of a tnmt when it is restarted
    compatible all_section"""
    db_manager = Manager(DATAPATH, DB)
    nb_counted = db_manager.count_doc(id_tournament)
    for n in range(1, nb_counted+1):
        data_doc_id = db_manager.search_by_doc_id_2(id_tournament)
        db_manager.del_by_doc_id(data_doc_id)


def tmnt_match_database_serialising(data):
    """send info to the database"""
    tmnt_match_manager = Manager(DATAPATH, DB_MATCH_TMNT)
    tmnt_match_manager.match_db_serialising(data)


def update_math_db(T0_s, players_t0):
    """update the match base"""
    print("test match_update")


def tmnt_match_database_to_matchmaking():
    """send info to the database"""
    tmnt_match_manager = Manager(DATAPATH, DB_MATCH_TMNT)
    tmnt_match_manager.match_db_unserialising()


def match_report_with_name(id_value=23, id_name='id'):
    """mastering data for displaying information with the name of player"""

    match_with_name = []
    match_with_name_list = []
    match_tmnt_manager = Manager(DATAPATH, DB_MATCH_TMNT)
    m_data = match_tmnt_manager.match_querying_by_id(id_value, id_name)
    for play in range(len(m_data)):
        if len(m_data[play]) > 3:
            my_match = model.models.Match(**m_data[play])
            player_manager = Manager(DATAPATH, DB_PLAYERS)
            my_player_data1 = player_manager.search_to_tinydb_by_id(my_match.player1_id)
            my_player_data2 = player_manager.search_to_tinydb_by_id(my_match.player2_id)
            my_player1 = model.models.Player(**my_player_data1[0])
            my_player2 = model.models.Player(**my_player_data2[0])

            match_with_name = match_tmnt_manager.match_object_db_unserialising(my_match)

            match_with_name[0][4] = my_player1.lastname + " " + my_player1.firstname
            match_with_name[0][5] = my_player2.lastname + " " + my_player2.firstname
            match_with_name_list.append(*match_with_name)

    return match_with_name_list


def round_report_by_id(id_value=23, id_name='id_tournament'):
    """mastering data for displaying round information"""

    turn_list = []
    turn_tmnt_manager = Manager(DATAPATH, DB_TURN_TMNT)
    m_data = turn_tmnt_manager.match_querying_by_id(id_value, id_name)
    for play in range(len(m_data)):
        my_turn = models.Turn(m_data[play])
        turn_name2 = my_turn.serialized()

        turn_list.append(turn_name2)

    return turn_list


def players_list():
    """catch the player document in db to list for match making"""
    player_manager_tmnt = Manager(DATAPATH, DB_PLAYER_TNMT)
    players_t0_tmnt = []

    players_t0_tmnt = player_manager_tmnt.player_serialized()

    return players_t0_tmnt


def player_update_to_db(players_T0):
    """ update the score to the db with manager"""

    player_tmnt_manager = Manager(DATAPATH, DB_PLAYER_TNMT)

    for row in range(len(players_T0)):

        player_tmnt_manager.update_player_tmnt(players_T0[row])


def tournament_register(data):
    """to create the database with data from view"""
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
        players_list[i][column] = chr(ord(d) + i)
        list_ind.append(chr(ord(d) + i))
        # affichage debug
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

    return round_0_list, tab_round_all_match


def convert_T0_2_T0_s(T0, T0_s, players_t0, round):
    # convert T0 (linear list) to  list of list with more information
    a = len(T0)
    tab_round_all_match = []

    round_0_listb = []

    for i in range(0, a, 4):

        if (i % 4 == 0):
            # 1 match of T0 is writed with 4 elements
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

    if (a % 2 == 0):
        T1.append("E" + str(int(a/4+1)))
        T1.append(player1)
        T1.append(player2)
        T1.append(10)

    else:
        print("erreur sur la liste Tournoi secondaire")
    return T1


def results_T0(T0, round=0, nb_chess=4):
    """
    recupere la saisie du  resultat  du gagnant
    jusqu'a ce que tous les gagnants soient saisi
    """
    # print("Tour 0 : Donner le nom du joueur gagnant")

    player_exist = False

    while player_exist is False:
        ind_player_1 = (input("Tour " + str(round) + " : Donner l'indice alphabétique du joueur gagnant : ")).upper()
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
                    gain = 1

                elif b == "N":
                    gain = 0.5

                else:
                    b = "G"
                    gain = 1

            player_exist, pos_result, ind_player_2 = search_player(T0, ind_player_1, round, nb_chess)
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
    player_exist = False

    while player_exist is False:
        ind_player_1 = (input("Tour " + str(round+1) + " : Donner l'indice alphabétique du joueur gagnant : ")).upper()
        player_exist = search_player(T0, ind_player_1, round)

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


def search_player(player_list, player, round=0, nb_chess=5):
    """
    cherche le joueur  dans la liste

    """
    try:

        actual_round = int(len(player_list)/(nb_chess*4))

        if round > 0:

            start_search = (actual_round - 1) * 4 * (nb_chess)
        else:
            start_search = 0

        end_list = len(player_list)-1

        a = player_list.index(player, start_search, end_list)  # position juste apres e+1

        p_exist = True
        ind_player2 = None
        if player_list[(a-1)][0] == "E" and len(player_list[(a-1)]) >= 2:
            "test"

            b = (a-1)+3
            nom_echiq = player_list[(a-1)]

            ind_player2 = player_list[(a+1)]
            print("Le joueur", ind_player2, "est trouvé dans l'échiquier", nom_echiq)

        elif player_list[(a-2)][0] == "E" and len(player_list[(a-2)]) >= 2:          # position 2 dans la liste
            "test"
            b = (a-2)+3
            nom_echiq = player_list[(a-2)]
            ind_player2 = player_list[(a-1)]
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


def round_tournament(player_lists, list_tmp_tournament, T0_results, round=0, col=3):
    """
    algo deroulement du tournoi sur la base des points accumulés au fur a mesure des parties

    """
    T1 = []  # liste des parties apres le 1er tour avec appariement par  piorité resultats
    T1.extend(T0_results)
    player_lists2 = tri_players_T1(player_lists)
    couple_list_temp2 = []
    list_temp = []
    list_temp3 = []
    list_combinaison2 = []
    # recuperation generique de la liste des indices joueurs
    for i in range(len(player_lists)):
        list_temp.append(player_lists[i][col])

    # creation des combinaisons mathematiquement possible avec les indices
    list_temp2 = list(combinations(list_temp, 2))

    # creation des couples indices formatée sur 2 catacteres
    list_temp3 = ["".join(item) for item in list_temp2]

    # tri des couples deja joués dans un tour precedent et ajout a une liste de recensement
    for j in range(len(list_temp3)):
        if test_couple_ind_all(list_tmp_tournament, list_temp3[j]) is False:
            couple_list_temp2.append(list_temp3[j])

    # creation des combinaisons sur un tour ou round complet
    list_combinaison = list(combinations(couple_list_temp2, int(len(player_lists2)/2)))

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

    list_combinaison_charg = tri_players_T1(list_combinaison2, 3)
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
    my_list = []

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
        if my_list.index(couple_player) >= 0:
            print("ok")
            return True
    except ValueError:
        print("le couple", couple_player, "n'a pas joué ensemble")
        return False


def test_couple_ind_all(my_list, couple_player):
    """
    this section is checking if the couple exists in the meeting_list
    if yes it returns true
    if not   error retuned  so the association has the agrement
    """
    try:
        if my_list.index(couple_player) >= 0:
            return True
    except ValueError:
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

    for match in range(nb_chess*nb_chess):

        match_tmnt_manager.data_match_tmnt_insert_by_objet(my_match)
        match_tmnt_manager.id_readjust()


def deroulement(players_t0, T_round, list_ind_tournament, nb_chess, round, T0_s):
    """

    """
    nb_free = 1

    while nb_free > 0:

        nb_free = test_search(T_round)
        if nb_free == 0:
            return T_round, list_ind_tournament

        if not T0_s:
            rapport.print_row_tab_round(round, T_round)

        else:
            rapport.print_row_tab_round_2(round, T0_s)

        T0_results, player_indice, pt_gain, player_indice2 = results_T0(T_round, round, nb_chess)
        T0_s = convert_T0_2_T0_s(T0_results, T0_s, players_t0, round)

        my_game_temp = model.models.GameTemp(serialised_game(T0_results))
        game_update(my_game_temp.game)

        list_ind_tournament = add_couplelist(list_ind_tournament, player_indice, player_indice2)
        players_t0 = score_up(players_t0, player_indice, player_indice2, pt_gain)
        player_update_to_db(players_t0)
        # ================================

        data_round = match_tmnt_database_list(T0_results, players_t0, round, nb_match=4,
                                              play1_result="", play2_result="", st_date="", end_date="")
        match_tmnt_manager = Manager(DATAPATH, DB_MATCH_TMNT)
        data_round_s = match_tmnt_manager.match_db_serialising(data_round)

        for row in range(len(data_round_s)):
            match_tmnt_manager.match_updating_2(data_round_s[row]['id'],
                                                data_round_s[row], data_round_s[row]['id_tournament'])

        # ==================================================

        nb_free = test_search(T0_results)  # trying to find "10", is the flag to chess party is not

    print("fin de la partie Round " + str(round+1))

    return T0_results, list_ind_tournament


def graphic_mode():
    maintk()


def close_active_tournament():
    # change the attribute of status of active tournament
    # it becomes to be closed
    tmnt_manager = Manager(DATAPATH, DB_TOURNAMENTS)
    result = tmnt_manager.search_to_tiny_is_open()
    if len(result) > 0:
        result[0]["state"] = "closed"
        result[0]["end_date"] = str(date.today())
        tmnt_manager.change_state_tmnt(result[0]["id"], result[0]["end_date"])


def main():
    """
    """
    set_global_var()

    players_t0 = players_list()

    players_t0 = tri_players(players_t0)
    list_ind = []
    list_ind_tournament = []
    players_t0 = assign_id_tnmt(players_t0)
    players_t0, list_ind = assign_id(players_t0)

    rapport.print_row_tab_player(players_t0)

    nb_chess = int((len(players_t0))*0.5)   # ex d
    T0 = []
    T0_s = []  # matrice of match , it will remplace T0
    T1 = []
    match_data = {'id': 1, 'id_turn': 1, 'id_tournament': 1,
                  'name': "", 'player1_id': 1, "player2_id": 2}

    my_match = models.Match(**match_data)
    my_match.id_tournament = query_id_open_state_tnmt()
    test_saisi = input("un tournoi est en cours , voulez vous le charger ? (Oui= O, Non=N)")
    test_saisi = test_saisi.upper()

    if test_saisi == "O":

        print('la partie sauvegardée est chargée en mémoire')
        # here is the emplacement to initiate the game information

        T0_temp = game_loader()
        if len(T0_temp) > (nb_chess * 4):
            T0 = T0_temp.copy()
            T0_results = T0
            list_ind_tournament = list_indice_constructor(T0_results)

        else:
            T0 = T0_temp.copy()

        players_t0 = score_constructor(T0, players_t0)
        active_round = int(len(T0)/(4*nb_chess))  # is divided by 4 because a party is writed  by 4 caracters
        T0_s = convert_T0_2_T0_s(T0, T0_s, players_t0, active_round)
        list_ind_tournament = list_indice_constructor(T0)

    else:
        print('la partie sauvegardée sera perdue...')
        game_init()

        print("système réinitialisé !")
        active_round = 1
    round = active_round

    if ((len(players_t0)) % 2) == 0:        # test si nb_chess est paire via le modulo == 0
        if active_round:
            round = active_round
        else:
            active_round = 1
            round = active_round

        while round < (nb_chess + 1):

            print("Creation des parties Round " + str(round))
            my_turn = turn_creation_db(my_match.id_tournament, round)
            turn_upgrade_date_internal(my_turn, date="start")
            if round == 1:
                # matchs creation in a round
                if len(T0) < 1:
                    T0, T0_s = couple_list_T0(players_t0)
                else:
                    print(" ca passe")

                T0_results, list_ind_tournament = deroulement(players_t0, T0, list_ind_tournament,
                                                              nb_chess, round, T0_s)

                rapport.print_row_tab_player(players_t0)
                turn_upgrade_date_internal(my_turn, date="end")
            else:
                nb_free = test_search(T0_results)
                if nb_free > 0:
                    T0_results, list_ind_tournament = deroulement(players_t0, T0,
                                                                  list_ind_tournament, nb_chess, round, T0_s)

                if len(T1) > (len(players_t0)/2*4):

                    T1, list_ind_tournament = round_tournament(players_t0, list_ind_tournament, T1, round)
                    T0_s = convert_T0_2_T0_s(T1, T0_s, players_t0, round)

                    my_game_temp = models.GameTemp(serialised_game(T1))
                    game_update(my_game_temp.game)

                    list_ind_tournament = list_indice_constructor(T1)

                    player_update_to_db(players_t0)

                    rapport.print_row_tab_player(players_t0)

                else:

                    T1, list_ind_tournament = round_tournament(players_t0, list_ind_tournament, T0_results, round)

                    my_game_temp = models.GameTemp(serialised_game(T1))
                    game_update(my_game_temp.game)
                    list_ind_tournament = list_indice_constructor(T1)

                    T0_s = convert_T0_2_T0_s(T1, T0_s, players_t0, round)
                    player_update_to_db(players_t0)
                deroulement(players_t0, T1, list_ind_tournament, nb_chess, round, T0_s)
                rapport.print_row_tab_player(players_t0)

            round += 1

        close_active_tournament()
    else:
        exit


if __name__ == '__main__':
    # menu_base()
    main()
