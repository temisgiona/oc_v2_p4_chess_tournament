"crud db tiny"
import json
from tinydb import TinyDB, Query, where
from typing import Any
#from generic_models import Player

class Manager:
    #def __init__(self, path, table, collection_type: Any):
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

    def search_to_tinydb_by_id(self, key):
        # search on tiny db database
        # return a dict with all elements

        query = (TinyDB(self.path).table(self.table)).search(where('id') == key)
        return query

    def serialize_query(self, query):
        # return data serialized , doc --> dict  unable to easy transfert
        for item in range(len(query)):
            # query[0] is the is the id's position 
            serialized_data = query[0]  
            return serialized_data
   
    def player_serialized(self):
        # catch the data list from tiny and format the list for matching system

        db_manager = (TinyDB(self.path).table(self.table))
        player_object_list = []
        list_player_object = []
        for item in range(len(db_manager.all())):
            element_id = db_manager.all()[item]
            print('element id ', element_id)
            #player_object_list.append(0].append(element_id["lastname"])
            for d in range(7):
                player_object_list.append(0)
            player_object_list[0] = element_id["lastname"]
            player_object_list[1] = element_id["firstname"]
            player_object_list[2] = element_id["rank"]
            player_object_list[3] = 0
            player_object_list[4] = 0
            player_object_list[5] = element_id["id"]

            # player_object_list.append(element_id["id"])
           
            list_player_object.append(player_object_list)
            player_object_list = []
            print(list_player_object)
        return list_player_object

    def players_all_data_serialized(self):
        #catch the data list from tiny and format the list for reporting system
        db_manager = (TinyDB(self.path).table(self.table))
        player_object_list = []
        list_player_object = []
        for item in range(len(db_manager.all())):
            element_id = db_manager.all()[item]
            # print('element id ', element_id)
            # player_object_list.append(0].append(element_id["lastname"])
            for d in range(7):
                player_object_list.append(0)
            player_object_list[0] = element_id["id"]    
            player_object_list[1] = element_id["lastname"]
            player_object_list[2] = element_id["firstname"]
            player_object_list[3] = element_id["birthdate"]
            player_object_list[4] = element_id["gender"]
            player_object_list[5] = element_id["rank"]
            player_object_list[6] = element_id["score"]
            

            # player_object_list.append(element_id["id"])
           
            list_player_object.append(player_object_list)
            player_object_list = []
            # print(list_player_object)
        return list_player_object


    def update_player_tmnt(self, player_t0_u):
        # update player indice , and score 26/10/2021
        db_manager = (TinyDB(self.path).table(self.table))
        m_query = Query()
        db_manager.update({'score': player_t0[3]}, m_query.id == player_t0[5])
        # db_manager.update({'score': player_t0[3]}, m_query.type'id') == player_t0[5])
        print(player_t0)  
            
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

        (TinyDB(self.path).table(self.table)).insert({"id": 1000, "lastname": data["lastname"],
                                                     "firstname": data["firstname"], "gender": data["gender"],
                                                      "birthdate": data["birthdate"], "rank": data["rank"],
                                                      "score": data["score"]})
                           
    def data_tmnt_insert(self, data):
        # creation data tournament  to put in the tiny database
        (TinyDB(self.path).table(self.table)).insert({"id": 1000, "name": data["name"],
                                                     "place": data["place"], "start_date": data["start_date"],
                                                      "end_date": data["end_date"],
                                                      "time_control": data["time_control"],
                                                      "round_number": data["round_number"]})

        """    id: PositiveInt
                    name: Name
                    place: Name
                    start_date: datetime = datetime.today()
                    end_date: datetime = None
                    round_number: PositiveInt
                    time_control: TimeControl
                    description: str = """



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