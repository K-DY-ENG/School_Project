import pygame
pygame.init()
pygame.mixer.init()

display_width = 650
display_height = 650

display = pygame.display.set_mode((display_width, display_height))

Obj_green = pygame.image.load('images\\Object_skins\\Obj_green.png')
Obj_blue = pygame.image.load('images\\Object_skins\\Obj_blue.png')
Obj_purple = pygame.image.load('images\\Object_skins\\Obj_purple.png')
Obj_red = pygame.image.load('images\\Object_skins\\Obj_red.png')
Obj_yellow = pygame.image.load('images\\Object_skins\\Obj_yellow.png')
Obj_white = pygame.image.load('images\\Object_skins\\Obj_white.png')

point = pygame.mixer.Sound("Sounds\\point.wav")


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
score_count = 0
obj_main_x = 540
obj_main_y = 300

score = 0
text_score = '00000000'

def play_score():
	global score, score_count, text_score
	if obj_count != score_count:
		score += 50
		score_count += 1
		a = len(str(score))
		text_score = '0'*(8-a) + str(score)

obj_brok = [1 for i in range(44)]
coords_x = [29, 71, 113, 155, 197, 239, 281, 323, 365, 407, 449] * 4
coords_y = [86 for i in range (11)]+[104 for i in range(11)]+[122 for i in range(11)]+[140 for i in range(11)]
colors = [obj_red, obj_blue, obj_yellow, obj_green, obj_purple] * 10

def objects_skin():
	for i in range(44):
		display.blit(colors[i], (coords_x[i], coords_y[i], OBJ_WIDHT, OBJ_HEIGT))
	display.blit(obj_white, (obj_main_x, obj_main_y, OBJ_WIDHT, OBJ_HEIGT))
	print_obj_count(('X' + str(44-obj_count)),586, 292)


def print_obj_count(messege, x, y, font_color = (WHITE), font_type = 'Fonts\\GameFont.ttf', font_size = 30):
	font_type = pygame.font.Font(font_type, font_size)
	text = font_type.render(messege, True, font_color)
	display.blit(text, (x, y))



def restart():
	global broken, broken_x, obj_count, score_count, score, coords_y, coords_x, colors, obj_brok

	broken = 0
	broken_x = 0
	obj_count = 0
	score_count = 0
	score = 0
	obj_brok = [1 for i in range(44)]
	coords_x = [29, 71, 113, 155, 197, 239, 281, 323, 365, 407, 449] * 4
	coords_y = [86 for i in range (11)]+[104 for i in range(11)]+[122 for i in range(11)]+[140 for i in range(11)]
	colors = [obj_red, obj_blue, obj_yellow, obj_green, obj_purple] * 10



def check_obj_brocken(boll_x, boll_y):
	global broken, broken_x, obj_count, score_count, score, coords_y, coords_x, colors, obj_brok


# Отскок мяча по координате У

