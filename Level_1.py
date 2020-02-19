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
Obj_white = pygame.image.load('images\\Object_skins\\Obj_white.png')


obj_green = pygame.transform.scale(Obj_green, (40, 15))
obj_blue = pygame.transform.scale(Obj_blue, (40, 15))
obj_purple = pygame.transform.scale(Obj_purple, (40, 15))
obj_red = pygame.transform.scale(Obj_red, (40, 15))
obj_yellow = pygame.transform.scale(Obj_yellow, (40, 15))
obj_white = pygame.transform.scale(Obj_white, (40, 15))

OBJ_WIDHT = 40
OBJ_HEIGT = 15
BLUE = (19, 31, 247)
YELLOW = (247, 255, 60)
GREEN = (45, 255, 60)
RED = (222, 17, 0)
PURPLE = (217, 0, 167)
WHITE = (255, 255, 255)

broken = 0
broken_x = 0
obj_count = 0
obj_main_x = 550
obj_main_y = 100



#Первый ряд
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
# Второй ряд
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
# Третий ряд
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
# Четвертый ряд
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
	display.blit(obj_white, (obj_main_x, obj_main_y, OBJ_WIDHT, OBJ_HEIGT))
	print_obj_count(('X' + str(40-obj_count)),596, 92)


def print_obj_count(messege, x, y, font_color = (WHITE), font_type = 'GameFont.ttf', font_size = 30):
	font_type = pygame.font.Font(font_type, font_size)
	text = font_type.render(messege, True, font_color)
	display.blit(text, (x, y))


obj23_brok = obj24_brok = obj25_brok = obj26_brok = obj27_brok = obj28_brok = \
obj29_brok = obj30_brok = obj31_brok = obj32_brok = obj33_brok = True
obj34_brok = obj35_brok = obj36_brok = obj37_brok = obj38_brok = obj39_brok = \
obj40_brok = obj41_brok = obj42_brok = obj43_brok = obj44_brok = True
obj12_brok = obj13_brok = obj14_brok = obj15_brok = obj16_brok = obj17_brok = \
obj18_brok = obj19_brok = obj20_brok = obj21_brok = obj22_brok = True
obj1_brok = obj2_brok = obj3_brok = obj4_brok = obj5_brok = obj6_brok = \
obj7_brok = obj8_brok = obj9_brok = obj10_brok = obj11_brok = True


def check_obj_brocken(boll_x, boll_y):
	global broken, broken_x, obj_count, obj34_x, obj34_y, obj35_x, obj35_y, obj36_x, obj36_y, obj37_x, obj37_y, obj38_x, obj38_y, \
	obj39_x, obj39_y, obj40_x, obj40_y, obj41_x, obj41_y, obj42_x, obj42_y, obj43_x, obj43_y, obj44_x, obj44_y, \
	obj34_brok, obj35_brok, obj36_brok, obj37_brok, obj38_brok, obj39_brok, obj40_brok, obj41_brok, obj42_brok, obj43_brok, obj44_brok, \
	obj23_x, obj23_y, obj24_x, obj24_y, obj25_x, obj25_y, obj26_x, obj26_y, obj27_x, obj27_y, obj28_x, obj28_y, obj29_x, obj29_y, obj30_x,\
	obj30_y, obj31_x, obj31_y, obj32_x, obj32_y, obj33_x, obj33_y, obj23_brok, obj24_brok, obj25_brok, obj26_brok, obj27_brok, obj28_brok, \
	obj29_brok, obj30_brok, obj31_brok, obj32_brok, obj33_brok, obj12_x, obj12_y, obj13_x, obj13_y, obj14_x, obj14_y, obj15_x, \
	obj15_y, obj16_x, obj16_y, obj17_x, obj17_y, obj18_x, obj18_y, obj19_x, obj19_y, obj20_x, obj20_y, obj21_x, obj21_y, obj22_x, obj22_y, \
	obj12_brok, obj13_brok, obj14_brok, obj15_brok, obj16_brok, obj17_brok, obj18_brok, obj19_brok, obj20_brok, obj21_brok, obj22_brok, \
	obj1_x, obj1_y, obj2_x, obj2_y, obj3_x, obj3_y, obj4_x, obj4_y, obj5_x, obj5_y, obj6_x, obj6_y, obj7_x, obj7_y, obj8_x, obj8_y,\
	obj9_x, obj9_y, obj10_x, obj10_y, obj11_x, obj11_y,	obj1_brok, obj2_brok, obj3_brok, obj4_brok, obj5_brok, obj6_brok, obj7_brok,\
	 obj8_brok, obj9_brok, obj10_brok, obj11_brok


