import pygame
from .bullet_ship import BulletShip
from .bullet_alien import BulletAlien
from settings import Settings


class Cartridge:
    def __init__(self, screen):
        self.bullets = []
        self.screen = screen
        self.settings = Settings()

    def update(self):
        self._make_it_drop()
        for bullet in self.bullets:
            bullet.update()

    def fire(self, pos):
        if len(self.bullets) < self.settings.bullets_max_num:
            self.bullets.append(BulletShip(self.settings, self.screen, pos))

    def fire_ship(self, pos):
        self.bullets.append(BulletAlien(self.settings, self.screen, pos))

    def _make_it_drop(self):
        for bullet in self.bullets.copy():
            if not self.screen.get_rect().colliderect(bullet.rect):
                self.bullets.remove(bullet)

    def draw(self):
        for bullet in self.bullets:
            bullet.draw()
