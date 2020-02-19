import pygame
import random
import Level_1
import Change_skin

pygame.init()
pygame.mixer.init()

display_width = 650
display_height = 650

BLUE = (19, 31, 247)
YELLOW = (247, 255, 60)
GREEN = (45, 255, 60)
RED = (222, 17, 0)
PURPLE = (217, 0, 167)
WHITE = (255, 255, 255)

display = pygame.display.set_mode((display_width, display_height))


platform_width = 90
platform_height = 15
platform_x = (display_width-105)//2 - 45
platform_y = display_height - 60
lenght_pl = 20
plat_width = 90
plat_len_time = 0
plat_time_start = False

boll_x = (display_width-150)//2 + 10
boll_y = display_height - 350
boll_width = 15
boll_height = 15



boll_step_x = (1, 2, 3)
boll_step_y = (1, 2, 3)
boll_control_x = 0
boll_control_y = 1


boll_moves_x = random.choice(boll_step_x)
boll_moves_y = 2

press_f = True
FPS_time = 100

FPS = pygame.time.Clock()

Fon = pygame.image.load('images\\Fon.png').convert_alpha()
Background = pygame.image.load('images\\background.png').convert_alpha()
Boll_skin = pygame.transform.scale(Change_skin.boll_color(),(boll_width, boll_height))

game_start = True

def game_run():
    global Platform_skin
    game = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Платформа в цикле, т.к ее размер меняется.
        Platform_skin = pygame.transform.scale(Change_skin.platform_color(), (platform_width, platform_height))
        blit_screen()

        if game_start:
            game_run_ENTER()
            blit_screen()
            game_time()
        
        if game:
            global press_f, press_f, plat_len_time, plat_time_start, FPS_time, \
            boll_moves_y, boll_moves_x,boll_control_y

            check_boll_y()
            check_boll_x()
            boll_move_x()
            boll_move_y()
            Level_1.check_obj_brocken(boll_x, boll_y)
            broken_y()
            broken_x()

            key = pygame.key.get_pressed()
            if key[pygame.K_RIGHT]:
                right()

            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                left()

            key = pygame.key.get_pressed()
            if key[pygame.K_f]:
                if press_f:
                    for i in range (20):
                        platform_lenght_plus()
                    plat_time_start = True
                    press_f = False
            key = pygame.key.get_pressed()
            if key[pygame.K_r]:
                FPS_time += 1

            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                pause_game()

            platform_lenght_time()

            if plat_len_time >= 1000:
                for i in range (20):
                    platform_lenght_minus()

                press_f = True
                plat_time_start = False
                plat_len_time = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            game = True


        pygame.display.update()
        FPS.tick(FPS_time)


def blit_screen():
            display.fill((0, 0, 0))
            display.blit(pygame.transform.scale(Background, (505, 600)), (10, 80, 505, 600))
            display.blit(Fon, (0, 0, display_width, display_height))
            display.blit(Boll_skin, (boll_x, boll_y, boll_width, boll_height))
            display.blit(Platform_skin, (platform_x, platform_y, platform_width, platform_height))
            Level_1.objects_skin()
            print_text('Developed for a school project by D.K (vk.com/d.e_mon)', 0, 0)
            print_text('Beta version 1.1', 570, 635)


def right():
    global platform_x
    if platform_x+plat_width < display_width-150:
        platform_x += 2

def left():
    global platform_x
    if platform_x > 20:
        platform_x -= 2

def boll_move_x():
    global boll_x, boll_control_x
    
    if boll_control_x == 1:
        boll_x += boll_moves_x

    if boll_control_x == -1:
        boll_x -= boll_moves_x
        
    if boll_control_x == 0:
        boll_x += boll_moves_x

def boll_move_y():
    global  boll_y, boll_control_y
    if boll_control_y == -1:
        boll_y -= boll_moves_y
    if boll_control_y == 1:
        boll_y += boll_moves_y

def check_boll_x():
    global boll_control_x, boll_control_y, boll, boll_moves_x

    if boll_x+15 >= display_width-150:
        boll_moves_x = random.choice(boll_step_x)
        boll_control_x = -1
    if boll_x <= 19:
        boll_moves_x = random.choice(boll_step_x)
        boll_control_x = 1
    if boll_x+15 == platform_x and boll_y+20 == platform_y:
        boll_moves_x = random.choice(boll_step_x)
        boll_control_x = -1
    
    if boll_x + 15 == platform_x and boll_y + 15 > platform_y:
        boll_control_x = -1
    if boll_x == platform_x + plat_width and boll_y + 15 > platform_y:
        boll_control_x = 1

def check_boll_y():
    global boll_control_y, boll_moves_y

    if boll_x + 15 >= platform_x and boll_x <= platform_x+platform_width:
        if boll_y + 15 >= platform_y and boll_y < platform_y:
            boll_moves_y = random.choice(boll_step_y)
            boll_control_y = -1 

    if boll_y >= display_height:
        pass
    
    if boll_y <= 85:
        boll_moves_y = random.choice(boll_step_y)
        boll_control_y = 1


def platform_lenght_plus():
    global plat_width, lenght_pl, platform_width, platform_x, Platform_skin
    platform_width += 2
    plat_width += 2
    lenght_pl += 2
    platform_x -= 1

def platform_lenght_minus():
    global plat_width, lenght_pl, platform_width, platform_x
    platform_width -= 2
    plat_width -= 2
    lenght_pl -= 2
    platform_x += 1



def platform_lenght_time():
    global plat_len_time
    if plat_time_start:
        plat_len_time += 1

def broken_y():
    global boll_control_y
    if Level_1.broken == 1:
        boll_control_y = 1
        Level_1.broken = 0
    if Level_1.broken == -1:
        boll_control_y = -1
        Level_1.broken = 0

def broken_x():
    global boll_control_x
    if Level_1.broken_x == 1:
        boll_control_x = 1
        Level_1.broken_x = 0
    if Level_1.broken_x == -1:
        boll_control_x = -1
        Level_1.broken_x = 0

font_doc = pygame.font.Font('DevFont.ttf', 10) 

def print_text(messege, x, y):
    text = font_doc.render(messege, True, WHITE)
    display.blit(text, (x, y))

def print_pause(messege, x, y, font_color = (255, 255, 255), font_type = 'GameFont.ttf', font_size = 30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(messege, True, font_color)
    display.blit(text, (x, y))

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_pause('PAUSED... PRESS SPACE TO CONTINUE', 80, 400)

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            paused = False

        pygame.display.update()
        pygame.time.Clock().tick(15)

def game_run_ENTER():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_pause('PRESS ENTER TO START GAME', 120, 400)

        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            paused = False
        pygame.display.update()
        pygame.time.Clock().tick(15)


def game_time():
    global game_start
    for i in range(600):
        pygame.display.update()
        print_pause('3', 260, 400)
    blit_screen()
    for i in range(600):
        pygame.display.update()
        print_pause('2', 260, 400)
    blit_screen()
    for i in range(600):
        pygame.display.update()
        print_pause('1', 260, 400)
    blit_screen()
    game_start = False


def pause_game():
    pause()
    blit_screen()
    game_time()

game_run()