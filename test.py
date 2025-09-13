import random

#       Aantal spelers      gamemode     profiel       speler1(plaatje, grote)       speler2
settings = [2,                  3,          4,              [1,      1],             [2,2]       ]
preset_matthew_cas_amber = [3, 1, 2, [5, 2, "matthew"], [2, 1, "cas"], [4, 5, "amber"] ]
empty_list = []

#algemene settings uit de lijst
aantal_spelers = preset_matthew_cas_amber[0]
gamemode = preset_matthew_cas_amber[1]

#bereken coordinaten
width = 1920
target_tussen = 50
height = 400
coordinates_list = []

for i in range(aantal_spelers):
    x = random.randint(((width-target_tussen-20)//aantal_spelers)*(i)+10,(((width-target_tussen-20)//aantal_spelers)*(i+1)-10))
    y = random.randint(0,(height-target_tussen-50))
    coordinates_list.append([x,y])
    
    print(coordinates_list)


# loopen door speler lijsten
lijst_index = 3
for i in range(aantal_spelers):
    player = preset_matthew_cas_amber[lijst_index]

    player_image =                      player[0]
    player_image_size_multiplier =      player[1]
    player_name =                       player[2]

    #funtie om plaatje op scherm te laten verschijnen (gebruikt de coordinaten uit de coordinaten lijst)
    
    #RESIZE IMAGE TO FIT player_image_size_multiplier
    #SCREEN.blit(image_list[i],(coordinates_list[x][0],coordinates_list[x][1]))

    lijst_index += 1
    print(player_name + " heeft de volgende settings:")
    print("Plaatje: " + str(player_image))
    print("Grote plaatje: " + str(player_image_size_multiplier))


# x = 0
# for i in range(aantal_spelers):
#     x -= 1
#     
#     # Dk_proj(coordinates_list,image_list)