#Четвертый ряд
	if 154>=boll_y>=152:
		if obj_brok[33]:
			if  68>= boll_x+7 and boll_x+8>=28 :
				point.play()
				coords_x[33] = obj_main_x
				coords_y[33] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[33] = False
		if obj_brok[34]:
			if 110>= boll_x+7 and boll_x+8>=70 :
				point.play()
				coords_x[34] = obj_main_x
				coords_y[34] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[34] = False
		if obj_brok[35]:
			if 152>= boll_x+7 and boll_x+8>=112 :
				point.play()
				coords_x[35] = obj_main_x
				coords_y[35] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[35] = False
		if obj_brok[36]:
			if 194>= boll_x+7 and boll_x+8>=154 :
				point.play()
				coords_x[36] = obj_main_x
				coords_y[36] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[36] = False
		if obj_brok[37]:
			if 236>= boll_x+7 and boll_x+8>=196 :
				point.play()
				coords_x[37] = obj_main_x
				coords_y[37] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[37] = False
		if obj_brok[38]:
			if 278>= boll_x+7 and boll_x+8>=238 :
				point.play()
				coords_x[38] = obj_main_x
				coords_y[38] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[38] = False
		if obj_brok[39]:
			if 320>= boll_x+7 and boll_x+8>=280:
				point.play()
				coords_x[39] = obj_main_x
				coords_y[39] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[39] = False
		if obj_brok[40]:
			if 362>= boll_x+7 and boll_x+8>=322 :
				point.play()
				coords_x[40] = obj_main_x
				coords_y[40] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[40] = False
		if obj_brok[41]:
			if 404>= boll_x+7 and boll_x+8>=364 :
				point.play()
				coords_x[41] = obj_main_x
				coords_y[41] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[41] = False
		if obj_brok[42]:
			if 446>= boll_x+7 and boll_x+8>=406 :
				point.play()
				coords_x[42] = obj_main_x
				coords_y[42] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[42] = False
		if obj_brok[43]:
			if 488>= boll_x+7 and boll_x+8>=448 :
				point.play()
				coords_x[43] = obj_main_x
				coords_y[43] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[43] = False
		
	
	if 140>=boll_y>=138:
		if obj_brok[33]:
			if  68>= boll_x+7 and boll_x+8>=28 :
				point.play()
				coords_x[33] = obj_main_x
				coords_y[33] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[33] = False
		if obj_brok[34]:
			if 110>= boll_x+7 and boll_x+8>=70 :
				point.play()
				coords_x[34] = obj_main_x
				coords_y[34] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[34] = False
		if obj_brok[35]:
			if 152>= boll_x+7 and boll_x+8>=112 :
				point.play()
				coords_x[35] = obj_main_x
				coords_y[35] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[35] = False
		if obj_brok[36]:
			if 194>= boll_x+7 and boll_x+8>=154 :
				point.play()
				coords_x[36] = obj_main_x
				coords_y[36] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[36] = False
		if obj_brok[37]:
			if 236>= boll_x+7 and boll_x+8>=196 :
				point.play()
				coords_x[37] = obj_main_x
				coords_y[37] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[37] = False
		if obj_brok[38]:
			if 278>= boll_x+7 and boll_x+8>=238 :
				point.play()
				coords_x[38] = obj_main_x
				coords_y[38] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[38] = False
		if obj_brok[39]:
			if 320>= boll_x+7 and boll_x+8>=280:
				point.play()
				coords_x[39] = obj_main_x
				coords_y[39] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[39] = False
		if obj_brok[40]:
			if 362>= boll_x+7 and boll_x+8>=322 :
				point.play()
				coords_x[40] = obj_main_x
				coords_y[40] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[40] = False
		if obj_brok[41]:
			if 404>= boll_x+7 and boll_x+8>=364 :
				point.play()
				coords_x[41] = obj_main_x
				coords_y[41] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[41] = False
		if obj_brok[42]:
			if 446>= boll_x+7 and boll_x+8>=406 :
				point.play()
				coords_x[42] = obj_main_x
				coords_y[42] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[42] = False
		if obj_brok[43]:
			if 488>= boll_x+7 and boll_x+8>=448 :
				point.play()
				coords_x[43] = obj_main_x
				coords_y[43] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[43] = False

