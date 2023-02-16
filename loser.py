import pygame


class Crashed:

    def __init__(self, screen):
        """ Экран когда ракета разбилась"""
        self.screen = screen
        self.image = pygame.image.load('images/try_again.png')
        self.start_rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.start_rect.center = self.screen_rect.center

    def output(self):
        self.screen.blit(self.image, self.start_rect)
