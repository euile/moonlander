import pygame


class Startscreen:

    def __init__(self, screen):
        """ Экран заставки"""
        self.screen = screen
        self.image1 = pygame.image.load('images/press_space.png')
        self.start_rect = self.image1.get_rect()
        self.screen_rect = screen.get_rect()
        self.start_rect.center = self.screen_rect.center
        self.start_screen_on = True

    def output(self):
        self.screen.blit(self.image1, self.start_rect)
