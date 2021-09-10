from typing import List
from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field, validator
import databases
from pydantic.class_validators import Validator
from pydantic.types import PositiveInt
import sqlalchemy
from datetime import datetime, date
from custom_types import Name, Gender, TimeControl
from utils import convert_date_to_check_is_past
#import controler


class Player(BaseModel):
    id: PositiveInt
    lastname: Name
    firstname: Name
    gender: Gender
    birthdate: date
    rank: PositiveInt
    #indice: str = "A"
    #date_created: datetime

    @validator('birthdate')
    def check_date(cls, value):
        if not convert_date_to_check_is_past(value):
            raise ValueError('la date est dans le futur, date invalide !')

"""
def convert_date_to_check_is_past(birth_date):
    birth_date = date(2001, 10, 10)
    today = date.today()
    if today > birth_date:
        print('today is', today)
        return True
    else:
        print(
            "votre date anniversaire est dans le futur,changez la date ou faites un saut dans le temps vers",
            birth_date
        )
        return False
"""
"""
class PlayerIn(BaseModel):
    id: PositiveInt
    name: Name
    firstname: Name
    birthday: date
    gender: Gender
    rank: PositiveInt
    score: float
    indice: str

"""
class tournament(BaseModel):
    name: Name
    city: Name
    Start_date: date
    End_date: date
    Round_number: PositiveInt
    time_control: TimeControl
    description: str = ""
    
    """
    @validator('name') 
    def no_space_in_name(cls, ):
    
    @validator('city')
    def only_letter_in_city(cls, value):
    
    @validator('Round_number')
    def only_number_in_Round_number(cls, value):

    @validator('time_control')
    def only_number_in_time_control(cls, value):

"""
class match(BaseModel):
    j1: str
    j2: str
    winner: str #
    j1_score: float
    j2_score: float
    Start_date: datetime
    End_date: datetime
    Round_number: PositiveInt
    chess_number: PositiveInt
    time_control: TimeControl   
    description: str = ""
"""
    @validator('j1')
    def only_letter_in_j1(cls, value):

    @validator('j2')
    def only_letter_in_j2(cls, value):
    
    @validator('Round_number')
    def only_number_in_Round_number(cls, value):

    @validator('time_control')
    def only_number_in_time_control(cls, value):
    
    @validator('city')
    def only_letter_in_city(cls, value):
    
    @validator('Round_number')
    def only_number_in_Round_number(cls, value):

    @validator('time_control')
    def only_number_in_time_control(cls, value):
        """