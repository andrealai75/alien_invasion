import abc
import pygame

class AbcBullet(abc.ABC):
    def __init__(self, settings, screen, pos):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = pos

        # Store the bullet's position as a float
        self.y = float(self.rect.y)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    @abc.abstractmethod
    def update(self):
        pass
