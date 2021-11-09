"crud db tiny"
# import json
from tinydb import TinyDB, Query, where
from typing import Any
import models
# from generic_models import Player


class Manager:
    # def __init__(self, path, table, collection_type: Any):
    def __init__(self, path, table):
        # self.collection = {}
        self.path = path
        self.table = table
        # self.collection_type = collection_type

    def db_initial(self):
        
        db = TinyDB(self.path).table(self.table)
        return db

    def load_all_from_tinydb(self):
        # load all elements of tiny database
        # return a list of dict with all elements key & values
        # return the count of elments for optimize the process
        db = TinyDB(self.path).table(self.table)
        serialized_data = {}
        count = 0
        for db_item in db:
            serialized_data[count] = db_item
            count += 1
        datall_2_lists = {}

        for item_id in range(len(serialized_data)):
            
            serial_single_data = serialized_data[item_id]
            data_list = serial_single_data.values()
            # data_list =serialized_data[item_id]
            data_list = list(data_list)
            datall_2_lists[item_id] = data_list
        return datall_2_lists, count

    def search_to_tinydb_by_id(self, key_value):

        # search on tiny db database
        # return a dict with all elements

        query = (TinyDB(self.path).table(self.table)).search(where('id') == key_value)
        return query

    def search_to_tinydb_by_player_name(self, key_value):

        # search on tiny db database
        # return a dict with all elements

        query = (TinyDB(self.path).table(self.table)).search(where('name') == key_value)
        return query


    def search_to_tiny_is_open(self):
        query = (TinyDB(self.path).table(self.table)).search(where('state') == 'open')
        return query

    def serialize_query(self, query):
        # return data serialized , doc --> dict  unable to easy transfert
        for item in range(len(query)):

            serialized_data = query[0]
            return serialized_data

    def player_serialized(self):
        # catch the data list from tiny and format the list for matching system

        db_manager = (TinyDB(self.path).table(self.table))
        match_object_list = []
        list_player_object = []
        for item in range(len(db_manager.all())):
            element_id = db_manager.all()[item]
            # print('element id ', element_id)
            # match_object_list.append(0].append(element_id["lastname"])
            for d in range(7):
                # creation of the entry of the objest to simplify the update
                match_object_list.append(0)
            match_object_list[0] = element_id["lastname"]
            match_object_list[1] = element_id["firstname"]
            match_object_list[2] = element_id["rank"]
            match_object_list[3] = 0
            match_object_list[4] = 0
            # match_object_list[5] = 0
            match_object_list[5] = element_id["id"]

            # match_object_list.append(element_id["id"])
           
            list_player_object.append(match_object_list)
            match_object_list = []
            # print(list_player_object)
        return list_player_object

    def players_all_data_serialized(self):
        # catch the data list from tiny and format the list for reporting system
        db_manager = (TinyDB(self.path).table(self.table))
        match_object_list = []
        list_player_object = []
        for item in range(len(db_manager.all())):
            element_id = db_manager.all()[item]
                        
            for d in range(7):
                match_object_list.append(0)
            match_object_list[0] = element_id["id"]    
            match_object_list[1] = element_id["lastname"]
            match_object_list[2] = element_id["firstname"]
            match_object_list[3] = element_id["birthdate"]
            match_object_list[4] = element_id["gender"]
            match_object_list[5] = element_id["rank"]
            match_object_list[6] = element_id["score"]
            
            list_player_object.append(match_object_list)
            match_object_list = []
            # print(list_player_object)
        return list_player_object

    def tmnt_all_datadb_serialized(self):
        # catch the TMNT data list from tiny and format the list for reporting system
        db_manager = (TinyDB(self.path).table(self.table))
        match_object_list = []
        list_tmnt_object = []
        for item in range(len(db_manager.all())):
            element_id = db_manager.all()[item]
                        
            for d in range(8):
                match_object_list.append(0)
            match_object_list[0] = element_id["id"]    
            match_object_list[1] = element_id["name"]
            match_object_list[2] = element_id["place"]
            match_object_list[3] = element_id["start_date"]
            match_object_list[4] = element_id["end_date"]
            match_object_list[5] = element_id["time_control"]
            match_object_list[6] = element_id["round_number"]
            match_object_list[7] = element_id["state"]

            list_tmnt_object.append(match_object_list)
            match_object_list = []
            # print(list_player_object)
        return list_tmnt_object

    def match_db_serialising(self, data):
        # catch information from match making db to database
        db_manager = (TinyDB(self.path).table(self.table))
        match_object_list = []
        list_match_object = []
        # for item in range(len(db_manager.all())):
        """for item in range(len(data)):
            # element_id = db_manager.all()[item]
            element_id = data[item]"""
            # db_manager.search_to_tinydb_by_id(element_id[0])
        for item in range(len(data)):
            if data[item] != 0:
                element_idb = db_manager.all()[item]
                element_id = data[item]
            #chercher la ligne correspondante                
                for d in range(13):
                    match_object_list.append(0)

                element_idb["id"] = element_id[0]
                element_idb["id_turn"] = element_id[1]
                element_idb["id_tournament"] = element_id[2]
                element_idb["name"] = element_id[3]
                element_idb["player1_id"] = element_id[4]
                element_idb["player2_id"] = element_id[5]
                element_idb["player1_ind"] = element_id[6]
                element_idb["player2_ind"] = element_id[7]
                element_idb["player1_result"] = element_id[8]
                element_idb["player2_result"] = element_id[9]
                element_idb["start_date"] = element_id[10]
                element_idb["end_date"] = element_id[11]
                element_idb["time_control"] = element_id[12]
                
                list_match_object.append(element_idb)
                element_idb = []
            # print(list_player_object)
        return list_match_object

    def match_object_db_serialising(self, datadb, match):
        # catch information from match making db to database 
        db_manager = (TinyDB(self.path).table(self.table))
        match_object_list = []
        list_match_object = []
        # for item in range(len(db_manager.all())):
        for item in range(len(datadb)):
            # element_id = db_manager.all()[item]
            element_id = datadb[item]            
            
            for item in range(len(db_manager.all())):
                element_idb = db_manager.all()[item]
                            
                """for d in range(13):
                    match_object_list.append(0)"""

                element_idb["id"] = match.id
                element_idb["id_turn"] = match.id_turn
                element_idb["id_tournament"] = match.id_tournament
                element_idb["name"] = match.name
                element_idb["player1_id"] = match.player1_id
                element_idb["player2_id"] = match.player2_id
                element_idb["player1_ind"] = match.player1_ind
                element_idb["player2_ind"] = match.player1_ind
                element_idb["player1_result"] = match.player1_result
                element_idb["player2_result"] = match.player2_result
                element_idb["start_date"] = match.start_date
                element_idb["end_date"] = match.end_date
                element_idb["time_control"] = match.timecontrol
                
                list_match_object.append(element_idb)
                element_idb = []
            # print(list_player_object)
        return list_match_object

    def match_db_unserialising(self, data):
        # catch information from data[] match making to database
        db_manager = (TinyDB(self.path).table(self.table))
        match_object_list = []
        list_match_object = []
        
        for item in range(len(db_manager.all())):
        # for item in range(len(db_manager.all())):
        
            # element_id = data[item]
            element_id = db_manager.all()[item]
                        
            for d in range(13):
                match_object_list.append(0)

            match_object_list[0] = element_id["id"] 
            match_object_list[1] = element_id["id_turn"]
            match_object_list[2] = element_id["id_tournament"]
            match_object_list[3] = element_id["name"]
            match_object_list[4] = element_id["player1_id"]
            match_object_list[5] = element_id["player2_id"]
            match_object_list[6] = element_id["player1_result"]
            match_object_list[7] = element_id["player2_result"]
            match_object_list[8] = element_id["start_date"]
            match_object_list[9] = element_id["end_date"]
            match_object_list[10] = element_id["time_control"]            
            list_match_object.append(match_object_list)
            match_object_list = []
            # print(list_player_object)
        
        return list_match_object

    def match_object_db_unserialising(self, data):
        # catch information from objet.data match making to database
        db_manager = (TinyDB(self.path).table(self.table))
        match_object_list = []
        list_match_object = []
        
                            
        for d in range(12):
            match_object_list.append(0)

        match_object_list[0] = data.id
        match_object_list[1] = data.id_turn
        match_object_list[2] = data.id_tournament
        match_object_list[3] = data.name
        match_object_list[4] = data.player1_id
        match_object_list[5] = data.player2_id
        match_object_list[6] = data.player1_result
        match_object_list[7] = data.player2_result
        match_object_list[8] = str(data.start_date)
        match_object_list[9] = str(data.end_date)
        match_object_list[10] = ""  # str(data.time_control)
        list_match_object.append(match_object_list)
        match_object_list = []
            # print(list_player_object)
        
        return list_match_object

    def match_db_unserialising2(self, data):
        # catch information from data[] match making to database
        db_manager = (TinyDB(self.path).table(self.table))
        match_object_list = []
        list_match_object = []
        
        #for item in range(len(db_manager.all())):
        for item in range(len(data)):
        
            # element_id = data[item]
            element_id = data[item]
                    
        for d in range(13):
            match_object_list.append(0)

        match_object_list[0] = element_id["id"] 
        match_object_list[1] = element_id["id_turn"]
        match_object_list[2] = element_id["id_tournament"]
        match_object_list[3] = element_id["name"]
        match_object_list[4] = element_id["player1_id"]
        match_object_list[5] = element_id["player2_id"]
        match_object_list[6] = element_id["player1_result"]
        match_object_list[7] = element_id["player2_result"]
        match_object_list[8] = element_id["start_date"]
        match_object_list[9] = element_id["end_date"]
        match_object_list[10] = element_id["time_control"]            
        list_match_object.append(match_object_list)
        match_object_list = []
            # print(list_player_object)
        
        return list_match_object

   

    def match_querying_by_id(self, id, key='id'):
        # query of for a match
        db_manager = (TinyDB(self.path).table(self.table))
        match_query = Query()
        if key == 'id':
            match = db_manager.search(match_query.id == id)
        elif key == 'id_tournament':
            match = self.search(match_query.id_tournament == id)
        elif key == 'id_turn':
            match = self.search(match_query.id_turn == id)
        elif key == 'name':
            match = self.search(match_query.name == id)
        # print(match)
        return match


    def match_updating(self, id, data):
        db_manager = (TinyDB(self.path).table(self.table))
        match_query = Query()
        match = db_manager.search(match_query.id == id)
        for item in (data):
            db_manager.update({data[item]}, match_query.id == id)
            print(item)
    
    def match_updating_2(self, id, data):
        # upsert the database by id
        db_manager = (TinyDB(self.path).table(self.table))
        match_query = Query()
        match = db_manager.search(match_query.id == id)
        db_manager.upsert(data, match_query.id == id)
        """for item in (data):
            db_manager.upsert({data[item]}, match_query.id == id)
            print(item)"""

    def update_player_tmnt(self, player_t0_u):
        # update player indice , and score 26/10/2021
        db_manager = (TinyDB(self.path).table(self.table))
        m_query = Query()
        db_manager.update({'score': player_t0_u[4]}, m_query.id == player_t0_u[5])
        # db_manager.update({'score': player_t0[3]}, m_query.type'id') == player_t0[5])
        # print(player_t0_u)

    def id_readjust(self):
        # copy the id allowed by tiny to assign a the document
        # catching de doc_id and if different assign the doc_id  to id if element
        db_manager = (TinyDB(self.path).table(self.table))
        for item in range(len(db_manager.all())):
            element_id = db_manager.all()[item]
            # on prend le doc id et on l'assigne id element
            # pour simp^lifier la requete
            if element_id.doc_id != element_id["id"]:
                db_manager.update({'id': element_id.doc_id}, doc_ids=[element_id.doc_id])

    def data_insert(self, data):
        # creation data player  to put in the tiny database
        if data['id'] == '':
            data['id'] = 1000

        (TinyDB(self.path).table(self.table)).insert({"id": data['id'], "lastname": data["lastname"],
                                                     "firstname": data["firstname"], "gender": data["gender"],
                                                      "birthdate": data["birthdate"], "rank": data["rank"],
                                                      "score": data["score"]})

    def data_match_tmnt_insert(self, data):
        # create the match data to put in the tiny database

        (TinyDB(self.path).table(self.table)).insert({"id": data['id'],
                                                      "id_turn": data['id_turn'],
                                                      "id_tournament": data["id_tournament"],
                                                      "name": data["name"],
                                                      "player1_id": data["player1_id"],
                                                      "player2_id": data["player2_id"],
                                                      "player1_ind": data["player1_ind"],
                                                      "player2_ind": data["player2_ind"],
                                                      "player1_result": data["player1_result"],
                                                      "player2_result": data["player2_result"],
                                                      "start_date": data["start_date"],
                                                      "end_date": data["end_date"],
                                                      "time_control": data["time_control"]})

    def data_match_tmnt_insert_by_objet(self, my_match):
        # create the match data to put in the tiny database

        (TinyDB(self.path).table(self.table)).insert({"id": my_match.id,
                                                      "id_turn": my_match.id_turn,
                                                      "id_tournament": my_match.id_tournament})
        """,
                                                      "name": data["name"],
                                                      "player1_id": data["player1_id"],
                                                      "player2_id": data["player2_id"],
                                                      "player1_ind": data["player1_ind"],
                                                      "player2_ind": data["player2_ind"],
                                                      "player1_result": data["player1_result"],
                                                      "player2_result": data["player2_result"],
                                                      "start_date": data["start_date"],
                                                      "end_date": data["end_date"],
                                                      "time_control": data["time_control"]})"""

    def data_tmnt_insert(self, data):
        # creation data tournament  to put in the tiny database
        (TinyDB(self.path).table(self.table)).insert({"id": data['id'], "name": data["name"],
                                                     "place": data["place"], "start_date": data["start_date"],
                                                      "end_date": data["end_date"],
                                                      "time_control": data["time_control"],
                                                      "round_number": data["round_number"], 'state': "open"})

    def create(self, *args, **kwargs):
        # print(*args)
        # print(**kwargs)
        item = self.collection_type(*args, **kwargs)
        self.collection[item.id] = item
        return item

    def read_all(self):
        return list(self.collection.values())

    def read(self, id):
        return self.collection[id]

    def modify_by_id(self, id):
        print(type(self.collection[id]))
        return self.collection[id]


"""
# __main__ = "__main__"


manager = Manager('./data_players2.json', 'players_list')
all_db_data, count = manager.load_all_from_tinydb()
m_query = manager.search_to_tinydb_by_id(5)
print(all_db_data)
print(m_query)
test = manager.db_initial()
print(test)
"""
