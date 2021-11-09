from datetime import date


def convert_date_to_check_is_past(birth_date):
    """verification de la position de la date dans le temps
    si elle est dans le futur elle est rejetée
    """
    birth_date = date(2001, 10, 10)
    today = date.today()
    if today > birth_date:
        #print('today is', today)
        return True
    else:
        print(
            "votre date anniversaire est dans le futur,changez la date ou faites un saut dans le temps vers",
            birth_date
        )
        return False