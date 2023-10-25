import pygame

class Ship:
  """A class to manage the ship."""
  
  def __init__(self, ai_game):
    """Initialize the ship and set te its starting position."""
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()
    self.settings = ai_game.settings
    
    # Load the ship image and get the rect.
    self.image = pygame.image.load('images/ship.bmp')
    self.rect = self.image.get_rect()
    
    # Start each new ship at the bottom center of the screen.
    self.rect.midbottom = self.screen_rect.midbottom
    
  def blitme(self):
    """Draw the ship at its current location"""
    self.screen.blit(self.image, self.rect)
    
  def move_right(self):
    new_left = self.rect.left + self.settings.ship_speed
    new_edge = new_left + self.rect.width
    if new_edge < self.screen_rect.width:
      self.rect.left = new_left
    
  def move_left(self):
    new_left = self.rect.left - self.settings.ship_speed
    if new_left > 0:
      self.rect.left = new_left
