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

icon = pygame.image.load("images\\icon.png")
icon = pygame.transform.scale(icon, (16, 16)).convert_alpha()
pygame.display.set_icon(icon)
pygame.display.set_caption("School game")


display = pygame.display.set_mode((display_width, display_height))

# ��������� ��������� �� ����
platform_width = 90
platform_height = 15
platform_x = (display_width-105)//2 - 45
platform_y = display_height - 60

# ������� ������ "���������� ���������"
lenght_pl = 20
plat_width = 90
plat_len_time = 0
plat_time_start = False

# ������������ ���� �� ����
boll_x = (display_width-150)//2 + 10
boll_y = display_height - 350
boll_width = 15
boll_height = 15

boll_speed = [(1, 2), (2, 3), (1, 2, 3)]


# ���������� �������� ����
boll_step_x = boll_speed[2]
boll_step_y = boll_speed[2]

# "���������" ��������� ����
boll_control_x = 0
boll_control_y = 1

# �������������� �������� ����
boll_moves_x = random.choice(boll_step_x)
boll_moves_y = 2

# ��������� ��� ���������� ���������
press_f = True


# ���������� ������ ������
USER_HELTH = 3


FPS = pygame.time.Clock()
FPS_time = 100

# �������� �������� �����������
Fon = pygame.image.load('images\\Fon.png').convert_alpha()
Background = pygame.image.load('images\\background.png').convert_alpha()

# �������� �������� ������ ������
helth = pygame.image.load('images\\Helth\\Helth.png').convert_alpha()
helth = pygame.transform.scale(helth,(30, 30))
helth_out = pygame.image.load('images\\Helth\\Helth_out.png').convert_alpha()
helth_out = pygame.transform.scale(helth_out,(30, 30))

# ������������� ���� � ������������ ������
Boll_skin = Change_skin.Bolls[0]
Platform_skin = Change_skin.Platforms[0]

# �������� ������� ��� ������
font_doc = pygame.font.Font('Fonts\\DevFont.ttf', 10)
score_font = pygame.font.Font('Fonts\\GameFont.ttf', 22)
pause_font = pygame.font.Font('Fonts\\GameFont.ttf', 30)
game_over_font = pygame.font.Font('Fonts\\GameFont.ttf', 25)

# �������� ������ ����
pause_ON = pygame.mixer.Sound("Sounds\\Pause_ON.wav")
pause_OFF = pygame.mixer.Sound("Sounds\\Pause_OFF.wav")
hit = pygame.mixer.Sound("Sounds\\hit.wav")
lose = pygame.mixer.Sound("Sounds\\lose.wav")
win = pygame.mixer.Sound("Sounds\\win.wav")
over = pygame.mixer.Sound("Sounds\\Game_over.wav")

game_start = True

def game_run():
    global Platform_skin
    game = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        Level_1.play_score() # ����� ����� �����
        blit_screen() # �������� ���� ��������� �����������

        # ��� ������ ���� �� ������� ������ ENTER
        if game_start:
            game_run_ENTER()
            blit_screen()
            game_time()
        # �������� ������� ����
        if game:
            global press_f, press_f, plat_len_time, plat_time_start, FPS_time, \
            boll_moves_y, boll_moves_x,boll_control_y

            # �������� �������������� ����
            check_boll_y()
            check_boll_x()

            # �������� ����
            boll_move_x()
            boll_move_y()

            # �������� ��������� �� ����������
            Level_1.check_obj_brocken(boll_x, boll_y)
            broken_y()
            broken_x()
            check_lvl_win()

            # �������� ���������
            key = pygame.key.get_pressed()
            if key[pygame.K_RIGHT]:
                right()

            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                left()

            # ����� "��������� ���������" , �������� ��������
           # key = pygame.key.get_pressed()
            #if key[pygame.K_f]:
             #   if press_f:
              #      for i in range (20):
               #         platform_lenght_plus()
                #    plat_time_start = True
                 #   press_f = False

            
            # �����
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                pause_game()

            # ������� "��������� ���������"
            platform_lenght_time()

            # ���������� ������
            if plat_len_time >= 1000000:
                for i in range (20):
                    platform_lenght_minus()

                press_f = True
                plat_time_start = False
                plat_len_time = 0
        # ENTER ��� ������ ����
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            game = True


        pygame.display.update()
        FPS.tick(FPS_time)

