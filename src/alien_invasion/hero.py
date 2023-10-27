import pygame
from settings import Settings


class Hero:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = Settings()

        # Load the hero image and get the rect.
        self.image = pygame.image.load('images/hero.bmp')
        self.rect = self.image.get_rect()

        # Start each new hero at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def move_right(self):
        new_left = self.rect.left + self.settings.ship_speed
        new_edge = new_left + self.rect.width
        if new_edge < self.screen_rect.width:
            self.rect.left = new_left

    def move_left(self):
        new_left = self.rect.left - self.settings.ship_speed
        if new_left > 0:
            self.rect.left = new_left
