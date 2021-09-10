"crud db tiny"
import json
from typing import Any

class Manager:
    def __init__(self, collection_type: Any):
        self.collection = {}
        self.collection_type = collection_type

    def load_from_json(self, path):

        with open(path) as file:
            for data in json.load(file):
                self.create(**data)
    
    def create(self, *args, **kwargs):
        item = self.collection_type(*args, **kwargs)
        self.collection[item.id] = item
        return item
     
    def read_all(self):
        return list(self.collection.values())

    def read(self, id):
        return self.collection[id]
    
