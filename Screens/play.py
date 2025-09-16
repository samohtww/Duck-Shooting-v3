import pygame, sys
import Screens.menu as menu
from Assets.PythonFiles.font import get_font
from Assets.PythonFiles.button import Button

pygame.mixer.init()
ping_sound = pygame.mixer.Sound("Assets/sounds/ping.mp3")

def play(screen, back_ground, settings):
    screen.fill("black")
    pygame.display.update()
    clock = pygame.time.Clock()
    timer = sys.maxsize
    dt = 0
    modus = ""
    maxInterval = 3

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
                modus = "Prepare"
                interval = 1

        if timer <= 0 and modus == "Prepare" and interval <= maxInterval:
            roundtext = "Ronde " + str(interval)
            pygame.mixer.Sound.play(ping_sound)
            timer = 5
            modus = "Shooting"
            
            # Dit is om te laten zien dat het werkt, zodra er logica aan toegevoegd wordt kan dit weg
            screen.fill("red")
            pygame.display.update()

            # Dit moet na de update() anders wordt het namelijk meteen weer weggehaald
            round_text = get_font(45).render(roundtext, True, "white")
            round_rect = round_text.get_rect(center=(200, 35))
            screen.blit(round_text, round_rect)
        if timer <= 0 and modus == "Shooting":
            timer = 5
            interval += 1
            modus = "Prepare"
            
            # Dit is om te laten zien dat het werkt, zodra er logica aan toegevoegd wordt kan dit weg
            screen.fill("green")
            pygame.display.update()



        dt = clock.tick(60) / 1000

        pygame.display.flip()