import pygame


class Battle:
    def __init__(self, hero, cartridge, aliens):
        self.aliens = aliens
        self.hero = hero
        self.cartridge = cartridge
        self.still_playing = True
        self.alien_defeated = False
        self.ship_hit = False
        self.reached_bottom = False

    def update(self):
        self.check_for_hits()
        if self.aliens.defeated():
            self.still_playing = False
            self.alien_defeated = True
        elif self.aliens.reached_bottom(self.hero.rect.height):
            self.still_playing = False
            self.reached_bottom = True
        elif self._check_for_ship_hit():
            self.still_playing = False
            self.ship_hit = True

    def _check_for_ship_to_alien_hits(self):
        for bullet in self.cartridge.bullets.copy():
            for alien in self.aliens.aliens.copy():
                if alien.rect.contains(bullet.rect):
                    self.cartridge.bullets.remove(bullet)
                    self.aliens.aliens.remove(alien)

    def _check_for_ship_hit(self):
        for bullet in self.cartridge.bullets:
            if self.hero.rect.contains(bullet.rect):
                return True
        return False

    def check_for_hits(self):
        self._check_for_ship_to_alien_hits()
