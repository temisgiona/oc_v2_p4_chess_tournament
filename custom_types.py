from enum import Enum
import re

class Gender(Enum):
    Male = "M"
    Female = "F"


class Name(str):
    def __new__(cls, value):
        if not re.match("^[a-zA-Z \-'ïöéè]{2,25}$", value):
            raise ValueError()

        return  str.__new__(cls, value.title())

class TimeControl(Enum):
    bullet = "Bullet"
    blitz = "Blitz"
    coups_rapide = "Coups rapide"



