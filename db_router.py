from tinydb import TinyDB, Query, where


db_players = TinyDB('./data_players2.json')
#db_players = TinyDB('./data.json')

#db_players.insert({"id": 12, "lastname": "Carlito", "firstname": "Maglito", "birthdate": "1990-11-30", "gender": "M", "rank": "2847", "score": 0})
#print(db_players.all())
#for item in db_players:
#     print(item)

player = Query()
#print(db_players.search(player.id == 8))
#print(db_players.count(player.id == 12))
print(db_players.search(where('lastname') == 'Carlsen'))