# Отскок мяча по координате У

#Четвертый ряд
	if 154>=boll_y>=152:
		if obj34_brok:
			if  68 >= boll_x and boll_x+15 >= 28 :
				obj34_x = 550
				obj34_y = 100
				broken = 1
				obj_count += 1
				obj34_brok = False
		if obj35_brok:
			if 110 >= boll_x and boll_x+15 >= 70 :
				obj35_x = 550
				obj35_y = 100
				broken = 1
				obj_count += 1
				obj35_brok = False
		if obj36_brok:
			if 152 >= boll_x and boll_x+15 >= 112 :
				obj36_x = 550
				obj36_y = 100
				broken = 1
				obj_count += 1
				obj36_brok = False
		if obj37_brok:
			if 194 >= boll_x and boll_x+15 >= 154 :
				obj37_x = 550
				obj37_y = 100
				broken = 1
				obj_count += 1
				obj37_brok = False
		if obj38_brok:
			if 236 >= boll_x and boll_x+15 >= 196 :
				obj38_x = 550
				obj38_y = 100
				broken = 1
				obj_count += 1
				obj38_brok = False
		if obj39_brok:
			if 278 >= boll_x and boll_x+15 >= 238 :
				obj39_x = 550
				obj39_y = 100
				broken = 1
				obj_count += 1
				obj39_brok = False
		if obj40_brok:
			if 320 >= boll_x and boll_x+15 >= 280:
				obj40_x = 550
				obj40_y = 100
				broken = 1
				obj_count += 1
				obj40_brok = False
		if obj41_brok:
			if 362 >= boll_x and boll_x+15 >= 322 :
				obj41_x = 550
				obj41_y = 100
				broken = 1
				obj_count += 1
				obj41_brok = False
		if obj42_brok:
			if 404 >= boll_x and boll_x+15 >= 364 :
				obj42_x = 550
				obj42_y = 100
				broken = 1
				obj_count += 1
				obj42_brok = False
		if obj43_brok:
			if 446 >= boll_x and boll_x+15 >= 406 :
				obj43_x = 550
				obj43_y = 100
				broken = 1
				obj_count += 1
				obj43_brok = False
		if obj44_brok:
			if 488 >= boll_x and boll_x+15 >= 448 :
				obj44_x = 550
				obj44_y = 100
				broken = 1
				obj_count += 1
				obj44_brok = False
		
	
	if 140>=boll_y>=138:
		if obj34_brok:
			if  68 >= boll_x and boll_x+15 >= 28 :
				obj34_x = 550
				obj34_y = 100
				broken = -1
				obj_count += 1
				obj34_brok = False
		if obj35_brok:
			if 110 >= boll_x and boll_x+15 >= 70 :
				obj35_x = 550
				obj35_y = 100
				broken = -1
				obj_count += 1
				obj35_brok = False
		if obj36_brok:
			if 152 >= boll_x and boll_x+15 >= 112 :
				obj36_x = 550
				obj36_y = 100
				broken = -1
				obj_count += 1
				obj36_brok = False
		if obj37_brok:
			if 194 >= boll_x and boll_x+15 >= 154 :
				obj37_x = 550
				obj37_y = 100
				broken = -1
				obj_count += 1
				obj37_brok = False
		if obj38_brok:
			if 236 >= boll_x and boll_x+15 >= 196 :
				obj38_x = 550
				obj38_y = 100
				broken = -1
				obj_count += 1
				obj38_brok = False
		if obj39_brok:
			if 278 >= boll_x and boll_x+15 >= 238 :
				obj39_x = 550
				obj39_y = 100
				broken = -1
				obj_count += 1
				obj39_brok = False
		if obj40_brok:
			if 320 >= boll_x and boll_x+15 >= 280:
				obj40_x = 550
				obj40_y = 100
				broken = -1
				obj_count += 1
				obj40_brok = False
		if obj41_brok:
			if 362 >= boll_x and boll_x+15 >= 322 :
				obj41_x = 550
				obj41_y = 100
				broken = -1
				obj_count += 1
				obj41_brok = False
		if obj42_brok:
			if 404 >= boll_x and boll_x+15 >= 364 :
				obj42_x = 550
				obj42_y = 100
				broken = -1
				obj_count += 1
				obj42_brok = False
		if obj43_brok:
			if 446 >= boll_x and boll_x+15 >= 406 :
				obj43_x = 550
				obj43_y = 100
				broken = -1
				obj_count += 1
				obj43_brok = False
		if obj44_brok:
			if 488 >= boll_x and boll_x+15 >= 448 :
				obj44_x = 550
				obj44_y = 100
				broken = -1
				obj_count += 1
				obj44_brok = False