# ��������� ���� ����������� �� ������
def blit_screen():
            display.fill((0, 0, 0))
            display.blit(pygame.transform.scale(Background, (505, 600)), (10, 80, 505, 600))
            display.blit(Fon, (0, 0, display_width, display_height))
            display.blit(Boll_skin, (boll_x, boll_y, boll_width, boll_height))
            display.blit(Platform_skin, (platform_x, platform_y, platform_width, platform_height))
            Level_1.objects_skin()
            print_text('Developed for a school project by D.K (vk.com/d.e_mon)', 0, 0, 0)
            print_text('Beta version 1.5', 570, 635, 0)
            print_text('SCORE', 525, 410, 1)
            print_text(Level_1.text_score, 575, 410, 1)
            print_helth()

# �������� ��������� ������
def right():
    global platform_x
    if platform_x+plat_width < display_width-150:
        platform_x += 2

# �������� ��������� �����
def left():
    global platform_x
    if platform_x > 20:
        platform_x -= 2

# ���������� �������� ����
def boll_move_x():
    global boll_x, boll_control_x
    
    if boll_control_x == 1:
        boll_x += boll_moves_x

    if boll_control_x == -1:
        boll_x -= boll_moves_x
        
    if boll_control_x == 0:
        boll_x += boll_moves_x

# �������� ���� �� ��� Y
def boll_move_y():
    global  boll_y, boll_control_y
    if boll_control_y == -1:
        boll_y -= boll_moves_y
    if boll_control_y == 1:
        boll_y += boll_moves_y

# �������� ���� �� ��� X
def check_boll_x():
    global boll_control_x, boll_control_y, boll, boll_moves_x

    if boll_x+15 >= display_width-150:
        hit.play()
        boll_moves_x = random.choice(boll_step_x)
        boll_control_x = -1
    if boll_x <= 19:
        hit.play()
        boll_moves_x = random.choice(boll_step_x)
        boll_control_x = 1
    if boll_x+15 == platform_x and boll_y+20 == platform_y:
        hit.play()
        boll_moves_x = random.choice(boll_step_x)
        boll_control_x = -1
    
    if boll_x + 15 == platform_x and boll_y + 15 > platform_y:
        hit.play()
        boll_control_x = -1
    if boll_x == platform_x + plat_width and boll_y + 15 > platform_y:
        hit.play()
        boll_control_x = 1
# �������� ��������� ���� �� ��� Y
def check_boll_y():
    global boll_control_y, boll_moves_y

    if boll_x + 15 >= platform_x and boll_x <= platform_x+platform_width:
        if boll_y + 15 >= platform_y and boll_y < platform_y:
            hit.play()
            boll_moves_y = random.choice(boll_step_y)
            boll_control_y = -1 

    if boll_y >= display_height:
        lose.play()
        game_loose()
    
    if boll_y <= 85:
        hit.play()
        boll_moves_y = random.choice(boll_step_y)
        boll_control_y = 1

# ��������� ��������� 
def platform_lenght_plus():
    global plat_width, lenght_pl, platform_width, platform_x, Platform_skin
    platform_width += 2
    plat_width += 2
    lenght_pl += 2
    platform_x -= 1

# ���������� ���������
def platform_lenght_minus():
    global plat_width, lenght_pl, platform_width, platform_x
    platform_width -= 2
    plat_width -= 2
    lenght_pl -= 2
    platform_x += 1


# ����� �������� ������
def platform_lenght_time():
    global plat_len_time
    if plat_time_start:
        plat_len_time += 1

# ������ �� ��������� ��������� �� ��� Y
def broken_y():
    global boll_control_y
    if Level_1.broken == 1:
        boll_control_y = 1
        Level_1.broken = 0
    if Level_1.broken == -1:
        boll_control_y = -1
        Level_1.broken = 0

# ������ �� ���������� �������� �� ��� X
def broken_x():
    global boll_control_x
    if Level_1.broken_x == 1:
        boll_control_x = 1
        Level_1.broken_x = 0
    if Level_1.broken_x == -1:
        boll_control_x = -1
        Level_1.broken_x = 0

# ��������� ���� ������� �� ������
def print_text(messege, x, y, play):
    if play == 0:
        text = font_doc.render(messege, True, WHITE)
    if play == 1:
        text = score_font.render(messege, True, WHITE)
    if play == 2:
        text = pause_font.render(messege, True, WHITE)
    if play == 3:
        text = game_over_font.render(messege, True, WHITE)

    display.blit(text, (x, y))


