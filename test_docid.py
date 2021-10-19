from tinydb import TinyDB, Query, where

db_players = TinyDB('./data_players2.json').table('players_list')

for item in range(len(db_players.all())):
    el = db_players.all()[item]
    # on prend le doc id et on l'assigne id element
    # pour simp^lifier la requete
    
    if el.doc_id != el["id"]:
        db_players.update({'id': el.doc_id}, doc_ids=[el.doc_id])
        print(el)
  