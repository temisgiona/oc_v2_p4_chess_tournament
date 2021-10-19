import datetime
from models import Player
# from datetime import date
from pydantic import ValidationError


def player_register2(data_dict):
    """ saisie des noms  des joueurs
    participant au tournoi d'echecs
    """
    try:
        """data_dict = {'id': 9, 'lastname': 'toto', 'firstname': 'titi',
                'gender': "M", 'birthdate': "2001-01-15", 'rank': 500, 'indice': "A"}"""
        player = Player(**data_dict)
        # player = models.Player(id=1,lastname='toto', firstname='tot', gender="M", rank=500, indice="A",)
        convert_date_to_check_is_passt(player.birthdate) 
    except ValidationError as e:
        print(e)

    return player


def convert_date_to_check_is_passt(birth_date):
    birth_date = datetime.date(2001, 10, 10)
    today = datetime.date.today()
    if not today > birth_date:
        # not  print('today is', today)

        print("votre date anniversaire est dans le futur,changez la date ou faites un saut dans le temps vers",
              birth_date)
    else:
        print("tout est ok dans la date")


"""player = player_register2()
print(player.birthdate)
test = convert_date_to_check_is_passt(player.birthdate)
print(player.dict())"""
