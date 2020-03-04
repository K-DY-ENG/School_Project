import pygame
import random
import Change_skin
import Arkanoid

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
ACTIVE = (249, 95, 5)

display = pygame.display.set_mode((display_width, display_height))

FPS_time = 30
FPS = pygame.time.Clock()

menu_font = pygame.font.Font('Fonts\\Menu_font.otf', 30)
menu_font_small = pygame.font.Font('Fonts\\Menu_font.otf', 20)
doc_font =  pygame.font.Font('Fonts\\Menu_font.otf', 15)

font_back_color = ACTIVE
font_plat_color = WHITE
font_boll_color = WHITE
font_boll_speed = WHITE
back_botton = menu_font.render('BACK', True, font_back_color)

low_speed = WHITE
normal_speed = WHITE
random_speed = ACTIVE



text = doc_font.render('Developed for a school project by D.K (vk.com/d.e_mon)', True, (255, 255, 255))
text2 =  doc_font.render('Version 1.3', True, (255, 255, 255))




play_color = (249, 95, 5)
about_color = (255, 255, 255)
settings_color = (255, 255, 255)
exit_color = (255, 255, 255)

play = 0
about = 0
settings = 0
exit = 0
ON = 1
choose_ON = 1
boll_set = 182
plat_set = 241

choose_speed_control = 2
choose_boll_color_control = 1
choose_plat_color_control = 1

#Пишет кнопки меню в соответствии с шрифтом
def font():
    global play, about, settings, exit
    play = menu_font.render('PLAY', True, play_color)
    about = menu_font.render('ABOUT', True, about_color)
    settings = menu_font.render('SETTINGS', True, settings_color)
    exit = menu_font.render('EXIT', True, exit_color)

#Функция выхода по нажатия на крестик
def ex():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
#Цикл меню
def menu():
    while ON:
        ex()
        font()
        blit_screen()
        pygame.display.update()
        botton_play()
        FPS.tick(FPS_time)

pygame.mixer.music.load("Sounds\\Intro_Music.ogg")
pygame.mixer.music.play(-1, 0.0)

#Рисует все на экране
def blit_screen():
    display.fill((0, 0, 0))
    display.blit(play, (285, 150))
    display.blit(about, (275, 250))
    display.blit(settings, (250, 350))
    display.blit(exit, (290, 450))
    pygame.display.update()

#Кнопка PLAY
def botton_play():
    global ON, about_color, exit_color, play_color
    pygame.time.wait(200)
    while ON:   
        pygame.display.update()
        ex()
        about_color = exit_color = (255, 255, 255)
        play_color = (249, 95, 5)
        font()
        blit_screen()
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            pygame.time.wait(100)
            ON = 0
            pygame.mixer.music.stop()
            pygame.time.wait(100)
            f = open('Settings.bin', 'wb')
            f.write(bytes(str(choose_speed_control) + ' ' + str(choose_boll_color_control) \
                                                    + ' ' + str(choose_plat_color_control), 'utf8'))
            f.close()
            Arkanoid.start()
        if key[pygame.K_DOWN]:
            botton_about()
        if key[pygame.K_UP]:
            botton_exit()
            FPS.tick(FPS_time)

#Кнопка ABOUT
def botton_about():
    global play_color, settings_color, about_color
    pygame.time.wait(200)
    while ON:
        pygame.display.update()
        ex()
        about_color = (249, 95, 5)
        settings_color = play_color = (255, 255, 255)
        font()
        blit_screen()
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            about_screen()
        if key[pygame.K_DOWN]:
            botton_settings()
        if key[pygame.K_UP]:
            botton_play()
            FPS.tick(FPS_time)

#Кнопка SETTINGS
def botton_settings():
    global about_color, settings_color, exit_color
    pygame.time.wait(200)
    while ON:
        pygame.display.update()
        ex()
        settings_color = (249, 95, 5)
        exit_color = about_color = (255, 255, 255)
        font()
        blit_screen()
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            pygame.time.wait(100)
            settings_screen()
        if key[pygame.K_DOWN]:
            botton_exit()
        if key[pygame.K_UP]:
            botton_about()
            FPS.tick(FPS_time)

