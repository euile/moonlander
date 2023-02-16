import pygame
import control
from platform import Platform
from rocket import Rocket
from start_screen import Startscreen
from winner import Landed
from loser import Crashed

FPS = 60
WIDTH = 1000
HEIGHT = 650

BLACK = (0, 0, 0)  # задний фон

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # граф область
pygame.display.set_caption("Moonlander")
clock = pygame.time.Clock()

platform = Platform(screen)
rocket = Rocket(screen)
start_screen = Startscreen(screen)  # заставка перед игрой
landed = Landed(screen)  # экран победителя
crashed = Crashed(screen)  # экран проигравшего

while True:  # обработка событий пользователя
    clock.tick(FPS)

    control.events(rocket, start_screen)

    if start_screen.start_screen_on:  # пока не нажат пробел
        start_screen.output()  # выводим заставку
    elif rocket.win:
        landed.output()  # выводим экран победителя
    elif rocket.loss:
        crashed.output()  # выводим экран проигравшего
    else:
        # обновление
        rocket.update()
        # рендеринг
        screen.fill(BLACK)  # заливка
        rocket.output()
        platform.output()
        control.collisions(rocket, platform)
    # после отрисовки всего, переворачиваем экран
    pygame.display.flip()
