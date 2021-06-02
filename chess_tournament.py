import itertools


# def players():
"""
list of player for the tournament
 affectation d'un id  compilant , dictionnaire 

"""

play1 = 10
play2 = 5
play3 = 4
play4 = 6
play5 = 7
play6 = 2
play7 = 1
play8 = 8

""" tour 1
"""
tour1 = [play1, play2, play3]
play1 = 11
tour2 = (play1, play2, play3)
# play1 = 11
print("tour2 = ", (tour2))
tour1.sort()
print(tour1)

players_t0 = [
    ['t', 'g', 4, 3],
    ['e', 'f', 8, 2],
    ['a', 'b', 3, 1],
    ['k', 'l', 15, 0],
    ['m', 'n', 15, 0],
    ['o', 'r', 15, 0],
    ['p', 's', 15, 0],
    ['q', 't', 15, 0]
     ]
a = players_t0[2][1]
print(a)
b = sorted(players_t0, key=lambda t: t[2])
print(b)