#Третий ряд
	if 137>=boll_y>=135:
		if obj_brok[22]:
			if  68>= boll_x+7 and boll_x+8>=28 :
				point.play()
				coords_x[22] = obj_main_x
				coords_y[22] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[22] = False
		if obj_brok[23]:
			if 110>= boll_x+7 and boll_x+8>=70 :
				point.play()
				coords_x[23] = obj_main_x
				coords_y[23] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[23] = False
		if obj_brok[24]:
			if 152>= boll_x+7 and boll_x+8>=112 :
				point.play()
				coords_x[24] = obj_main_x
				coords_y[24] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[24] = False
		if obj_brok[25]:
			if 194>= boll_x+7 and boll_x+8>=154 :
				point.play()
				coords_x[25] = obj_main_x
				coords_y[25] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[25] = False
		if obj_brok[26]:
			if 236>= boll_x+7 and boll_x+8>=196 :
				point.play()
				coords_x[26] = obj_main_x
				coords_y[26] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[26] = False
		if obj_brok[27]:
			if 278>= boll_x+7 and boll_x+8>=238 :
				point.play()
				coords_x[27] = obj_main_x
				coords_y[27] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[27] = False
		if obj_brok[28]:
			if 320>= boll_x+7 and boll_x+8>=280:
				point.play()
				coords_x[28] = obj_main_x
				coords_y[28] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[28] = False
		if obj_brok[29]:
			if 362>= boll_x+7 and boll_x+8>=322 :
				point.play()
				coords_x[29] = obj_main_x
				coords_y[29] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[29] = False
		if obj_brok[30]:
			if 404>= boll_x+7 and boll_x+8>=364 :
				point.play()
				coords_x[30] = obj_main_x
				coords_y[30] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[30] = False
		if obj_brok[31]:
			if 446>= boll_x+7 and boll_x+8>=406 :
				point.play()
				coords_x[31] = obj_main_x
				coords_y[31] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[31] = False
		if obj_brok[32]:
			if 488>= boll_x+7 and boll_x+8>=448 :
				point.play()
				coords_x[32] = obj_main_x
				coords_y[32] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[32] = False


	if 122>=boll_y>=120:
		if obj_brok[22]:
			if  68>= boll_x+7 and boll_x+8>=28 :
				point.play()
				coords_x[22] = obj_main_x
				coords_y[22] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[22] = False
		if obj_brok[23]:
			if 110>= boll_x+7 and boll_x+8>=70 :
				point.play()
				coords_x[23] = obj_main_x
				coords_y[23] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[23] = False
		if obj_brok[24]:
			if 152>= boll_x+7 and boll_x+8>=112 :
				point.play()
				coords_x[24] = obj_main_x
				coords_y[24] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[24] = False
		if obj_brok[25]:
			if 194>= boll_x+7 and boll_x+8>=154 :
				point.play()
				coords_x[25] = obj_main_x
				coords_y[25] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[25] = False
		if obj_brok[26]:
			if 236>= boll_x+7 and boll_x+8>=196 :
				point.play()
				coords_x[26] = obj_main_x
				coords_y[26] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[26] = False
		if obj_brok[27]:
			if 278>= boll_x+7 and boll_x+8>=238 :
				point.play()
				coords_x[27] = obj_main_x
				coords_y[27] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[27] = False
		if obj_brok[28]:
			if 320>= boll_x+7 and boll_x+8>=280:
				point.play()
				coords_x[28] = obj_main_x
				coords_y[28] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[28] = False
		if obj_brok[29]:
			if 362>= boll_x+7 and boll_x+8>=322 :
				point.play()
				coords_x[29] = obj_main_x
				coords_y[29] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[29] = False
		if obj_brok[30]:
			if 404>= boll_x+7 and boll_x+8>=364 :
				point.play()
				coords_x[30] = obj_main_x
				coords_y[30] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[30] = False
		if obj_brok[31]:
			if 446>= boll_x+7 and boll_x+8>=406 :
				point.play()
				coords_x[31] = obj_main_x
				coords_y[31] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[31] = False
		if obj_brok[32]:
			if 488>= boll_x+7 and boll_x+8>=448 :
				point.play()
				coords_x[32] = obj_main_x
				coords_y[32] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[32] = False

