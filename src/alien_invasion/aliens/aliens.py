from .aliens_rect import AliensRect
from .aliens_builder import AliensBuilder
from .aliens_mover import AliensMover
from .aliens_shooting import AliensShooting
from settings import Settings


class Aliens:
    """Class to manage all the Aliens in the game"""

    def __init__(self, screen, cartridge):
        self.screen = screen
        self.cartridge = cartridge
        self.settings = Settings()
        self.rect = AliensRect(screen)
        builder = AliensBuilder(screen, self.rect)
        builder.build()
        self.aliens = builder.aliens
        self.mover = AliensMover(self.screen, self.rect, self.aliens)
        self.shooting = AliensShooting(
            self.screen, self.rect, self.aliens, self.cartridge)

    def defeated(self):
        if len(self.aliens) == 0:
            return True
        return False

    def reached_bottom(self, margin):
        for alien in self.aliens:
            if alien.reached_bottom(margin):
                return True
        return False

    def update(self):
        self.mover.move()
        self.shooting.fire()

    def draw(self):
        for alien in self.aliens:
            alien.draw()
