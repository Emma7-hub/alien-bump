import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a class representing a single alien in a fleet"""

    def __init__(self, ai_game):
        """initialize an alien 😎"""
        super().__init__()
        self.screen = ai_game.screen

        # load the alien image and set its rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start each alien near top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact x position
        self.x = float(self.rect.x)
