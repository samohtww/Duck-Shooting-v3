#       Aantal spelers      gamemode     profiel       speler1(plaatje, grote)       speler2
settings = (2,                  3,          4,              (1,      1),             (2,2),       )

aantal_spelers = settings[0]
gamemode = settings[1]
profiel = settings[2]
speler1 = settings[3]
speler2 = settings[4]

counter = 3
for i in range(aantal_spelers):
    speler = settings[counter]
    counter += 1
    print(speler)