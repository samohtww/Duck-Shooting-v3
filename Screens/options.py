import pygame, pygame_widgets
import Screens.menu as menu
from Assets.PythonFiles.font import get_font
from Assets.PythonFiles.button import Button
from pygame_widgets.dropdown import Dropdown

Duck_1 = pygame.image.load("Assets/Pictures/Duck_easy_blue.PNG")
Deer_1 = pygame.image.load("Assets/Pictures/Deer1.PNG")
Frog_1 = pygame.image.load("Assets/Pictures/Frog1.PNG")

lanes = 2

def options(screen, back_ground, settings):
    screen.blit(back_ground,(0, 0))
    pygame.display.update()
    
    screen_size = pygame.display.get_window_size()
    width = screen_size[0]
    length = screen_size[1]

    events = pygame.event.get()
    dropdown_1 = Dropdown(
        screen, 225, 100, 100, 30, name='Select image',
        choices=['Deer','Duck','Frog',],
        borderRadius=3, colour=pygame.Color('gray'), values=[Deer_1, Duck_1, Frog_1], direction='down', textHAlign='left')

    while True:
        options_text = get_font(45).render("General Settings", True, "Black")
        options_rect = options_text.get_rect(center=(width/2, length/10))
        screen.blit(options_text, options_rect)

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