#Кнопка EXIT
def botton_exit():
    global play_color, settings_color, exit_color
    pygame.time.wait(200)
    while ON:
        pygame.display.update()
        ex()
        exit_color = (249, 95, 5)
        settings_color = play_color = (255, 255, 255)
        font()
        blit_screen()
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            pygame.quit()
            quit()            
        if key[pygame.K_DOWN]:
            botton_play()
        if key[pygame.K_UP]:
            botton_settings()
            FPS.tick(FPS_time)


#При нажатии на кнопку ABOUT
def about_screen():
    display.fill((0, 0, 0))
    display.blit(back_botton, (290, 500))
    display.blit(text, (65, 200))
    display.blit(text2, (285, 300))
    pygame.display.update()
    while ON:
        pygame.time.wait(150)
        ex()
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            botton_about()



#При нажатии на кнопку SETTINGS
def settings_screen():
    pygame.time.wait(200)
    while ON:
        pygame.time.wait(150)
        ex()
        settings_blit()
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            botton_settings()
        if key[pygame.K_UP]:
            settings_speed()
        if key[pygame.K_DOWN]:
            settings_boll_skin()

#Рисует кнопки во вкладке SETTINGS
def settings_blit():
        display.fill((0, 0, 0))
        display.blit((menu_font_small.render('Boll color:', True, font_boll_color)), (30, 100))
        display.blit((menu_font_small.render('Platorm color:', True, font_plat_color)), (30, 250))
        display.blit((menu_font_small.render('Boll speed:', True, font_boll_speed)), (30, 400))
        display.blit((menu_font.render('BACK:', True, font_back_color)), (290, 500))
        pygame.display.update()


#Кновка SPEED в SETTINGS
def settings_speed():
    global font_plat_color, font_back_color, font_boll_speed
    pygame.time.wait(200)
    while ON:
        ex()
        font_boll_speed = ACTIVE
        font_back_color = font_plat_color = WHITE
        settings_blit()
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN] or key[pygame.K_RIGHT]:
            choose_speed()
        if key[pygame.K_UP]:
            settings_plat_skin()
        if key[pygame.K_DOWN]:
            font_back_color = ACTIVE
            font_boll_speed = WHITE
            settings_screen()


#Кнопка BOLL SKIN в SETTINGS
def settings_boll_skin():
    global font_plat_color, font_back_color, font_boll_color
    pygame.time.wait(200)
    while ON:
        ex()
        font_boll_color = ACTIVE
        font_plat_color = font_back_color = WHITE
        settings_blit()
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            font_boll_color = WHITE
            font_back_color = ACTIVE
            settings_screen()
        if key[pygame.K_DOWN]:
            settings_plat_skin()
        if key[pygame.K_RETURN] or key[pygame.K_RIGHT]:
            choose_boll_skin()

#Кнопка PLATFORM SKIN в SETTINGS
def settings_plat_skin():
    global font_plat_color, font_boll_color, font_boll_speed
    pygame.time.wait(200)
    while ON:
        ex()
        font_plat_color = ACTIVE
        font_boll_speed = font_boll_color = WHITE
        settings_blit()
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            settings_boll_skin()
        if key[pygame.K_DOWN]:
            settings_speed()
        if key[pygame.K_RETURN] or key[pygame.K_RIGHT]:
            choose_plat_skin()



#Выбор скорости игры
def choose_speed():
    global font_boll_speed, low_speed, normal_speed, random_speed, choose_ON, choose_speed_control
    pygame.time.wait(200)
    while ON:
        ex()
        font_boll_speed = WHITE
        key = pygame.key.get_pressed()
        
        if choose_ON:
            settings_blit()
            blit_choose_speed()
            pygame.display.update()
            choose_ON = 0

        if key[pygame.K_UP] or key[pygame.K_DOWN] or key[pygame.K_RETURN]:
            choose_ON = 1
            settings_speed()
        
        if key[pygame.K_LEFT]:
            if choose_speed_control == 2:
                choose_speed_control = 1
                pygame.time.wait(200)
                low_speed = WHITE
                random_speed = WHITE
                normal_speed = ACTIVE
                blit_choose_speed()
                pygame.display.update()
            elif choose_speed_control == 1:
                choose_speed_control = 0
                pygame.time.wait(200)
                random_speed = WHITE
                normal_speed = WHITE
                low_speed = ACTIVE
                blit_choose_speed()
                pygame.display.update()
            elif choose_speed_control == 0:
                choose_speed_control = 2
                pygame.time.wait(200)
                normal_speed = WHITE
                low_speed = WHITE
                random_speed = ACTIVE
                blit_choose_speed()
                pygame.display.update()
        if key[pygame.K_RIGHT]:
            if choose_speed_control == 1:
                choose_speed_control = 2
                pygame.time.wait(200)
                random_speed = ACTIVE
                low_speed = WHITE
                normal_speed = WHITE
                blit_choose_speed()
                pygame.display.update()
            elif choose_speed_control == 0:
                choose_speed_control = 1
                pygame.time.wait(200)
                normal_speed = ACTIVE
                random_speed = WHITE
                low_speed = WHITE
                blit_choose_speed()
                pygame.display.update()
            elif choose_speed_control == 2:
                choose_speed_control = 0
                pygame.time.wait(200)
                low_speed = ACTIVE
                normal_speed = WHITE
                random_speed = WHITE
                blit_choose_speed()
                pygame.display.update()

