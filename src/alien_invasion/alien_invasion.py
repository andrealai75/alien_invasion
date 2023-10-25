import sys
import pygame
import os

from os.path import dirname, join, abspath

sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from alien_invasion.settings import Settings
from alien_invasion.ship import Ship
from alien_invasion.bullet import Bullet


class AlienInvasion:
  """Overall class to mange game assets and behavior"""
  
  def __init__(self):
    pygame.init()
    self.clock = pygame.time.Clock()
    self.settings = Settings()
    self.screen = pygame.display.set_mode(
      (self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    self.ship = Ship(self)
    self.bullets = pygame.sprite.Group()

  def run_game(self):
    """Start the main loop for the game."""
    
    while True:
      self._check_events()
      self._hold_key()
      self._clear_bullets()
      self.bullets.update()
      self._update_screen()

  def _fire_bullet(self):
    if len(self.bullets) < self.settings.max_bullets:
      self.bullets.add(Bullet(self))
  
  def _keydown(self, event):
    if event.key == pygame.K_q:
      sys.exit()
    if event.key == pygame.K_SPACE:
      self._fire_bullet()

  def _check_events(self):
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      if event.type == pygame.KEYDOWN:
        self._keydown(event)

  def _update_screen(self):
    # Redraw the screen during each pass through the loop.
    self.screen.fill(self.settings.bg_color)
    self.ship.blitme()
    
    for bullet in self.bullets:
      bullet.draw_bullet()

    # Make the most recently drawn screen visible
    pygame.display.flip()
    self.clock.tick(60)
    
  def _hold_key(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
      self.ship.move_right() 
    if keys[pygame.K_LEFT]:
      self.ship.move_left()

  def _clear_bullets(self):
    for bullet in self.bullets.copy():
      if bullet.rect.bottom <= 0:
        self.bullets.remove(bullet)