import pygame
import random

PLATFORM_WIDTH = 80
PLATFORM_HEIGHT = 4
WHITE = (255, 255, 255)


class Platform:
    """Платформа для посадки ракеты"""
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect = pygame.Rect((0, 0), (PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.color = WHITE
        self.rect.centerx = random.randint(0, self.screen_rect.right - PLATFORM_WIDTH / 2)
        self.rect.bottom = self.screen_rect.bottom
        # правая и левая границы платформы пригодятся в collisions
        self.rect.right = self.rect.centerx + PLATFORM_WIDTH / 2
        self.rect.left = self.rect.centerx - PLATFORM_WIDTH / 2

    def output(self):
        """Вывод платформы"""
        pygame.draw.rect(self.screen, self.color, self.rect)