#Анимация выбора скорости
def blit_choose_speed():
    display.blit((menu_font_small.render('Low', True, low_speed)), (230, 400))
    display.blit((menu_font_small.render('Normal', True, normal_speed)), (310, 400))
    display.blit((menu_font_small.render('Random', True, random_speed)), (430, 400))


#Выбор скина платформы
def choose_plat_skin():
    global font_plat_color, choose_ON, plat_set, choose_plat_color_control
    pygame.time.wait(200)
    while ON:
        ex()
        font_plat_color = WHITE
        key = pygame.key.get_pressed()
        
        if choose_ON:
            settings_blit()
            blit_choose_plat_skin()
            pygame.display.update()
            choose_ON = 0
        if key[pygame.K_UP] or key[pygame.K_DOWN] or key[pygame.K_RETURN]:
            choose_ON = 1
            settings_plat_skin()
        if key[pygame.K_RIGHT]:
            if choose_plat_color_control == 1:
                choose_plat_color_control = 2
                pygame.time.wait(200)
                plat_set = 361
                settings_blit()
                blit_choose_plat_skin()
            elif choose_plat_color_control == 2:
                choose_plat_color_control = 3
                pygame.time.wait(200)
                plat_set = 481
                settings_blit()
                blit_choose_plat_skin()
            elif choose_plat_color_control == 3:
                choose_plat_color_control = 1
                pygame.time.wait(200)
                plat_set = 241
                settings_blit()
                blit_choose_plat_skin()

        if key[pygame.K_LEFT]:
            if choose_plat_color_control == 1:
                choose_plat_color_control = 3
                pygame.time.wait(200)
                plat_set = 481
                settings_blit()
                blit_choose_plat_skin()
            elif choose_plat_color_control == 3:
                choose_plat_color_control = 2
                pygame.time.wait(200)
                plat_set = 361
                settings_blit()
                blit_choose_plat_skin()
            elif choose_plat_color_control == 2:
                choose_plat_color_control = 1
                pygame.time.wait(200)
                plat_set = 241
                settings_blit()
                blit_choose_plat_skin()


#Анимация выбора платформы
def blit_choose_plat_skin():
    display.blit(Change_skin.Platform_first_skin, (250, 255, 90, 15))
    display.blit(Change_skin.Platform_second_skin, (370, 255, 90, 15))
    display.blit(Change_skin.Platform_third_skin, (490, 255, 90, 15))
    pygame.draw.rect(display, ACTIVE, (plat_set, 258, 5, 6))
    pygame.draw.rect(display, WHITE, (240, 257, 7, 8), 1)
    pygame.draw.rect(display, WHITE, (360, 257, 7, 8), 1)
    pygame.draw.rect(display, WHITE, (480, 257, 7, 8), 1)
    pygame.display.update()