#Второй ряд
	if 119>=boll_y>=117:
		if obj_brok[11]:
			if  68>= boll_x+7 and boll_x+8>=28 :
				point.play()
				coords_x[11] = obj_main_x
				coords_y[11] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[11] = False
		if obj_brok[12]:
			if 110>= boll_x+7 and boll_x+8>=70 :
				point.play()
				coords_x[12] = obj_main_x
				coords_y[12] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[12] = False
		if obj_brok[13]:
			if 152>= boll_x+7 and boll_x+8>=112 :
				point.play()
				coords_x[13] = obj_main_x
				coords_y[13] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[13] = False
		if obj_brok[14]:
			if 194>= boll_x+7 and boll_x+8>=154 :
				point.play()
				coords_x[14] = obj_main_x
				coords_y[14] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[14] = False
		if obj_brok[15]:
			if 236>= boll_x+7 and boll_x+8>=196 :
				point.play()
				coords_x[15] = obj_main_x
				coords_y[15] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[15] = False
		if obj_brok[16]:
			if 278>= boll_x+7 and boll_x+8>=238 :
				point.play()
				coords_x[16] = obj_main_x
				coords_y[16] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[16] = False
		if obj_brok[17]:
			if 320>= boll_x+7 and boll_x+8>=280:
				point.play()
				coords_x[17] = obj_main_x
				coords_y[17] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[17] = False
		if obj_brok[18]:
			if 362>= boll_x+7 and boll_x+8>=322 :
				point.play()
				coords_x[18] = obj_main_x
				coords_y[18] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[18] = False
		if obj_brok[19]:
			if 404>= boll_x+7 and boll_x+8>=364 :
				point.play()
				coords_x[19] = obj_main_x
				coords_y[19] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[19] = False
		if obj_brok[20]:
			if 446>= boll_x+7 and boll_x+8>=406 :
				point.play()
				coords_x[20] = obj_main_x
				coords_y[20] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[20] = False
		if obj_brok[21]:
			if 488>= boll_x+7 and boll_x+8>=448 :
				point.play()
				coords_x[21] = obj_main_x
				coords_y[21] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[21] = False


	if 104>=boll_y>=102:
		if obj_brok[11]:
			if  68>= boll_x+7 and boll_x+8>=28 :
				point.play()
				coords_x[11] = obj_main_x
				coords_y[11] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[11] = False
		if obj_brok[12]:
			if 110>= boll_x+7 and boll_x+8>=70 :
				point.play()
				coords_x[12] = obj_main_x
				coords_y[12] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[12] = False
		if obj_brok[13]:
			if 152>= boll_x+7 and boll_x+8>=112 :
				point.play()
				coords_x[13] = obj_main_x
				coords_y[13] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[13] = False
		if obj_brok[14]:
			if 194>= boll_x+7 and boll_x+8>=154 :
				point.play()
				coords_x[14] = obj_main_x
				coords_y[14] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[14] = False
		if obj_brok[15]:
			if 236>= boll_x+7 and boll_x+8>=196 :
				point.play()
				coords_x[15] = obj_main_x
				coords_y[15] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[15] = False
		if obj_brok[16]:
			if 278>= boll_x+7 and boll_x+8>=238 :
				point.play()
				coords_x[16] = obj_main_x
				coords_y[16] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[16] = False
		if obj_brok[17]:
			if 281 >= boll_x+7 >= 241:
				point.play()
				coords_x[17] = obj_main_x
				coords_y[17] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[17] = False
		if obj_brok[18]:
			if 362>= boll_x+7 and boll_x+8>=322 :
				point.play()
				coords_x[18] = obj_main_x
				coords_y[18] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[18] = False
		if obj_brok[19]:
			if 404>= boll_x+7 and boll_x+8>=364 :
				point.play()
				coords_x[19] = obj_main_x
				coords_y[19] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[19] = False
		if obj_brok[20]:
			if 446>= boll_x+7 and boll_x+8>=406 :
				point.play()
				coords_x[20] = obj_main_x
				coords_y[20] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[20] = False
		if obj_brok[21]:
			if 488>= boll_x+7 and boll_x+8>=448 :
				point.play()
				coords_x[21] = obj_main_x
				coords_y[21] = obj_main_y
				broken = -1
				obj_count += 1
				obj_brok[21] = False

