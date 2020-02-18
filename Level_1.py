import pygame
pygame.init()

display_width = 650
display_height = 650

display = pygame.display.set_mode((display_width, display_height))

Obj_green = pygame.image.load('images\\Object_skins\\Obj_green.png')
Obj_blue = pygame.image.load('images\\Object_skins\\Obj_blue.png')
Obj_purple = pygame.image.load('images\\Object_skins\\Obj_purple.png')
Obj_red = pygame.image.load('images\\Object_skins\\Obj_red.png')
Obj_yellow = pygame.image.load('images\\Object_skins\\Obj_yellow.png')


obj_green = pygame.transform.scale(Obj_green, (40, 15))
obj_blue = pygame.transform.scale(Obj_blue, (40, 15))
obj_purple = pygame.transform.scale(Obj_purple, (40, 15))
obj_red = pygame.transform.scale(Obj_red, (40, 15))
obj_yellow = pygame.transform.scale(Obj_yellow, (40, 15))


OBJ_WIDHT = 40
OBJ_HEIGT = 15
BLUE = (19, 31, 247)
YELLOW = (247, 255, 60)
GREEN = (45, 255, 60)
RED = (222, 17, 0)
PURPLE = (217, 0, 167)

broken = 0
obj_count = 0

# Первый ряд платформ
obj1_x = 29
obj1_y = 86
obj2_x = 71
obj2_y = 86
obj3_x = 113
obj3_y = 86
obj4_x = 155
obj4_y = 86
obj5_x = 197
obj5_y = 86
obj6_x = 239
obj6_y = 86
obj7_x = 281
obj7_y = 86
obj8_x = 323
obj8_y = 86
obj9_x = 365
obj9_y = 86
obj10_x = 407
obj10_y = 86
obj11_x = 449
obj11_y = 86
# Второй ряд платформ
obj12_x = 29
obj12_y = 104
obj13_x = 71
obj13_y = 104
obj14_x = 113
obj14_y = 104
obj15_x = 155
obj15_y = 104
obj16_x = 197
obj16_y = 104
obj17_x = 239
obj17_y = 104
obj18_x = 281
obj18_y = 104
obj19_x = 323
obj19_y = 104
obj20_x = 365
obj20_y = 104
obj21_x = 407
obj21_y = 104
obj22_x = 449
obj22_y = 104
# Третий ряд платформ
obj23_x = 29
obj23_y = 122
obj24_x = 71
obj24_y = 122
obj25_x = 113
obj25_y = 122
obj26_x = 155
obj26_y = 122
obj27_x = 197
obj27_y = 122
obj28_x = 239
obj28_y = 122
obj29_x = 281
obj29_y = 122
obj30_x = 323
obj30_y = 122
obj31_x = 365
obj31_y = 122
obj32_x = 407
obj32_y = 122
obj33_x = 449
obj33_y = 122
# Четвертый ряд платформ
obj34_x = 29
obj34_y = 140
obj35_x = 71
obj35_y = 140
obj36_x = 113
obj36_y = 140
obj37_x = 155
obj37_y = 140
obj38_x = 197
obj38_y = 140
obj39_x = 239
obj39_y = 140
obj40_x = 281
obj40_y = 140
obj41_x = 323
obj41_y = 140
obj42_x = 365
obj42_y = 140
obj43_x = 407
obj43_y = 140
obj44_x = 449
obj44_y = 140

def objects_skin():
	display.blit(obj_red, (obj1_x, obj1_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_blue, (obj2_x, obj2_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_yellow, (obj3_x, obj3_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_green, (obj4_x, obj4_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_purple, (obj5_x, obj5_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_red, (obj6_x, obj6_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_blue, (obj7_x, obj7_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_yellow, (obj8_x, obj8_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_green, (obj9_x, obj9_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_purple, (obj10_x, obj10_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_red, (obj11_x, obj11_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_blue, (obj12_x, obj12_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_yellow, (obj13_x, obj13_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_green, (obj14_x, obj14_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_purple, (obj15_x, obj15_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_red, (obj16_x, obj16_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_blue, (obj17_x, obj17_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_yellow, (obj18_x, obj18_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_green, (obj19_x, obj19_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_purple, (obj20_x, obj20_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_red, (obj21_x, obj21_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_blue, (obj22_x, obj22_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_yellow, (obj23_x, obj23_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_green, (obj24_x, obj24_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_purple, (obj25_x, obj25_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_red, (obj26_x, obj26_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_blue, (obj27_x, obj27_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_yellow, (obj28_x, obj28_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_green, (obj29_x, obj29_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_purple, (obj30_x, obj30_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_red, (obj31_x, obj31_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_blue, (obj32_x, obj32_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_yellow, (obj33_x, obj33_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_green, (obj34_x, obj34_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_purple, (obj35_x, obj35_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_red, (obj36_x, obj36_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_blue, (obj37_x, obj37_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_yellow, (obj38_x, obj38_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_green, (obj39_x, obj39_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_purple, (obj40_x, obj40_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_red, (obj41_x, obj41_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_blue, (obj42_x, obj42_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_yellow, (obj43_x, obj43_y, OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_green, (obj44_x, obj44_y, OBJ_WIDHT, OBJ_HEIGT))

obj34_brok= True
obj35_brok = True


def check_obj_brocken(boll_x, boll_y):
	global broken, obj_count, obj34_x, obj34_y, obj35_x, obj35_y, obj36_x, obj36_y,obj37_x, obj37_y, obj38_x, obj38_y, \
	obj39_x, obj39_y, obj40_x, obj40_y, obj41_x, obj41_y, obj42_x, obj42_y, obj43_x, obj43_y, obj44_x, obj44_y, obj34_brok, obj35_brok
	if 150>=boll_y<=153:
		if obj34_brok:
			if  69 >= boll_x and boll_x+20 >= 29 :
				obj34_x = 550
				obj34_y = 100
				broken = 1
				obj_count += 1
				obj34_brok = False
		if obj35_brok:
			if 111 >= boll_x and boll_x+20 >= 71 :
				obj35_x = 550
				obj35_y = 100
				broken = 1
				obj_count += 1
				obj35_brok = False