#Третий ряд
	if 137>=boll_y>=135:
		if obj23_brok:
			if  68 >= boll_x and boll_x+15 >= 28 :
				obj23_x = 550
				obj23_y = 100
				broken = 1
				obj_count += 1
				obj23_brok = False
		if obj24_brok:
			if 110 >= boll_x and boll_x+15 >= 70 :
				obj24_x = 550
				obj24_y = 100
				broken = 1
				obj_count += 1
				obj24_brok = False
		if obj25_brok:
			if 152 >= boll_x and boll_x+15 >= 112 :
				obj25_x = 550
				obj25_y = 100
				broken = 1
				obj_count += 1
				obj25_brok = False
		if obj26_brok:
			if 194 >= boll_x and boll_x+15 >= 154 :
				obj26_x = 550
				obj26_y = 100
				broken = 1
				obj_count += 1
				obj26_brok = False
		if obj27_brok:
			if 236 >= boll_x and boll_x+15 >= 196 :
				obj27_x = 550
				obj27_y = 100
				broken = 1
				obj_count += 1
				obj27_brok = False
		if obj28_brok:
			if 278 >= boll_x and boll_x+15 >= 238 :
				obj28_x = 550
				obj28_y = 100
				broken = 1
				obj_count += 1
				obj28_brok = False
		if obj28_brok:
			if 320 >= boll_x and boll_x+15 >= 280:
				obj28_x = 550
				obj28_y = 100
				broken = 1
				obj_count += 1
				obj28_brok = False
		if obj30_brok:
			if 362 >= boll_x and boll_x+15 >= 322 :
				obj30_x = 550
				obj30_y = 100
				broken = 1
				obj_count += 1
				obj30_brok = False
		if obj31_brok:
			if 404 >= boll_x and boll_x+15 >= 364 :
				obj31_x = 550
				obj31_y = 100
				broken = 1
				obj_count += 1
				obj31_brok = False
		if obj32_brok:
			if 446 >= boll_x and boll_x+15 >= 406 :
				obj32_x = 550
				obj32_y = 100
				broken = 1
				obj_count += 1
				obj32_brok = False
		if obj33_brok:
			if 488 >= boll_x and boll_x+15 >= 448 :
				obj33_x = 550
				obj33_y = 100
				broken = 1
				obj_count += 1
				obj33_brok = False


	if 122>=boll_y>=120:
		if obj23_brok:
			if  68 >= boll_x and boll_x+15 >= 28 :
				obj23_x = 550
				obj23_y = 100
				broken = -1
				obj_count += 1
				obj23_brok = False
		if obj24_brok:
			if 110 >= boll_x and boll_x+15 >= 70 :
				obj24_x = 550
				obj24_y = 100
				broken = -1
				obj_count += 1
				obj24_brok = False
		if obj25_brok:
			if 152 >= boll_x and boll_x+15 >= 112 :
				obj25_x = 550
				obj25_y = 100
				broken = -1
				obj_count += 1
				obj25_brok = False
		if obj26_brok:
			if 194 >= boll_x and boll_x+15 >= 154 :
				obj26_x = 550
				obj26_y = 100
				broken = -1
				obj_count += 1
				obj26_brok = False
		if obj27_brok:
			if 236 >= boll_x and boll_x+15 >= 196 :
				obj27_x = 550
				obj27_y = 100
				broken = -1
				obj_count += 1
				obj27_brok = False
		if obj28_brok:
			if 278 >= boll_x and boll_x+15 >= 238 :
				obj28_x = 550
				obj28_y = 100
				broken = -1
				obj_count += 1
				obj28_brok = False
		if obj28_brok:
			if 320 >= boll_x and boll_x+15 >= 280:
				obj28_x = 550
				obj28_y = 100
				broken = -1
				obj_count += 1
				obj28_brok = False
		if obj30_brok:
			if 362 >= boll_x and boll_x+15 >= 322 :
				obj30_x = 550
				obj30_y = 100
				broken = -1
				obj_count += 1
				obj30_brok = False
		if obj31_brok:
			if 404 >= boll_x and boll_x+15 >= 364 :
				obj31_x = 550
				obj31_y = 100
				broken = -1
				obj_count += 1
				obj31_brok = False
		if obj32_brok:
			if 446 >= boll_x and boll_x+15 >= 406 :
				obj32_x = 550
				obj32_y = 100
				broken = -1
				obj_count += 1
				obj32_brok = False
		if obj33_brok:
			if 488 >= boll_x and boll_x+15 >= 448 :
				obj33_x = 550
				obj33_y = 100
				broken = -1
				obj_count += 1
				obj33_brok = False