#Первый ряд
	if 101>=boll_y>=99:
		if obj_brok[0]:
			if  68>= boll_x+7 and boll_x+8>=28 :
				point.play()
				coords_x[0] = obj_main_x
				coords_y[0] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[0] = False
		if obj_brok[1]:
			if 110>= boll_x+7 and boll_x+8>=70 :
				point.play()
				coords_x[1] = obj_main_x
				coords_y[1] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[1] = False
		if obj_brok[2]:
			if 152>= boll_x+7 and boll_x+8>=112 :
				point.play()
				coords_x[2] = obj_main_x
				coords_y[2] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[2] = False
		if obj_brok[3]:
			if 194>= boll_x+7 and boll_x+8>=154 :
				point.play()
				coords_x[3] = obj_main_x
				coords_y[3] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[3] = False
		if obj_brok[4]:
			if 236>= boll_x+7 and boll_x+8>=196 :
				point.play()
				coords_x[4] = obj_main_x
				coords_y[4] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[4] = False
		if obj_brok[5]:
			if 278>= boll_x+7 and boll_x+8>=238 :
				point.play()
				coords_x[5] = obj_main_x
				coords_y[5] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[5] = False
		if obj_brok[6]:
			if 320>= boll_x+7 and boll_x+8>=280:
				point.play()
				coords_x[6] = obj_main_x
				coords_y[6] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[6] = False
		if obj_brok[7]:
			if 362>= boll_x+7 and boll_x+8>=322 :
				point.play()
				coords_x[7] = obj_main_x
				coords_y[7] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[7] = False
		if obj_brok[8]:
			if 404>= boll_x+7 and boll_x+8>=364 :
				point.play()
				coords_x[8] = obj_main_x
				coords_y[8] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[8] = False
		if obj_brok[9]:
			if 446>= boll_x+7 and boll_x+8>=406 :
				point.play()
				coords_x[9] = obj_main_x
				coords_y[9] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[9] = False
		if obj_brok[10]:
			if 488>= boll_x+7 and boll_x+8>=448 :
				point.play()
				coords_x[10] = obj_main_x
				coords_y[10] = obj_main_y
				broken = 1
				obj_count += 1
				obj_brok[10] = False




# Отскок мяча по координате Х

#Четвертый ряд
	if 156>=boll_y and 139<=boll_y+15:
		if obj_brok[33]:
			if 69 >= boll_x >= 67:
				point.play()
				broken_x = 1
				obj_count += 1
				coords_x[33] = obj_main_x
				coords_y[33] = obj_main_y
				obj_brok[33] = False
		if obj_brok[34]:
			if 111 >= boll_x >= 109:
				point.play()
				coords_x[34] = obj_main_x
				coords_y[34] = obj_main_y
				broken_x = 1
				obj_count += 1
				obj_brok[34] = False
			if 73 >= boll_x +15 >= 71:
				point.play()
				coords_x[34] = obj_main_x
				coords_y[34] = obj_main_y
				broken_x = -1
				obj_count += 1
				obj_brok[34] = False
		if obj_brok[35]:
			if 153 >= boll_x >= 151:
				point.play()
				coords_x[35] = obj_main_x
				coords_y[35] = obj_main_y
				broken_x = 1
				obj_count += 1
				obj_brok[35] = False
			if 115 >= boll_x +15 >= 113:
				point.play()
				coords_x[35] = obj_main_x
				coords_y[35] = obj_main_y
				broken_x = -1
				obj_count += 1
				obj_brok[35] = False
		if obj_brok[36]:
			if 195 >= boll_x >= 193:
				point.play()
				coords_x[36] = obj_main_x
				coords_y[36] = obj_main_y
				broken_x = 1
				obj_count += 1
				obj_brok[36] = False
			if 157 >= boll_x +15 >= 155:
				point.play()
				coords_x[36] = obj_main_x
				coords_y[36] = obj_main_y
				broken_x = -1
				obj_count += 1
				obj_brok[36] = False
		if obj_brok[37]:
			if 237>= boll_x >= 235:
				point.play()
				coords_x[37] = obj_main_x
				coords_y[37] = obj_main_y
				broken_x = 1
				obj_count += 1
				obj_brok[37] = False
			if 199 >= boll_x +15 >= 197:
				point.play()
				coords_x[37] = obj_main_x
				coords_y[37] = obj_main_y
				broken_x = -1
				obj_count += 1
				obj_brok[37] = False
		if obj_brok[38]:
			if 279 >= boll_x >= 277:
				point.play()
				coords_x[38] = obj_main_x
				coords_y[38] = obj_main_y
				broken_x = 1
				obj_count += 1
				obj_brok[38] = False
			if 241 >= boll_x +15 >= 239:
				point.play()
				coords_x[38] = obj_main_x
				coords_y[38] = obj_main_y
				broken_x = -1
				obj_count += 1
				obj_brok[38] = False
		if obj_brok[39]:
			if 321 >= boll_x >= 319:
				point.play()
				coords_x[39] = obj_main_x
				coords_y[39] = obj_main_y
				broken_x = 1
				obj_count += 1
				obj_brok[39] = False
			if 283 >= boll_x +15 >= 281:
				point.play()
				coords_x[39] = obj_main_x
				coords_y[39] = obj_main_y
				broken_x = -1
				obj_count += 1
				obj_brok[39] = False
		if obj_brok[40]:
			if 363 >= boll_x >= 361:
				point.play()
				coords_x[40] = obj_main_x
				coords_y[40] = obj_main_y
				broken_x = 1
				obj_count += 1
				obj_brok[40] = False
			if 325 >= boll_x +15 >= 323:
				point.play()
				coords_x[40] = obj_main_x
				coords_y[40] = obj_main_y
				broken_x = -1
				obj_count += 1
				obj_brok[40] = False
		if obj_brok[41]:
			if 405 >= boll_x >= 403:
				point.play()
				coords_x[41] = obj_main_x
				coords_y[41] = obj_main_y
				broken_x = 1
				obj_count += 1
				obj_brok[41] = False
			if boll_x + 15 == 365:
				point.play()
				coords_x[41] = obj_main_x
				coords_y[41] = obj_main_y
				broken_x = -1
				obj_count += 1
				obj_brok[41] = False
		if obj_brok[42]:
			if 447 >= boll_x >= 445:
				point.play()
				coords_x[42] = obj_main_x
				coords_y[42] = obj_main_y
				broken_x = 1
				obj_count += 1
				obj_brok[42] = False
			if 409 >= boll_x +15 >= 407:
				point.play()
				coords_x[42] = obj_main_x
				coords_y[42] = obj_main_y
				broken_x = -1
				obj_count += 1
				obj_brok[42] = False
		if obj_brok[43]:
			if 489 >= boll_x >= 487:
				point.play()
				coords_x[43] = obj_main_x
				coords_y[43] = obj_main_y
				broken_x = 1
				obj_count += 1
				obj_brok[43] = False
			if 451>= boll_x +15 >= 449:
				point.play()
				coords_x[43] = obj_main_x
				coords_y[43] = obj_main_y
				broken_x = -1
				obj_count += 1
				obj_brok[43] = False

