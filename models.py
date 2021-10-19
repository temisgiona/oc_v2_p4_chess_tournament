# from os import name
from typing import List
# from fastapi import FastAPI, Depends
from pydantic import BaseModel, validator
# import databases
from pydantic.class_validators import Validator
from pydantic.types import PositiveInt
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
    id: PositiveInt
    name: Name
    place: Name
    start_date: datetime = datetime.today()
    end_date: datetime = None
    round_number: PositiveInt
    time_control: TimeControl
    description: str = ""


class Turn(BaseModel):
    id: PositiveInt
    id_tournament: PositiveInt
    number = PositiveInt
    start_date: datetime = None
    end_date: datetime = None
    description: str = ""


class Match(BaseModel):
    id: PositiveInt
    id_turn: PositiveInt
    id_tournament: PositiveInt
    name: Name
    j1: str
    j2: str
    j1_result: Results
    j2_result: Results
    start_date: datetime = None
    end_date: datetime = None
    time_control: TimeControl
  


