from settings import Settings
from cartridge import Cartridge
from random import randint
import pygame
import time

class AliensShooting():
    def __init__(self, screen, rect, aliens, cartridge):
        self.settings = Settings()
        self.screen = screen
        self.rect = rect
        self.aliens = aliens
        self.cartridge = cartridge
        self.last_fire_time = time.time()

    def fire(self):
        if time.time() - self.last_fire_time > self.settings.alien_shoot_every_in_seconds:
            for alien in self._aliens_with_line_of_sight():
                if randint(0, 5) == 0:
                    alien.fire(self.cartridge)
                    self.last_fire_time = time.time()

    def _aliens_with_line_of_sight(self):
        ready_to_shoot_aliens = []
        for alien in self.aliens:
            if self._is_line_of_sight_clear(alien):
                ready_to_shoot_aliens.append(alien)
        return ready_to_shoot_aliens
    
    def _is_line_of_sight_clear(self, shooter):
        is_clear = True
        line_of_sight = self._line_of_sight(shooter)
        for alien in self.aliens:
            if alien.rect.colliderect(line_of_sight):
                is_clear = False
                break
        return is_clear

    def _line_of_sight(self, alien):
        left = alien.rect.left + alien.image.get_rect().width / 2
        top = alien.rect.top + alien.image.get_rect().height 
        width = 1
        height = self.rect.height
        return pygame.rect.Rect(left, top, width, height)
    