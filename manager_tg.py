"crud db tiny"
import json
from tinydb import TinyDB, Query, where
from typing import Any
#from generic_models import Player

class Manager:
    # def __init__(self, path, table, collection_type: Any):
    def __init__(self, path, table):
        #self.collection = {}
        self.path = path
        self.table = table
        #self.collection_type = collection_type
    

    def load_from_json(self, path):
        with open(path) as file:
            for data in json.load(file):
                self.create(**data)
        
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

    def search_to_tinydb(self, key):
        # search on tiny db database
        # return a dict with all elements

        query = (TinyDB(self.path).table(self.table)).search(where('id') == key)
        return query

    def data_insert(self, data):
        # creation data player  to put in the tiny database

        (TinyDB(self.path).table(self.table)).insert({"id": 1000, "lastname": data["lastname"],
                                                        "firstname": data["firstname"], "gender": data["gender"],
                                                        "birthdate": data["birthdate"], "rank": data["rank"], "score": data["score"]})

                                  
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

#__main__ = "__main__"
players = {}
#manager = Manager('./data_players2.json', 'players_list',players )
manager = Manager('./data_players2.json', 'players_list')
all_db_data, count = manager.load_all_from_tinydb()
m_query = manager.search_to_tinydb(5)
"""print(all_db_data)
print(m_query)
test = manager.db_initial()
print(test)"""

