import pygame

WIDTH = 1000
HEIGHT = 650


class Rocket:
    """Ракета"""

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/rocket.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.top = self.screen_rect.top + 1
        self.move_up = False
        self.move_down = False
        self.move_left = False
        self.move_right = False
        self.speedx, self.speedy = (0, 2)
        # правая и левая границы платформы пригодятся в collisions
        self.rect.right = self.rect.centerx + 13  # 16 это половина ширины ракеты
        self.rect.left = self.rect.centerx - 13
        # флаги выигрыша и проигрыша
        self.win = False
        self.loss = False

    def update(self):
        """Обновления ракеты"""
        # не улетит за пределы граф области
        if self.rect.top > 0 and self.rect.bottom < HEIGHT and self.rect.right < WIDTH and self.rect.left > 0:
            if self.move_up:
                self.speedy -= 0.2
            if self.move_down:
                self.speedy += 0.2
            if self.move_right:
                self.speedx += 0.2
            if self.move_left:
                self.speedx -= 0.2
            self.rect.y += self.speedy
            self.rect.x += self.speedx


    def output(self):
        self.screen.blit(self.image, self.rect)
