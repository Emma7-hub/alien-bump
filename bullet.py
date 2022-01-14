import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """to manage the bullets fired from the ship"""

    def __init__(self, ai_game):
        """to create a bullet object at ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create a bullet rect at (0, 0) and then set current position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # store the bullet's position as a decimal
        self.y = float(self.rect.y)

    def update(self):
        # move bullets up to the top
        self.y -= self.settings.bullet_speed
        # update bullet position
        self.rect.y = self.y

    def draw_bullet(self):
        # drawing each bullet
        pygame.draw.rect(self.screen, self.color, self.rect)