#Второй ряд
	if 119>=boll_y>=117:
		if obj12_brok:
			if  68 >= boll_x and boll_x+15 >= 28 :
				obj12_x = 550
				obj12_y = 100
				broken = 1
				obj_count += 1
				obj12_brok = False
		if obj13_brok:
			if 110 >= boll_x and boll_x+15 >= 70 :
				obj13_x = 550
				obj13_y = 100
				broken = 1
				obj_count += 1
				obj13_brok = False
		if obj14_brok:
			if 152 >= boll_x and boll_x+15 >= 112 :
				obj14_x = 550
				obj14_y = 100
				broken = 1
				obj_count += 1
				obj14_brok = False
		if obj15_brok:
			if 194 >= boll_x and boll_x+15 >= 154 :
				obj15_x = 550
				obj15_y = 100
				broken = 1
				obj_count += 1
				obj15_brok = False
		if obj16_brok:
			if 236 >= boll_x and boll_x+15 >= 196 :
				obj16_x = 550
				obj16_y = 100
				broken = 1
				obj_count += 1
				obj16_brok = False
		if obj17_brok:
			if 278 >= boll_x and boll_x+15 >= 238 :
				obj17_x = 550
				obj17_y = 100
				broken = 1
				obj_count += 1
				obj17_brok = False
		if obj18_brok:
			if 320 >= boll_x and boll_x+15 >= 280:
				obj18_x = 550
				obj18_y = 100
				broken = 1
				obj_count += 1
				obj18_brok = False
		if obj19_brok:
			if 362 >= boll_x and boll_x+15 >= 322 :
				obj19_x = 550
				obj19_y = 100
				broken = 1
				obj_count += 1
				obj19_brok = False
		if obj20_brok:
			if 404 >= boll_x and boll_x+15 >= 364 :
				obj20_x = 550
				obj20_y = 100
				broken = 1
				obj_count += 1
				obj20_brok = False
		if obj21_brok:
			if 446 >= boll_x and boll_x+15 >= 406 :
				obj21_x = 550
				obj21_y = 100
				broken = 1
				obj_count += 1
				obj21_brok = False
		if obj22_brok:
			if 488 >= boll_x and boll_x+15 >= 448 :
				obj22_x = 550
				obj22_y = 100
				broken = 1
				obj_count += 1
				obj22_brok = False


	if 104>=boll_y>=102:
		if obj12_brok:
			if  68 >= boll_x and boll_x+15 >= 28 :
				obj12_x = 550
				obj12_y = 100
				broken = -1
				obj_count += 1
				obj12_brok = False
		if obj13_brok:
			if 110 >= boll_x and boll_x+15 >= 70 :
				obj13_x = 550
				obj13_y = 100
				broken = -1
				obj_count += 1
				obj13_brok = False
		if obj14_brok:
			if 152 >= boll_x and boll_x+15 >= 112 :
				obj14_x = 550
				obj14_y = 100
				broken = -1
				obj_count += 1
				obj14_brok = False
		if obj15_brok:
			if 194 >= boll_x and boll_x+15 >= 154 :
				obj15_x = 550
				obj15_y = 100
				broken = -1
				obj_count += 1
				obj15_brok = False
		if obj16_brok:
			if 236 >= boll_x and boll_x+15 >= 196 :
				obj16_x = 550
				obj16_y = 100
				broken = -1
				obj_count += 1
				obj16_brok = False
		if obj17_brok:
			if 278 >= boll_x and boll_x+15 >= 238 :
				obj17_x = 550
				obj17_y = 100
				broken = -1
				obj_count += 1
				obj17_brok = False
		if obj18_brok:
			if 381 >= boll_x and boll_x+15 >= 241:
				obj18_x = 550
				obj18_y = 100
				broken = -1
				obj_count += 1
				obj18_brok = False
		if obj19_brok:
			if 362 >= boll_x and boll_x+15 >= 322 :
				obj19_x = 550
				obj19_y = 100
				broken = -1
				obj_count += 1
				obj19_brok = False
		if obj20_brok:
			if 404 >= boll_x and boll_x+15 >= 364 :
				obj20_x = 550
				obj20_y = 100
				broken = -1
				obj_count += 1
				obj20_brok = False
		if obj21_brok:
			if 446 >= boll_x and boll_x+15 >= 406 :
				obj21_x = 550
				obj21_y = 100
				broken = -1
				obj_count += 1
				obj21_brok = False
		if obj22_brok:
			if 488 >= boll_x and boll_x+15 >= 448 :
				obj22_x = 550
				obj22_y = 100
				broken = -1
				obj_count += 1
				obj22_brok = False

