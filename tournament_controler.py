from pydantic import BaseModel
from manager_txt import Manager
import models
from view import *

def tournament_register(data,DATAPATH, DB_TOURNAMENTS):
    # to create the database with data from view
    tnmt_manager = Manager(DATAPATH, DB_TOURNAMENTS)
    tnmt_manager.data_tmnt_insert(data)
    tnmt_manager.id_readjust()


