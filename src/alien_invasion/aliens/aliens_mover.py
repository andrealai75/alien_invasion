from settings import Settings
from .alien import Alien


class AliensMover:
    def __init__(self, screen, rect, aliens):
        self.settings = Settings()
        self.screen = screen
        self.rect = rect
        self.aliens = aliens
        self.moving_step_x = self.settings.alien_move_x_speed
        self.moving_step_y = 0

    def _refresh_rect(self):
        self.rect.x = self.screen.get_rect().width
        self.rect.width = 0
        for alien in self.aliens:
            self.rect.x = min(self.rect.x, alien.rect.x)
            self.rect.width = max(alien.rect.x + Alien.rect().width - self.rect.x, self.rect.width)

    def move(self):
        self._refresh_rect()
        self._update_moving_direction()
        self.rect.x += self.moving_step_x
        for alien in self.aliens:
            alien.update(self.moving_step_x, self.moving_step_y)

    def _change_direction(self):
        self.moving_step_y = self.settings.alien_move_y_speed
        self.rect.y += self.moving_step_y
        self.moving_step_x *= -1

    def _update_moving_direction(self):
        if self.moving_step_x > 0:
            if (self.rect.x + self.rect.width) >= self.screen.get_rect().width:
                self._change_direction()
                return
        else:
            if self.rect.x <= 0:
                self._change_direction()
                return
        self.moving_step_y = 0