# �����
def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text('PAUSED... PRESS SPACE TO CONTINUE', 80, 400, 2)
        print_text('or ESCAPE to exit', 170, 440, 2)

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            paused = False

        if key[pygame.K_ESCAPE]:
            pygame.quit()
            quit()

        pygame.display.update()
        pygame.time.Clock().tick(15)

# ������ ���� �� ������� �� ENTER
def game_run_ENTER(play = 'now'):
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if play == 'now':
            print_text('PRESS ENTER TO START GAME', 120, 400, 2)

        if play == 'again':
            print_text('PRESS ENTER TO PLAY AGAIN', 130, 400, 2)

        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            paused = False

        pygame.display.update()
        pygame.time.Clock().tick(15)

# �������� ������ �� ������ ���� 
def game_time():
    global game_start
    for i in range(700):
        pygame.display.update()
        print_text('3', 260, 400, 2)
    blit_screen()
    for i in range(700):
        pygame.display.update()
        print_text('2', 260, 400, 2)
    blit_screen()
    for i in range(700):
        pygame.display.update()
        print_text('1', 260, 400, 2)
    blit_screen()
    game_start = False

# ������ ������ ��� ����� 
def pause_game(play = 'now'):
    pygame.time.wait(200)
    pause_ON.play()
    if play == 'now':
        pause()
        blit_screen()
        game_time()
    if play == 'again':
        game_run_ENTER(play = 'again')
        blit_screen()
        game_time()
    pause_OFF.play()


# ��������� ����������� ���������� ������ �� ������ 
def print_helth():
    if USER_HELTH == 3:
        display.blit(helth,(530, 350, 30, 30))
        display.blit(helth,(570, 350, 30, 30))
        display.blit(helth,(610, 350, 30, 30))
        pygame.display.update()
    if USER_HELTH == 2:
        display.blit(helth,(530, 350, 30, 30))
        display.blit(helth,(570, 350, 30, 30))
        display.blit(helth_out,(610, 350, 30, 30))
        pygame.display.update()    
    if USER_HELTH == 1:
        display.blit(helth,(530, 350, 30, 30))
        display.blit(helth_out,(570, 350, 30, 30))
        display.blit(helth_out,(610, 350, 30, 30))
        pygame.display.update()
    if USER_HELTH == 0:
        display.blit(helth_out,(530, 350, 30, 30))
        display.blit(helth_out,(570, 350, 30, 30))
        display.blit(helth_out,(610, 350, 30, 30))

# ������� ��������� ������ 
def game_loose():
    global USER_HELTH, boll_y, boll_x, platform_x, platform_y
    if USER_HELTH != 1:
        USER_HELTH -= 1
        boll_x = (display_width-150)//2 + 10
        boll_y = display_height - 350
        platform_x = (display_width-105)//2 - 45
        platform_y = display_height - 60
        game_run_ENTER(play = 'again')
        blit_screen()
        game_time()
    elif USER_HELTH == 1:
        USER_HELTH -= 1
        game_over()

# ����� ����
def game_over():
    game = True
    over.play()
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()        
        blit_screen()
        print_text('GAME OVER', 200, 400, 2)
        print_text('Press ENTER to play again or ESC to exit', 100, 500, 3)
        pygame.display.update()
        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:
            pygame.quit()
            quit()

        if key[pygame.K_RETURN]:
            restart()
        FPS.tick(5)

def check_lvl_win():
    if Level_1.obj_count >= 44:
        pygame.display.update()
        blit_screen()
        win.play()
        print_text('YOU WIN!', 215, 400, 2)
        pygame.display.update()
        pygame.time.wait(6000)
        game_over()




# ������� ����������� ����
def restart():
    global boll_y, boll_x, platform_x, platform_y, USER_HELTH, game_start, \
    boll_control_x, boll_control_y

    boll_control_x = 0
    boll_control_y = 1
    boll_x = (display_width-150)//2 + 10
    boll_y = display_height - 350 
    platform_x = (display_width-105)//2 - 45
    platform_y = display_height - 60   
    USER_HELTH = 3
    game_start = True
    Level_1.restart()
    game_run()

#������ ���� �� ����
def start():
    global boll_step_x, boll_step_y, Boll_skin, Platform_skin
    f = open('Settings.bin', 'rb')
    skins = f.readline().split()
    boll_step_x = boll_speed[(int(skins[0]))]
    boll_step_y = boll_speed[(int(skins[0]))]
    Boll_skin = Change_skin.Bolls[(int(skins[1]))]
    Platform_skin = Change_skin.Platforms[(int(skins[2]))]
    game_run()