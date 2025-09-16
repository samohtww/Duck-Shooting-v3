import pygame, pygame_widgets, os
import Screens.menu as menu
from Assets.PythonFiles.SIMPLE_FKN_BUTTON import simplefknButton

current_working_directory = os.path.dirname(__file__)

from Assets.PythonFiles.font import get_font
from Assets.PythonFiles.button import Button
from pygame_widgets.dropdown import Dropdown



Deer_1                = pygame.image.load("Assets/Targets/Animals/Deer2.PNG")
Frog_1                = pygame.image.load("Assets/Targets/Animals/Frog1.PNG")
Rabbit_1              = pygame.image.load("Assets/Targets/Animals/Rabbit1.PNG")
Dot_B_Hard            = pygame.image.load("Assets/Targets/Dots_and_Rings/Blue_Dot.PNG")
Dot_R_Hard            = pygame.image.load("Assets/Targets/Dots_and_Rings/Red_Dot.PNG")
Blue_ring             = pygame.image.load("Assets/Targets/Dots_and_Rings/Blue_Ring.PNG")
Red_ring              = pygame.image.load("Assets/Targets/Dots_and_Rings/Red_ring.PNG")
Duck_Easy_red         = pygame.image.load("Assets/Targets/ducks/Duck_easy_red.PNG")
Duck_easy_blue        = pygame.image.load("Assets/Targets/ducks/Duck_easy_blue.PNG")
placeholder           = pygame.image.load("Assets/Targets/ducks/Duck_easy_blue.PNG")
can                   = pygame.image.load("Assets/Targets/shooting targets/can.PNG")

imsel_1               = simplefknButton(400, 200, Deer_1, 0.75)
imsel_2               = simplefknButton(500, 200, Frog_1, 0.75)
imsel_3               = simplefknButton(600, 200, Rabbit_1, 0.75)
imsel_4               = simplefknButton(700, 200, Dot_B_Hard, 0.75)
imsel_5               = simplefknButton(800, 200, Dot_R_Hard, 0.75)
imsel_6               = simplefknButton(900, 200, Blue_ring, 0.75)
imsel_7               = simplefknButton(1000, 200, Red_ring, 0.75)
imsel_8               = simplefknButton(1100, 200, Duck_Easy_red, 0.75)
imsel_9               = simplefknButton(1200, 200, Duck_easy_blue, 0.75)
imsel_10              = simplefknButton(1300, 200, can, 0.75)


lanes = 2

def options(screen, back_ground, settings):
    screen.blit(back_ground,(0, 0))
    pygame.display.update()
    
    screen_size = pygame.display.get_window_size()
    width = screen_size[0]
    length = screen_size[1]

    events = pygame.event.get()
    # dropdown_1 = Dropdown(
    #     screen, 225, 100, 100, 30, name='Select image',
    #     choices=['Deer','Duck','Frog',],
    #     borderRadius=3, colour=pygame.Color('gray'), values=[Deer_1, Rabbit_1, Frog_1], direction='down', textHAlign='left')

    while True:
        options_text = get_font(45).render("General Settings", True, "Black")
        options_rect = options_text.get_rect(center=(width/2, length/10))
        screen.blit(options_text, options_rect)

        if imsel_1.draw(screen):
            lane_1 = lane_2 = lane_3 = lane_4 = lane_5 = lane_6 = lane_7 = lane_8 = Deer_1
            print("all img set to Deer")
        if imsel_2.draw(screen):
            lane_1 = lane_2 = lane_3 = lane_4 = lane_5 = lane_6 = lane_7 = lane_8 = Frog_1
            print("all img set to Frog")
        if imsel_3.draw(screen):
            lane_1 = lane_2 = lane_3 = lane_4 = lane_5 = lane_6 = lane_7 = lane_8 = Rabbit_1
            print("all img set to Rabbit")
        if imsel_4.draw(screen):
            lane_1 = lane_2 = lane_3 = lane_4 = lane_5 = lane_6 = lane_7 = lane_8 = Dot_B_Hard
            print("all img set to Dot Blue")
        if imsel_5.draw(screen):
            lane_1 = lane_2 = lane_3 = lane_4 = lane_5 = lane_6 = lane_7 = lane_8 = Dot_R_Hard
            print("all img set to Dot Red")
        if imsel_6.draw(screen):
            lane_1 = lane_2 = lane_3 = lane_4 = lane_5 = lane_6 = lane_7 = lane_8 = Blue_ring
            print("all img set to Blue ring")
        if imsel_7.draw(screen):
            lane_1 = lane_2 = lane_3 = lane_4 = lane_5 = lane_6 = lane_7 = lane_8 = Red_ring
            print("all img set to Red ring")
        if imsel_8.draw(screen):
            lane_1 = lane_2 = lane_3 = lane_4 = lane_5 = lane_6 = lane_7 = lane_8 = Duck_Easy_red
            print("all img set to Duck Red")
        if imsel_9.draw(screen):
            lane_1 = lane_2 = lane_3 = lane_4 = lane_5 = lane_6 = lane_7 = lane_8 = Duck_easy_blue
            print("all img set to Duck Blue")













        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                menu.menu(screen, back_ground, settings)

            if lanes >= 1:
                continue
            if lanes >= 2:
                continue
        
        pygame_widgets.update(events)
        pygame.display.update()