#Первый ряд
	if 101>=boll_y>=99:
		if obj1_brok:
			if  68 >= boll_x and boll_x+15 >= 28 :
				obj1_x = 550
				obj1_y = 100
				broken = 1
				obj_count += 1
				obj1_brok = False
		if obj2_brok:
			if 110 >= boll_x and boll_x+15 >= 70 :
				obj2_x = 550
				obj2_y = 100
				broken = 1
				obj_count += 1
				obj2_brok = False
		if obj3_brok:
			if 152 >= boll_x and boll_x+15 >= 112 :
				obj3_x = 550
				obj3_y = 100
				broken = 1
				obj_count += 1
				obj3_brok = False
		if obj4_brok:
			if 194 >= boll_x and boll_x+15 >= 154 :
				obj4_x = 550
				obj4_y = 100
				broken = 1
				obj_count += 1
				obj4_brok = False
		if obj5_brok:
			if 236 >= boll_x and boll_x+15 >= 196 :
				obj5_x = 550
				obj5_y = 100
				broken = 1
				obj_count += 1
				obj5_brok = False
		if obj6_brok:
			if 278 >= boll_x and boll_x+15 >= 238 :
				obj6_x = 550
				obj6_y = 100
				broken = 1
				obj_count += 1
				obj6_brok = False
		if obj7_brok:
			if 320 >= boll_x and boll_x+15 >= 280:
				obj7_x = 550
				obj7_y = 100
				broken = 1
				obj_count += 1
				obj7_brok = False
		if obj8_brok:
			if 362 >= boll_x and boll_x+15 >= 322 :
				obj8_x = 550
				obj8_y = 100
				broken = 1
				obj_count += 1
				obj8_brok = False
		if obj9_brok:
			if 404 >= boll_x and boll_x+15 >= 364 :
				obj9_x = 550
				obj9_y = 100
				broken = 1
				obj_count += 1
				obj9_brok = False
		if obj10_brok:
			if 446 >= boll_x and boll_x+15 >= 406 :
				obj10_x = 550
				obj10_y = 100
				broken = 1
				obj_count += 1
				obj10_brok = False
		if obj11_brok:
			if 488 >= boll_x and boll_x+15 >= 448 :
				obj11_x = 550
				obj11_y = 100
				broken = 1
				obj_count += 1
				obj11_brok = False



# Отскок мяча по координате Х

