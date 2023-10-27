import pygame
from settings import Settings


class AliensRect(pygame.Rect):
    def __init__(self, screen):
        self.screen = screen
        self.settings = Settings()
        self._initialise()

    def _initialise(self):
        self.width = self.screen.get_rect().width * 0.9
        self.height = 0
        self.x = 20
