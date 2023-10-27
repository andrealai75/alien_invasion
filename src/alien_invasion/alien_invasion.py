from aliens import Aliens
from alien_invasion.battle import Battle
from alien_invasion.end_game import EndGame
from cartridge import Cartridge
from alien_invasion.hero import Hero
from alien_invasion.settings import Settings
from keyboard_handler import KeyboardHandler
import sys
import pygame
import os

from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.cartridge = Cartridge(self.screen)
        self.hero = Hero(self.screen)
        self.aliens = Aliens(self.screen, self.cartridge)
        self.keyboard_handler = KeyboardHandler(self.hero, self.cartridge, self.aliens)
        self.battle = Battle(self.hero, self.cartridge, self.aliens)

    def run_game(self):
        while True:
            self.keyboard_handler.handle()
            self.aliens.update()
            self.cartridge.update()
            self.battle.update()
            self._refresh_screen()

    def _refresh_screen(self):
        if self.battle.still_playing:
            self.screen.fill(self.settings.bg_color)
            self.hero.draw()
            self.aliens.draw()
            self.cartridge.draw()
        else:
            EndGame(self.settings, self.screen, self.battle).draw()

        pygame.display.flip()
        self.clock.tick(self.settings.clock)
