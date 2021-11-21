# from os import name
from typing import List
# from fastapi import FastAPI, Depends
from pydantic import BaseModel, validator
# import databases
from pydantic.class_validators import Validator
from pydantic.types import PositiveFloat, PositiveInt
# import sqlalchemy
from datetime import datetime, date
from custom_types import Name, Gender, Results, TimeControl
from utils import convert_date_to_check_is_past


class Player(BaseModel):
    id: PositiveInt
    lastname: Name
    firstname: Name
    gender: Gender
    birthdate: date
    rank: PositiveInt
    score: float = None
    indice: str = None

    @validator('birthdate')
    def check_date(cls, value):
        if not convert_date_to_check_is_past(value):
            raise ValueError('la date est dans le futur, date invalide !')
        else:
            return value


class Tournament(BaseModel):
    id: int
    name: Name
    place: Name
    start_date: datetime = datetime.today()
    end_date: datetime = None
    round_number: PositiveInt
    time_control: TimeControl
    # description: str = ""


"""class Turn(BaseModel):
    id: int
    id_tournament: int
    number = int
    start_date: date = None
    end_date: date = None"""


class Match(BaseModel):
    id: PositiveInt
    id_turn: int
    id_tournament: PositiveInt
    name: Name
    player1_id: PositiveInt
    player2_id: PositiveInt
    player1_ind: str = None
    player2_ind: str = None
    player1_result: float = None
    player2_result: float = None
    start_date: date = None
    end_date: date = None
    # time_control: TimeControl = None
    # time_control: str

    def serialized(self):
        return {'id': self.id, 'id_tournament': self.id_tournament,
                "start_date": self.start_date, "end_date": self.end_date}


class Turn:
    def __init__(self, data_type: any):
        # self.data = {}
        self.id = data_type['id']
        self.id_tournament = data_type['id_tournament']
        self.number = data_type['number']
        self.start_date = data_type['start_date']
        self.end_date = data_type['end_date']

    def serialized(self):
        return {'id': self.id, 'id_tournament': self.id_tournament, 'number': self.number,
                "start_date": self.start_date, "end_date": self.end_date}


class GameTemp:
    def __init__(self, game: any):
        self.game = game


class Player_Chess:
    def __init__(self, data_type: any):
        self.id = data_type['id']
        self.lastname = data_type['lastname']
        self.firstname = data_type['firstname']
        self.birthdate = data_type['birthdate']
        self.gender = data_type['gender']
        self.rank = data_type['rank']
        self.score = data_type['score']
    
    def serialized(self):
        return {'id': self.id, 'lastname': self.lastname, 'firstname': self.firstname, 'birthdate': self.birthdate,
                'gender': self.gender, 'rank': self.gender, 'score': self.score}
