import datetime
from models import Player
from datetime import date
from pydantic import BaseModel, ValidationError, root_validator


def player_register():
    """ saisie des noms  des joueurs 
    participant au tournoi d'echecs
    """
    
    player = Player()
    
    try:
        player.lastname = input(" Veuillez entrer le nom du joueur")
        player.firstname = input(" Veuillez entrer le prénom du joueur")
        player.gender = input("Donner le sexe de la personne, SVP.(M ou F)")
        player.birthdate = input(" Veuillez entrer la date de naissance du joueur")
        player.rank = input(" Veuillez entrer le rang du joueur. (0 à 3000)")
    
    except ValidationError as e:
        print(e)
    
    return player

def player_register2():
    """ saisie des noms  des joueurs 
    participant au tournoi d'echecs
    """
    try:
        player = models.Player(id=1,lastname='toto', firstname='tot', gender="M", birthdate=date(2001,10,5), rank=500, indice="A",)
        #player = models.Player(id=1,lastname='toto', firstname='tot', gender="M", rank=500, indice="A",)
        """
        player.lastname = input(" Veuillez entrer le nom du joueur")
        player.firstname = input(" Veuillez entrer le prénom du joueur")
        player.gender = input("Donner le sexe de la personne, SVP.(M ou F)")
        player.birthdate = input(" Veuillez entrer la date de naissance du joueur")
        player.rank = input(" Veuillez entrer le rang du joueur. (0 à 3000)")
        """
    except ValidationError as e:
        print(e)
    
    return Player()

def convert_date_to_check_is_passt(birth_date):
    birth_date = datetime.date(2001, 10, 10)
    today = datetime.date.today()
    if today > birth_date:
        print('today is', today)
    else: 
        print(
            "votre date anniversaire est dans le futur,changez la date ou faites un saut dans le temps vers",
            birth_date
        )
    #print(birth_date < today) 


birth_date = (2001, 10, 12)
#test = convert_date_to_check_is_passt(birth_date)
player = player_register()

