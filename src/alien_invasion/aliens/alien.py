import pygame
from pygame.sprite import Sprite
from cartridge import Cartridge

class Alien(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

    @staticmethod
    def rect():
        return pygame.image.load('images/alien.bmp').get_rect()

    def update(self, move_x, move_y):
        self.rect.x += move_x
        self.rect.y += move_y

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def reached_bottom(self, margin):
        if (self.rect.y + self.rect.height + margin) >= self.screen.get_rect().height:
            return True
        return False
    
    def fire(self, cartridge):
        cartridge.fire_ship(self.rect.midbottom)
