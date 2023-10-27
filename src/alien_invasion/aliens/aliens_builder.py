import pygame
import math
from .alien import Alien
from settings import Settings


class AliensBuilder:
    def __init__(self, screen, rect):
        self.settings = Settings()
        self.screen = screen
        self.rect = rect
        self._aliens = pygame.sprite.Group()

    @property
    def aliens(self):
        return self._aliens

    def build(self):
        y_position = self.settings.alien_margin_y
        num_launched = 0
        for rank in range(self._num_of_ranks()):
            num_left_to_launch = self.settings.aliens_num - num_launched
            num_in_this_rank = min([num_left_to_launch, self._max_per_rank()])
            self.launch_a_rank(num_in_this_rank, y_position)
            num_launched += num_in_this_rank
            y_position += Alien(self.settings, self.screen).rect.height + \
                self.settings.alien_margin_y

    def _num_of_ranks(self):
        return math.ceil(self.settings.aliens_num / self._max_per_rank())

    def _max_per_rank(self):
        return math.floor(self.rect.width / (Alien.rect().width + self.settings.alien_margin_x))

    def _gap(self, num):
        return int((self.rect.width - Alien.rect().width * num) / num)

    def launch_an_alien(self, x, y):
        an_alien = Alien(self.settings, self.screen)
        an_alien.set_position(x, y)
        self._aliens.add(an_alien)

    def launch_a_rank(self, num, y):
        gap = self._gap(num)
        x = self.rect.x
        self.launch_an_alien(x, y)
        for i in range(2, num + 1):
            x += Alien.rect().width + gap
            self.launch_an_alien(x, y)
        self.rect.height += Alien.rect().height + self.settings.alien_margin_y