#Четвертый ряд
	if boll_y<=156 and boll_y+15>=139:
		if obj34_brok:
			if boll_x == 69:
				broken_x = 1
				obj_count += 1
				obj34_x = 550
				obj34_y = 100
				obj34_brok = False
		if obj35_brok:
			if boll_x == 111:
				obj35_x = 550
				obj35_y = 100
				broken_x = 1
				obj_count += 1
				obj35_brok = False
			if boll_x + 15 == 71:
				obj35_x = 550
				obj35_y = 100
				broken_x = -1
				obj_count += 1
				obj35_brok = False
		if obj36_brok:
			if boll_x == 153:
				obj36_x = 550
				obj36_y = 100
				broken_x = 1
				obj_count += 1
				obj36_brok = False
			if boll_x + 15 == 113:
				obj36_x = 550
				obj36_y = 100
				broken_x = -1
				obj_count += 1
				obj36_brok = False
		if obj37_brok:
			if boll_x == 195:
				obj37_x = 550
				obj37_y = 100
				broken_x = 1
				obj_count += 1
				obj37_brok = False
			if boll_x + 15 == 155:
				obj37_x = 550
				obj37_y = 100
				broken_x = -1
				obj_count += 1
				obj37_brok = False
		if obj38_brok:
			if boll_x == 237:
				obj38_x = 550
				obj38_y = 100
				broken_x = 1
				obj_count += 1
				obj38_brok = False
			if boll_x + 15 == 197:
				obj38_x = 550
				obj38_y = 100
				broken_x = -1
				obj_count += 1
				obj38_brok = False
		if obj39_brok:
			if boll_x == 279:
				obj39_x = 550
				obj39_y = 100
				broken_x = 1
				obj_count += 1
				obj39_brok = False
			if boll_x + 15 == 239:
				obj39_x = 550
				obj39_y = 100
				broken_x = -1
				obj_count += 1
				obj39_brok = False
		if obj40_brok:
			if boll_x == 321:
				obj40_x = 550
				obj40_y = 100
				broken_x = 1
				obj_count += 1
				obj40_brok = False
			if boll_x + 15 == 281:
				obj40_x = 550
				obj40_y = 100
				broken_x = -1
				obj_count += 1
				obj40_brok = False
		if obj41_brok:
			if boll_x == 363:
				obj41_x = 550
				obj41_y = 100
				broken_x = 1
				obj_count += 1
				obj41_brok = False
			if boll_x + 15 == 323:
				obj41_x = 550
				obj41_y = 100
				broken_x = -1
				obj_count += 1
				obj41_brok = False
		if obj42_brok:
			if boll_x == 405:
				obj42_x = 550
				obj42_y = 100
				broken_x = 1
				obj_count += 1
				obj42_brok = False
			if boll_x + 15 == 365:
				obj42_x = 550
				obj42_y = 100
				broken_x = -1
				obj_count += 1
				obj42_brok = False
		if obj43_brok:
			if boll_x == 447:
				obj43_x = 550
				obj43_y = 100
				broken_x = 1
				obj_count += 1
				obj43_brok = False
			if boll_x + 15 == 407:
				obj43_x = 550
				obj43_y = 100
				broken_x = -1
				obj_count += 1
				obj43_brok = False
		if obj44_brok:
			if boll_x == 489:
				obj44_x = 550
				obj44_y = 100
				broken_x = 1
				obj_count += 1
				obj44_brok = False
			if boll_x + 15 == 449:
				obj44_x = 550
				obj44_y = 100
				broken_x = -1
				obj_count += 1
				obj44_brok = False

#Третий ряд
	if boll_y<=138 and boll_y+15>=121:
			if obj23_brok:
				if boll_x == 69:
					broken_x = 1
					obj_count += 1
					obj23_x = 550
					obj23_y = 100
					obj23_brok = False
			if obj24_brok:
				if boll_x == 111:
					obj24_x = 550
					obj24_y = 100
					broken_x = 1
					obj_count += 1
					obj24_brok = False
				if boll_x + 15 == 71:
					obj24_x = 550
					obj24_y = 100
					broken_x = -1
					obj_count += 1
					obj24_brok = False
			if obj25_brok:
				if boll_x == 153:
					obj25_x = 550
					obj25_y = 100
					broken_x = 1
					obj_count += 1
					obj25_brok = False
				if boll_x + 15 == 113:
					obj25_x = 550
					obj25_y = 100
					broken_x = -1
					obj_count += 1
					obj25_brok = False
			if obj26_brok:
				if boll_x == 195:
					obj26_x = 550
					obj26_y = 100
					broken_x = 1
					obj_count += 1
					obj26_brok = False
				if boll_x + 15 == 155:
					obj26_x = 550
					obj26_y = 100
					broken_x = -1
					obj_count += 1
					obj26_brok = False
			if obj27_brok:
				if boll_x == 237:
					obj27_x = 550
					obj27_y = 100
					broken_x = 1
					obj_count += 1
					obj27_brok = False
				if boll_x + 15 == 197:
					obj27_x = 550
					obj27_y = 100
					broken_x = -1
					obj_count += 1
					obj27_brok = False
			if obj28_brok:
				if boll_x == 279:
					obj28_x = 550
					obj28_y = 100
					broken_x = 1
					obj_count += 1
					obj28_brok = False
				if boll_x + 15 == 239:
					obj28_x = 550
					obj28_y = 100
					broken_x = -1
					obj_count += 1
					obj28_brok = False
			if obj29_brok:
				if boll_x == 321:
					obj29_x = 550
					obj29_y = 100
					broken_x = 1
					obj_count += 1
					obj29_brok = False
				if boll_x + 15 == 281:
					obj29_x = 550
					obj29_y = 100
					broken_x = -1
					obj_count += 1
					obj29_brok = False
			if obj30_brok:
				if boll_x == 363:
					obj30_x = 550
					obj30_y = 100
					broken_x = 1
					obj_count += 1
					obj30_brok = False
				if boll_x + 15 == 323:
					obj30_x = 550
					obj30_y = 100
					broken_x = -1
					obj_count += 1
					obj30_brok = False
			if obj31_brok:
				if boll_x == 405:
					obj31_x = 550
					obj31_y = 100
					broken_x = 1
					obj_count += 1
					obj31_brok = False
				if boll_x + 15 == 365:
					obj31_x = 550
					obj31_y = 100
					broken_x = -1
					obj_count += 1
					obj31_brok = False
			if obj32_brok:
				if boll_x == 447:
					obj32_x = 550
					obj32_y = 100
					broken_x = 1
					obj_count += 1
					obj32_brok = False
				if boll_x + 15 == 407:
					obj32_x = 550
					obj32_y = 100
					broken_x = -1
					obj_count += 1
					obj32_brok = False
			if obj33_brok:
				if boll_x == 489:
					obj33_x = 550
					obj33_y = 100
					broken_x = 1
					obj_count += 1
					obj33_brok = False
				if boll_x + 15 == 449:
					obj33_x = 550
					obj33_y = 100
					broken_x = -1
					obj_count += 1
					obj33_brok = False