#Третий ряд
	if 138>=boll_y and 121<=boll_y+15:
			if obj_brok[22]:
				if 69 >= boll_x >= 67:
					point.play()
					broken_x = 1
					obj_count += 1
					coords_x[22] = obj_main_x
					coords_y[22] = obj_main_y
					obj_brok[22] = False
			if obj_brok[23]:
				if 111 >= boll_x >= 109:
					point.play()
					coords_x[23] = obj_main_x
					coords_y[23] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[23] = False
				if 73 >= boll_x +15 >= 71:
					point.play()
					coords_x[23] = obj_main_x
					coords_y[23] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[23] = False
			if obj_brok[24]:
				if 153 >= boll_x >= 151:
					point.play()
					coords_x[24] = obj_main_x
					coords_y[24] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[24] = False
				if 115 >= boll_x +15 >= 113:
					point.play()
					coords_x[24] = obj_main_x
					coords_y[24] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[24] = False
			if obj_brok[25]:
				if 195 >= boll_x >= 193:
					point.play()
					coords_x[25] = obj_main_x
					coords_y[25] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[25] = False
				if 157 >= boll_x +15 >= 155:
					point.play()
					coords_x[25] = obj_main_x
					coords_y[25] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[25] = False
			if obj_brok[26]:
				if 237>= boll_x >= 235:
					point.play()
					coords_x[26] = obj_main_x
					coords_y[26] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[26] = False
				if 199 >= boll_x +15 >= 197:
					point.play()
					coords_x[26] = obj_main_x
					coords_y[26] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[26] = False
			if obj_brok[27]:
				if 279 >= boll_x >= 277:
					point.play()
					coords_x[27] = obj_main_x
					coords_y[27] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[27] = False
				if 241 >= boll_x +15 >= 239:
					point.play()
					coords_x[27] = obj_main_x
					coords_y[27] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[27] = False
			if obj_brok[28]:
				if 321 >= boll_x >= 319:
					point.play()
					coords_x[28] = obj_main_x
					coords_y[28] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[28] = False
				if 283 >= boll_x +15 >= 281:
					point.play()
					coords_x[28] = obj_main_x
					coords_y[28] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[28] = False
			if obj_brok[29]:
				if 363 >= boll_x >= 361:
					point.play()
					coords_x[29] = obj_main_x
					coords_y[29] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[29] = False
				if 325 >= boll_x +15 >= 323:
					point.play()
					coords_x[29] = obj_main_x
					coords_y[29] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[29] = False
			if obj_brok[30]:
				if 405 >= boll_x >= 403:
					point.play()
					coords_x[30] = obj_main_x
					coords_y[30] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[30] = False
				if boll_x + 15 == 365:
					point.play()
					coords_x[30] = obj_main_x
					coords_y[30] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[30] = False
			if obj_brok[31]:
				if 447 >= boll_x >= 445:
					point.play()
					coords_x[31] = obj_main_x
					coords_y[31] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[31] = False
				if 409 >= boll_x +15 >= 407:
					point.play()
					coords_x[31] = obj_main_x
					coords_y[31] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[31] = False
			if obj_brok[32]:
				if 489 >= boll_x >= 487:
					point.play()
					coords_x[32] = obj_main_x
					coords_y[32] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[32] = False
				if 451>= boll_x +15 >= 449:
					point.play()
					coords_x[32] = obj_main_x
					coords_y[32] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[32] = False

