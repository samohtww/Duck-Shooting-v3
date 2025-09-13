import pygame
import Screens.menu as menu

pygame.init()
screen = pygame.display.set_mode((1800, 400))
back_ground = pygame.image.load("Assets/Pictures/Black_background_3.jpg")
settings = []

menu.menu(screen, back_ground, settings)