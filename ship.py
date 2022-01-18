import pygame


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load('images/spaceship1.bmp')
        self.rect = self.image.get_rect()

        # start each new ship  at bottom-center
        self.rect.midbottom = self.screen_rect.midbottom

        # store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

          # movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ship's position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """draw the ship at its location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """centers the ship back"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
