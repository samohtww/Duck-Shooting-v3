import pygame, sys
import Screens.menu as menu
from Assets.PythonFiles.font import get_font
from Assets.PythonFiles.button import Button

def play(screen, back_ground, settings):
    screen.fill("black")
    pygame.display.update()
    clock = pygame.time.Clock()
    timer = sys.maxsize
    dt = 0
    color = ""

    while True:
        options_text = get_font(45).render("Play", True, "white")
        options_rect = options_text.get_rect(center=(900, 35))
        screen.blit(options_text, options_rect)
        
        timer -= dt  # Decrement the timer by the delta time.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                menu.menu(screen, back_ground, settings)
            if keys[pygame.K_DOWN]:
                timer = 5

        if timer <= 0 and color == "":  # When the time is up ...
            color = "green"
            screen.fill("green")
            pygame.display.update()
            timer = 5
        if timer <= 0 and color == "green":  # When the time is up ...
            color = "blue"
            screen.fill("blue")
            pygame.display.update()
            timer = 5
        if timer <= 0 and color == "blue":  # When the time is up ...
            color = "red"
            screen.fill("red")
            pygame.display.update()
            timer = 5
        if timer <= 0 and color == "red":  # When the time is up ...
            color = "purple"
            screen.fill("purple")
            pygame.display.update()
            timer = sys.maxsize

        dt = clock.tick(60) / 1000

        pygame.display.flip()