#Второй ряд
	if boll_y<=120 and boll_y+15>=103:
			if obj12_brok:
				if boll_x == 69:
					broken_x = 1
					obj_count += 1
					obj12_x = 550
					obj12_y = 100
					obj12_brok = False
			if obj13_brok:
				if boll_x == 111:
					obj13_x = 550
					obj13_y = 100
					broken_x = 1
					obj_count += 1
					obj13_brok = False
				if boll_x + 15 == 71:
					obj13_x = 550
					obj13_y = 100
					broken_x = -1
					obj_count += 1
					obj13_brok = False
			if obj14_brok:
				if boll_x == 153:
					obj14_x = 550
					obj14_y = 100
					broken_x = 1
					obj_count += 1
					obj14_brok = False
				if boll_x + 15 == 113:
					obj14_x = 550
					obj14_y = 100
					broken_x = -1
					obj_count += 1
					obj14_brok = False
			if obj15_brok:
				if boll_x == 195:
					obj15_x = 550
					obj15_y = 100
					broken_x = 1
					obj_count += 1
					obj15_brok = False
				if boll_x + 15 == 155:
					obj15_x = 550
					obj15_y = 100
					broken_x = -1
					obj_count += 1
					obj15_brok = False
			if obj16_brok:
				if boll_x == 237:
					obj16_x = 550
					obj16_y = 100
					broken_x = 1
					obj_count += 1
					obj16_brok = False
				if boll_x + 15 == 197:
					obj16_x = 550
					obj16_y = 100
					broken_x = -1
					obj_count += 1
					obj16_brok = False
			if obj17_brok:
				if boll_x == 279:
					obj17_x = 550
					obj17_y = 100
					broken_x = 1
					obj_count += 1
					obj17_brok = False
				if boll_x + 15 == 239:
					obj17_x = 550
					obj17_y = 100
					broken_x = -1
					obj_count += 1
					obj17_brok = False
			if obj18_brok:
				if boll_x == 321:
					obj18_x = 550
					obj18_y = 100
					broken_x = 1
					obj_count += 1
					obj18_brok = False
				if boll_x + 15 == 281:
					obj18_x = 550
					obj18_y = 100
					broken_x = -1
					obj_count += 1
					obj18_brok = False
			if obj19_brok:
				if boll_x == 363:
					obj19_x = 550
					obj19_y = 100
					broken_x = 1
					obj_count += 1
					obj19_brok = False
				if boll_x + 15 == 323:
					obj19_x = 550
					obj19_y = 100
					broken_x = -1
					obj_count += 1
					obj19_brok = False
			if obj20_brok:
				if boll_x == 405:
					obj20_x = 550
					obj20_y = 100
					broken_x = 1
					obj_count += 1
					obj20_brok = False
				if boll_x + 15 == 365:
					obj20_x = 550
					obj20_y = 100
					broken_x = -1
					obj_count += 1
					obj20_brok = False
			if obj21_brok:
				if boll_x == 447:
					obj21_x = 550
					obj21_y = 100
					broken_x = 1
					obj_count += 1
					obj21_brok = False
				if boll_x + 15 == 407:
					obj21_x = 550
					obj21_y = 100
					broken_x = -1
					obj_count += 1
					obj21_brok = False
			if obj22_brok:
				if boll_x == 489:
					obj22_x = 550
					obj22_y = 100
					broken_x = 1
					obj_count += 1
					obj22_brok = False
				if boll_x + 15 == 449:
					obj22_x = 550
					obj22_y = 100
					broken_x = -1
					obj_count += 1
					obj22_brok = False

