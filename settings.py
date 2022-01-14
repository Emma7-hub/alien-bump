class Settings:
    """this class stores all the settings of the game"""

    def __init__(self):
        """initialize the game settings"""
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.2
        # bullets
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (72, 72, 72)
        self.bullets_allowed = 5