#Второй ряд
	if 120>=boll_y and 103<=boll_y+15:
			if obj_brok[11]:
				if 69 >= boll_x >= 67:
					point.play()
					broken_x = 1
					obj_count += 1
					coords_x[11] = obj_main_x
					coords_y[11] = obj_main_y
					obj_brok[11] = False
			if obj_brok[12]:
				if 111 >= boll_x >= 109:
					point.play()
					coords_x[12] = obj_main_x
					coords_y[12] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[12] = False
				if 73 >= boll_x +15 >= 71:
					point.play()
					coords_x[12] = obj_main_x
					coords_y[12] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[12] = False
			if obj_brok[13]:
				if 153 >= boll_x >= 151:
					point.play()
					coords_x[13] = obj_main_x
					coords_y[13] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[13] = False
				if 115 >= boll_x +15 >= 113:
					point.play()
					coords_x[13] = obj_main_x
					coords_y[13] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[13] = False
			if obj_brok[14]:
				if 195 >= boll_x >= 193:
					point.play()
					coords_x[14] = obj_main_x
					coords_y[14] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[14] = False
				if 157 >= boll_x +15 >= 155:
					point.play()
					coords_x[14] = obj_main_x
					coords_y[14] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[14] = False
			if obj_brok[15]:
				if 237>= boll_x >= 235:
					point.play()
					coords_x[15] = obj_main_x
					coords_y[15] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[15] = False
				if 199 >= boll_x +15 >= 197:
					point.play()
					coords_x[15] = obj_main_x
					coords_y[15] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[15] = False
			if obj_brok[16]:
				if 279 >= boll_x >= 277:
					point.play()
					coords_x[16] = obj_main_x
					coords_y[16] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[16] = False
				if 241 >= boll_x +15 >= 239:
					point.play()
					coords_x[16] = obj_main_x
					coords_y[16] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[16] = False
			if obj_brok[17]:
				if 321 >= boll_x >= 319:
					point.play()
					coords_x[17] = obj_main_x
					coords_y[17] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[17] = False
				if 283 >= boll_x +15 >= 281:
					point.play()
					coords_x[17] = obj_main_x
					coords_y[17] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[17] = False
			if obj_brok[18]:
				if 363 >= boll_x >= 361:
					point.play()
					coords_x[18] = obj_main_x
					coords_y[18] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[18] = False
				if 325 >= boll_x +15 >= 323:
					point.play()
					coords_x[18] = obj_main_x
					coords_y[18] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[18] = False
			if obj_brok[19]:
				if 405 >= boll_x >= 403:
					point.play()
					coords_x[19] = obj_main_x
					coords_y[19] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[19] = False
				if boll_x + 15 == 365:
					point.play()
					coords_x[19] = obj_main_x
					coords_y[19] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[19] = False
			if obj_brok[20]:
				if 447 >= boll_x >= 445:
					point.play()
					coords_x[20] = obj_main_x
					coords_y[20] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[20] = False
				if 409 >= boll_x +15 >= 407:
					point.play()
					coords_x[20] = obj_main_x
					coords_y[20] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[20] = False
			if obj_brok[21]:
				if 489 >= boll_x >= 487:
					point.play()
					coords_x[21] = obj_main_x
					coords_y[21] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[21] = False
				if 451>= boll_x +15 >= 449:
					point.play()
					coords_x[21] = obj_main_x
					coords_y[21] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[21] = False