#Первый ряд
	if boll_y<=102 and boll_y+15>=85:
			if obj1_brok:
				if boll_x == 69:
					broken_x = 1
					obj_count += 1
					obj1_x = 550
					obj1_y = 100
					obj1_brok = False
			if obj2_brok:
				if boll_x == 111:
					obj2_x = 550
					obj2_y = 100
					broken_x = 1
					obj_count += 1
					obj2_brok = False
				if boll_x + 15 == 71:
					obj2_x = 550
					obj2_y = 100
					broken_x = -1
					obj_count += 1
					obj2_brok = False
			if obj3_brok:
				if boll_x == 153:
					obj3_x = 550
					obj3_y = 100
					broken_x = 1
					obj_count += 1
					obj3_brok = False
				if boll_x + 15 == 113:
					obj3_x = 550
					obj3_y = 100
					broken_x = -1
					obj_count += 1
					obj3_brok = False
			if obj4_brok:
				if boll_x == 195:
					obj4_x = 550
					obj4_y = 100
					broken_x = 1
					obj_count += 1
					obj4_brok = False
				if boll_x + 15 == 155:
					obj4_x = 550
					obj4_y = 100
					broken_x = -1
					obj_count += 1
					obj4_brok = False
			if obj5_brok:
				if boll_x == 237:
					obj5_x = 550
					obj5_y = 100
					broken_x = 1
					obj_count += 1
					obj5_brok = False
				if boll_x + 15 == 197:
					obj5_x = 550
					obj5_y = 100
					broken_x = -1
					obj_count += 1
					obj5_brok = False
			if obj6_brok:
				if boll_x == 279:
					obj6_x = 550
					obj6_y = 100
					broken_x = 1
					obj_count += 1
					obj6_brok = False
				if boll_x + 15 == 239:
					obj6_x = 550
					obj6_y = 100
					broken_x = -1
					obj_count += 1
					obj6_brok = False
			if obj7_brok:
				if boll_x == 321:
					obj7_x = 550
					obj7_y = 100
					broken_x = 1
					obj_count += 1
					obj7_brok = False
				if boll_x + 15 == 281:
					obj7_x = 550
					obj7_y = 100
					broken_x = -1
					obj_count += 1
					obj7_brok = False
			if obj8_brok:
				if boll_x == 363:
					obj8_x = 550
					obj8_y = 100
					broken_x = 1
					obj_count += 1
					obj8_brok = False
				if boll_x + 15 == 323:
					obj8_x = 550
					obj8_y = 100
					broken_x = -1
					obj_count += 1
					obj8_brok = False
			if obj9_brok:
				if boll_x == 405:
					obj9_x = 550
					obj9_y = 100
					broken_x = 1
					obj_count += 1
					obj9_brok = False
				if boll_x + 15 == 365:
					obj9_x = 550
					obj9_y = 100
					broken_x = -1
					obj_count += 1
					obj9_brok = False
			if obj10_brok:
				if boll_x == 447:
					obj10_x = 550
					obj10_y = 100
					broken_x = 1
					obj_count += 1
					obj10_brok = False
				if boll_x + 15 == 407:
					obj10_x = 550
					obj10_y = 100
					broken_x = -1
					obj_count += 1
					obj10_brok = False
			if obj11_brok:
				if boll_x == 489:
					obj11_x = 550
					obj11_y = 100
					broken_x = 1
					obj_count += 1
					obj11_brok = False
				if boll_x + 15 == 449:
					obj11_x = 550
					obj11_y = 100
					broken_x = -1
					obj_count += 1
					obj11_brok = False

