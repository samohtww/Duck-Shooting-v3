import pygame
import Screens.menu as menu
from Assets.PythonFiles.font import get_font
from Assets.PythonFiles.button import Button

def play(screen, back_ground, settings):
    screen.fill("black")
    pygame.display.update()

    while True:
        options_text = get_font(45).render("Play", True, "white")
        options_rect = options_text.get_rect(center=(900, 35))
        screen.blit(options_text, options_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                menu.menu(screen, back_ground, settings)
            if keys[pygame.K_DOWN]:
                screen.fill("green")
                pygame.display.update()
                pygame.time.delay(5000)
                screen.fill("blue")
                pygame.display.update()
                pygame.time.delay(5000)
                screen.fill("red")
                pygame.display.update()
                pygame.time.delay(5000)
                screen.fill("purple")
                pygame.display.update()



        pygame.display.flip()