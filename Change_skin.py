import pygame
import random

pygame.init()
pygame.mixer.init()

display_width = 650
display_height = 650
boll_width = 20
boll_height = 20


Boll_green = pygame.image.load('images\\Boll_skins\\Boll_green.png')
Boll_yellow = pygame.image.load('images\\Boll_skins\\Boll_yellow.png')
Boll_pink = pygame.image.load('images\\Boll_skins\\Boll_pink.png')
Boll_blue = pygame.image.load('images\\Boll_skins\\Boll_blue.png')
Boll_white = pygame.image.load('images\\Boll_skins\\Boll_white.png')
Boll_red = pygame.image.load('images\\Boll_skins\\Boll_red.png')

def boll_color():
	Boll_skin = random.choice((Boll_green, Boll_yellow, Boll_pink, Boll_blue, Boll_white, Boll_red))
	return Boll_skin

Platform_first_skin = pygame.image.load('images\\Platform_skins\\Platform_first_skin.png')


def platform_color():
	Platform_skin = Platform_first_skin
	return Platform_skin