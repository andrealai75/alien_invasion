import pygame
import sys


class KeyboardHandler():
    def __init__(self, hero, cartridge, aliens):
        self.hero = hero
        self.cartridge = cartridge
        self.aliens = aliens

    def handle(self):
        self._check_keydowns()
        self._check_pressed()

    def _check_keydowns(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self._keydown(event)

    def _check_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.hero.move_right()
        if keys[pygame.K_LEFT]:
            self.hero.move_left()

    def _keydown(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self.cartridge.fire(self.hero.rect.midtop)
