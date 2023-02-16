import pygame
import sys

WIDTH = 1000
HEIGHT = 650
PLATFORM_HEIGHT = 4


def events(rocket, start_screen):
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            sys.exit()
        # клавиша нажата
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rocket.move_up = True
            elif event.key == pygame.K_DOWN:
                rocket.move_down = True
            elif event.key == pygame.K_LEFT:
                rocket.move_left = True
            elif event.key == pygame.K_RIGHT:
                rocket.move_right = True
            elif event.key == pygame.K_SPACE:
                start_screen.start_screen_on = False  # нажали пробел => заставка выкл
        # клавиша отжата
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                rocket.move_up = False
            elif event.key == pygame.K_DOWN:
                rocket.move_down = False
            elif event.key == pygame.K_LEFT:
                rocket.move_left = False
            elif event.key == pygame.K_RIGHT:
                rocket.move_right = False


def collisions(rocket, platform):
    # проверка на коллизию ракеты и платформы
    if pygame.sprite.collide_rect(rocket, platform):
        # если приземление точно на платформу
        if rocket.rect.right <= platform.rect.right and \
                rocket.rect.left >= platform.rect.left:
            rocket.win = True  # успешная посадка
        else:
            rocket.loss = True # ракета разбилась
    elif rocket.rect.right >= WIDTH or rocket.rect.left <= 0 or \
            rocket.rect.top <= 0 or rocket.rect.top + 32 >= HEIGHT:  # top + 32 = bottom
        rocket.loss = True  # ракета разбилась