#Выбор цвета мяча
def choose_boll_skin():
    global font_boll_color, choose_ON, boll_set, choose_boll_color_control
    pygame.time.wait(200)
    while ON:
        ex()
        font_boll_color = WHITE
        key = pygame.key.get_pressed()
        
        if choose_ON:
            settings_blit()
            blit_choose_boll_skin()
            pygame.display.update()
            choose_ON = 0
        if key[pygame.K_UP] or key[pygame.K_DOWN] or key[pygame.K_RETURN]:
            choose_ON = 1
            settings_boll_skin()
        if key[pygame.K_RIGHT]:
            if choose_boll_color_control == 1:
                choose_boll_color_control = 2
                pygame.time.wait(200)
                boll_set = 222
                Change_skin.boll_color = Change_skin.Boll_blue
                settings_blit()
                blit_choose_boll_skin()
            elif choose_boll_color_control == 2:
                choose_boll_color_control = 3
                pygame.time.wait(200)
                boll_set = 262
                Change_skin.boll_color = Change_skin.Boll_pink
                settings_blit()
                blit_choose_boll_skin()
            elif choose_boll_color_control == 3:
                choose_boll_color_control = 4
                pygame.time.wait(200)
                boll_set = 302
                Change_skin.boll_color = Change_skin.Boll_red
                settings_blit()
                blit_choose_boll_skin()
            elif choose_boll_color_control == 4:
                choose_boll_color_control = 5
                pygame.time.wait(200)
                boll_set = 342
                Change_skin.boll_color = Change_skin.Boll_white
                settings_blit()
                blit_choose_boll_skin()
            elif choose_boll_color_control == 5:
                choose_boll_color_control = 6
                pygame.time.wait(200)
                boll_set = 382
                Change_skin.boll_color = Change_skin.Boll_yellow
                settings_blit()
                blit_choose_boll_skin()
            elif choose_boll_color_control == 6:
                choose_boll_color_control = 1
                pygame.time.wait(200)
                boll_set = 182
                Change_skin.boll_color = Change_skin.Boll_green
                settings_blit()
                blit_choose_boll_skin()

        if key[pygame.K_LEFT]:
            if choose_boll_color_control == 1:
                choose_boll_color_control = 6
                pygame.time.wait(200)
                boll_set = 382
                Change_skin.boll_color = Change_skin.Boll_yellow
                settings_blit()
                blit_choose_boll_skin()
            elif choose_boll_color_control == 6:
                choose_boll_color_control = 5
                pygame.time.wait(200)
                boll_set = 342
                Change_skin.boll_color = Change_skin.Boll_white
                settings_blit()
                blit_choose_boll_skin()
            elif choose_boll_color_control == 5:
                choose_boll_color_control = 4
                pygame.time.wait(200)
                boll_set = 302
                Change_skin.boll_color = Change_skin.Boll_red
                settings_blit()
                blit_choose_boll_skin()
            elif choose_boll_color_control == 4:
                choose_boll_color_control = 3
                pygame.time.wait(200)
                boll_set = 262
                Change_skin.boll_color = Change_skin.Boll_pink
                settings_blit()
                blit_choose_boll_skin()
            elif choose_boll_color_control == 3:
                choose_boll_color_control = 2
                pygame.time.wait(200)
                boll_set = 222
                Change_skin.boll_color = Change_skin.Boll_blue
                settings_blit()
                blit_choose_boll_skin()
            elif choose_boll_color_control == 2:
                choose_boll_color_control = 1
                pygame.time.wait(200)
                boll_set = 182
                Change_skin.boll_color = Change_skin.Boll_green
                settings_blit()
                blit_choose_boll_skin()


#Анимация выбора цвета мяча
def blit_choose_boll_skin():
    pygame.draw.rect(display, ACTIVE, (boll_set, 111, 5, 6))
    pygame.draw.rect(display, WHITE, (181, 110, 7, 8), 1)
    pygame.draw.rect(display, WHITE, (221, 110, 7, 8), 1)
    pygame.draw.rect(display, WHITE, (261, 110, 7, 8), 1)
    pygame.draw.rect(display, WHITE, (301, 110, 7, 8), 1)
    pygame.draw.rect(display, WHITE, (341, 110, 7, 8), 1)
    pygame.draw.rect(display, WHITE, (381, 110, 7, 8), 1)
    display.blit(Change_skin.Boll_green, (190, 107, 15, 15))
    display.blit(Change_skin.Boll_blue, (230, 107, 15, 15))
    display.blit(Change_skin.Boll_pink, (270, 107, 15, 15))
    display.blit(Change_skin.Boll_red, (310, 107, 15, 15))
    display.blit(Change_skin.Boll_white, (350, 107, 15, 15))
    display.blit(Change_skin.Boll_yellow, (390, 107, 15, 15))
    pygame.display.update()

menu()
