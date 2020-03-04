import pygame
import random

pygame.init()
pygame.mixer.init()

display_width = 650
display_height = 650
boll_width = 15
boll_height = 15
platform_width = 90
platform_height = 15


Boll_green = pygame.image.load('images\\Boll_skins\\Boll_green.png')
Boll_yellow = pygame.image.load('images\\Boll_skins\\Boll_yellow.png')
Boll_pink = pygame.image.load('images\\Boll_skins\\Boll_pink.png')
Boll_blue = pygame.image.load('images\\Boll_skins\\Boll_blue.png')
Boll_white = pygame.image.load('images\\Boll_skins\\Boll_white.png')
Boll_red = pygame.image.load('images\\Boll_skins\\Boll_red.png')

Boll_green = pygame.transform.scale(Boll_green,(boll_width, boll_height))
Boll_yellow = pygame.transform.scale(Boll_yellow,(boll_width, boll_height))
Boll_pink = pygame.transform.scale(Boll_pink,(boll_width, boll_height))
Boll_blue = pygame.transform.scale(Boll_blue,(boll_width, boll_height))
Boll_white = pygame.transform.scale(Boll_white,(boll_width, boll_height))
Boll_red = pygame.transform.scale(Boll_red,(boll_width, boll_height))


Bolls = [Boll_green, Boll_green, Boll_blue, Boll_pink, Boll_red, Boll_white, Boll_yellow]


Platform_first_skin = pygame.image.load('images\\Platform_skins\\Platform_first_skin.png')
Platform_second_skin = pygame.image.load('images\\Platform_skins\\Platform_second_skin.png')
Platform_third_skin = pygame.image.load('images\\Platform_skins\\Platform_third_skin.png')

Platform_first_skin = pygame.transform.scale(Platform_first_skin, (platform_width, platform_height))
Platform_second_skin = pygame.transform.scale(Platform_second_skin, (platform_width, platform_height))
Platform_third_skin = pygame.transform.scale(Platform_third_skin, (platform_width, platform_height))


Platforms = [Platform_first_skin, Platform_first_skin, Platform_second_skin, Platform_third_skin]

platform_color = Platform_second_skin 