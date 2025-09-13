import pygame
import Screens.options as option
import Screens.play as play
from Assets.PythonFiles.font import get_font
from Assets.PythonFiles.button import Button

def menu(screen, back_ground, settings):
    screen.blit(back_ground,(0, 0))
    pygame.display.update()

    while True:
        mouse_pos = pygame.mouse.get_pos()
        play_button = Button(image=pygame.image.load("Assets/Button/Play Rect.png"), pos=(83, 275), 
                    text_input="PLAY", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
        options_button = Button(image=pygame.image.load("Assets/Button/Options Rect.png"), pos=(120, 325), 
                    text_input="OPTIONS", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
        quit_button = Button(image=pygame.image.load("Assets/Button/Quit Rect.png"), pos=(80, 375), 
                    text_input="QUIT", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
        
        for button in [play_button, options_button, quit_button]:
            button.changeColor(mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(mouse_pos):
                    play.play(screen, back_ground, settings)
                if options_button.checkForInput(mouse_pos):
                    option.options(screen, back_ground, settings)
                if quit_button.checkForInput(mouse_pos):
                    pygame.quit()
                
        pygame.display.flip()