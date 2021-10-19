"crud db tiny"
import json
from tinydb import TinyDB, Query
from typing import Any


class Manager:
    def __init__(self, collection_type: Any):
        self.collection = {}
        self.collection_type = collection_type

    def load_from_json(self, path):
        with open(path) as file:
            for data in json.load(file):
                self.create(**data)
    
    def load_from_tinydb(self, path, m_table):
        # stockage de la base de données
        db = TinyDB(path).table(m_table)
        #return db
        
        for data in db:
            self.create(**data)
            print(data)

    def create(self, *args, **kwargs):
        print(*args)
        #print(**kwargs)
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


players = {}
manager = Manager(players)
TinyDB('./data_players2.json').table('players_list')
test = manager.load_from_tinydb('./data_players2.json', 'players_list')
print(test)

