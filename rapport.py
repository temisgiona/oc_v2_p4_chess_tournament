
def print_row_tab_player(player_serialized):
    #print the information of player a the end of round
    tab = "    "
    print("")
    print("Nom", tab, "Prenom", tab, "rang", tab, "Ind", tab, "Score", tab, "ID")
    print("")
    for row in range(len(player_serialized)):
        # for column in range (6):
        print('%-8s' % player_serialized[row][0],
              '%-12s' % player_serialized[row][1],
              '%-8s' % player_serialized[row][2],
              '%-10s' % player_serialized[row][3],
              '%-8s' % player_serialized[row][4],
              '%-8s' % player_serialized[row][5])
    print("")


def print_row_tab_round(round, match):
    # print the result of a round  match/match 
    match_view = match.copy()
    tab = "    "
    print("")
    print("Nom Echiquier", tab, "indice joueur 1", tab, "indice Joueur2", tab, "Resultat")
    print("")
    for row in range(0, len(match), 4):
        m_row = row + 3
        # print (match[m_row])
        if match[m_row] == 10:
            match_view[m_row] = 'Non joué'
    # for column in range (6):
            print('%-20s' % match[row],
                  '%-20s' % match[row + 1],
                  '%-18s' % match[row + 2],
                  '%-10s' % match_view[m_row])
    print("")


def print_players_database(player_serialized, title2='rank', title="Liste des joueurs du club"):
    # print all data of the player database

    tab = "    "
    #method of sorting 
    if title2 == 'rank':
        title2b = "rangé par classement"
    elif title2 == 'alpha':
        title2b = "rangé par ordre alphabetique"
    else:
        title2b = ""

    print("")
    print('%-25s' % tab, title)
    if not title2 == "":
        print('%-25s' % tab, title2b)

    print("ID", tab, "Nom", tab, tab, "Prenom", tab, "date de naissance", tab, "Genre", tab, "Rang", tab, "Score")
    print("")

    for row in range(len(player_serialized)):
        # for column in range (6):
        print('%-5s' % player_serialized[row][0],
              '%-15s' % player_serialized[row][1],
              '%-12s' % player_serialized[row][2],
              '%-22s' % player_serialized[row][3],
              '%-10s' % player_serialized[row][4],
              '%-10s' % player_serialized[row][5],
              '%-5s' % player_serialized[row][6])
    print("")


def print_tournament_database(tmnt_serialized, title2='open', title="Liste des tournois"):
    # print all data of the tournament database

    tab = "    "
    #method of sorting 
    if title2 == 'open':
        title2b = "en cours"
    elif title2 == 'finished':
        title2b = "terminés"
    else:
        title2b = ""

    print("")
    print('%-25s' % tab, title)
    if not title2 == "":
        print('%-25s' % tab, title2b)

    print("ID", tab, "Nom", tab, tab, "Lieu", tab, "Date de début", tab, "Date de fin", tab,
          "Controle temps", tab, "Nbr Round", tab, "Statut")
    print("")
    if title2 == 'open':
        for row in range(len(tmnt_serialized)):
            # for column in range (6):
            if tmnt_serialized[row][7] == "open":
                print('%-7s' % tmnt_serialized[row][0],
                      '%-12s' % tmnt_serialized[row][1],
                      '%-12s' % tmnt_serialized[row][2],
                      '%-15s' % tmnt_serialized[row][3],
                      '%-25s' % tmnt_serialized[row][4],
                      '%-15s' % tmnt_serialized[row][5],
                      '%-10s' % tmnt_serialized[row][6],
                      '%-10s' % tmnt_serialized[row][7],
                      )

    elif title2 == 'finished':
        for row in range(len(tmnt_serialized)):
            if tmnt_serialized[row][7] == "closed":
                print('%-7s' % tmnt_serialized[row][0],
                      '%-12s' % tmnt_serialized[row][1],
                      '%-12s' % tmnt_serialized[row][2],
                      '%-15s' % tmnt_serialized[row][3],
                      '%-25s' % tmnt_serialized[row][4],
                      '%-15s' % tmnt_serialized[row][5],
                      '%-10s' % tmnt_serialized[row][6]
                      )
    else:
        for row in range(len(tmnt_serialized)):
            print('%-7s' % tmnt_serialized[row][0],
                  '%-12s' % tmnt_serialized[row][1],
                  '%-12s' % tmnt_serialized[row][2],
                  '%-15s' % tmnt_serialized[row][3],
                  '%-25s' % tmnt_serialized[row][4],
                  '%-15s' % tmnt_serialized[row][5],
                  '%-10s' % tmnt_serialized[row][6],
                  '%-10s' % tmnt_serialized[row][7],
                  )

    print("")

def print_match_tmnt_datase(data_serialized, title2='open', title="Liste des match" ):
    print ('test beta')
    tab = "    "
    #method of sorting 
    if title2 == 'open':
        title2b = "en cours"
    elif title2 == 'finished':
        title2b = "terminés"
    else:
        title2b = ""

    print("")
    print('%-25s' % tab, title)
    if not title2 == "":
        print('%-25s' % tab, title2b)

    print("ID", tab, "Nom", tab, tab, "Joueur 1", tab,"joueur 2" "Date de début", tab, "Date de fin", tab,
          "Controle temps", tab, "Nbr Round", tab, "r")
    print("")
    if title2 == 'open':
        for row in range(len(data_serialized)):
            # for column in range (6):
            #if data_serialized[row][13] == "open":
            print('%-7s' % data_serialized[row][0],
                    '%-12s' % data_serialized[row][3],
                    '%-12s' % data_serialized[row][2],
                    '%-15s' % data_serialized[row][3],
                    '%-25s' % data_serialized[row][4],
                    '%-15s' % data_serialized[row][5],
                    '%-10s' % data_serialized[row][6],
                    '%-10s' % data_serialized[row][7],
                    )
    

player_t0 = [
        ['temis', 'giona', 4, 0, 0, 0],
        ['eric', 'fortunato', 8, 0, 0, 0],
        ['a', 'b', 3, 0, 0, 0],
        ['k', 'l', 15, 0, 0, 0],
        ['m', 'n', 1000, 0, 0, 0],
        ['o', 'r', 100, 0, 0, 0],
        ['q', 's', 16, 0, 0, 0],
        ['p', 't', 16, 0, 0, 0]
        ]
# print_row_tab_player(player_serialized)
