from .abc_bullet import AbcBullet


class BulletAlien(AbcBullet):
    def __init__(self, settings, screen, pos):
        super().__init__(settings, screen, pos)
        self.color = self.settings.alien_bullet_color

    def update(self):
        self.y += self.settings.bullet_speed
        self.rect.y = self.y