#Первый ряд
	if 102>=boll_y and 85<=boll_y+15:
			if obj_brok[0]:
				if 69 >= boll_x >= 67:
					point.play()
					broken_x = 1
					obj_count += 1
					coords_x[0] = obj_main_x
					coords_y[0] = obj_main_y
					obj_brok[0] = False
			if obj_brok[1]:
				if 111 >= boll_x >= 109:
					point.play()
					coords_x[1] = obj_main_x
					coords_y[1] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[1] = False
				if 73 >= boll_x +15 >= 71:
					point.play()
					coords_x[1] = obj_main_x
					coords_y[1] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[1] = False
			if obj_brok[2]:
				if 153 >= boll_x >= 151:
					point.play()
					coords_x[2] = obj_main_x
					coords_y[2] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[2] = False
				if 115 >= boll_x +15 >= 113:
					point.play()
					coords_x[2] = obj_main_x
					coords_y[2] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[2] = False
			if obj_brok[3]:
				if 195 >= boll_x >= 193:
					point.play()
					coords_x[3] = obj_main_x
					coords_y[3] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[3] = False
				if 157 >= boll_x +15 >= 155:
					point.play()
					coords_x[3] = obj_main_x
					coords_y[3] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[3] = False
			if obj_brok[4]:
				if 237>= boll_x >= 235:
					point.play()
					coords_x[4] = obj_main_x
					coords_y[4] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[4] = False
				if 199 >= boll_x +15 >= 197:
					point.play()
					coords_x[4] = obj_main_x
					coords_y[4] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[4] = False
			if obj_brok[5]:
				if 279 >= boll_x >= 277:
					point.play()
					coords_x[5] = obj_main_x
					coords_y[5] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[5] = False
				if 241 >= boll_x +15 >= 239:
					point.play()
					coords_x[5] = obj_main_x
					coords_y[5] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[5] = False
			if obj_brok[6]:
				if 321 >= boll_x >= 319:
					point.play()
					coords_x[6] = obj_main_x
					coords_y[6] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[6] = False
				if 283 >= boll_x +15 >= 281:
					point.play()
					coords_x[6] = obj_main_x
					coords_y[6] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[6] = False
			if obj_brok[7]:
				if 363 >= boll_x >= 361:
					point.play()
					coords_x[7] = obj_main_x
					coords_y[7] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[7] = False
				if 325 >= boll_x +15 >= 323:
					point.play()
					coords_x[7] = obj_main_x
					coords_y[7] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[7] = False
			if obj_brok[8]:
				if 405 >= boll_x >= 403:
					point.play()
					coords_x[8] = obj_main_x
					coords_y[8] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[8] = False
				if boll_x + 15 == 365:
					point.play()
					coords_x[8] = obj_main_x
					coords_y[8] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[8] = False
			if obj_brok[9]:
				if 447 >= boll_x >= 445:
					point.play()
					coords_x[9] = obj_main_x
					coords_y[9] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[9] = False
				if 409 >= boll_x +15 >= 407:
					point.play()
					coords_x[9] = obj_main_x
					coords_y[9] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[9] = False
			if obj_brok[10]:
				if 489 >= boll_x >= 487:
					point.play()
					coords_x[10] = obj_main_x
					coords_y[10] = obj_main_y
					broken_x = 1
					obj_count += 1
					obj_brok[10] = False
				if 451>= boll_x +15 >= 449:
					point.play()
					coords_x[10] = obj_main_x
					coords_y[10] = obj_main_y
					broken_x = -1
					obj_count += 1
					obj_brok[10] = False
