import pygame


class EndGame:
    def __init__(self, settings, screen, battle):
        self.battle = battle
        self.screen = screen
        self.settings = settings

        font = pygame.font.Font(self.settings.font, 75)
        self.text = font.render(
            self._message(), True, self.settings.text_color, self.settings.bg_color)
        self.rect = self.text.get_rect()
        self.rect.center = self.screen.get_rect().center

    def draw(self):
        self.screen.blit(self.text, self.rect)

    def _message(self):
        if self.battle.alien_defeated:
            return 'You won ... Well Done!!!!'
        elif self.battle.reached_bottom:
            return 'Game Over!!'
        elif self.battle.ship_hit:
            return 'Hero was hit - Game Over!!'
