import models
"""
class Turn:
    def __init__(self, data_type: any):
        self.data = {}
        self.id = data_type['id']
        self.id_tournament = data_type['id_tournament']
        self.number = data_type['number']
        self.start_date = data_type['start_date']
        self.end_date = data_type['end_date']

turn_list = []

for i in range(5):
    turn_data = {"id": i, "id_tournament": i*2, "number": i*2+1, "start_date": "2021-10-16", "end_date": "2021-10-16"}
    turn_list.append(Turn(turn_data))
# id_list_turn = list(map(lambda x : str(x.id) + ": " + str(x.start_date), turn_list))
id_list_turn = list(map(lambda x : [str(x.id),  str(x.start_date)], turn_list))
print(id_list_turn)"""

data = {"id": 1, "id_tournament": 2, "number": 1, "start_date": "2021-10-16", "end_date": "2021-10-16"}
data2 = {"id": 1, "id_turn": 1, "id_tournament": 2, "name": "E1", "player1_id": 1, "player2_id": 2, "player1_result": 0, "player2_result": 1, "start_date": "2021-10-30", "end_date": "2021-10-30", "time_control": "r" }
my_turn = models.Turn(data)
print(my_turn.id)
test = my_turn.serialized()
print(test)
my_turn = models.Turn(test)
print(my_turn.id)
my_match = models.Match(data2)
test2 = my_match.serialized()
print(test2)
