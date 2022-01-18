class Settings:
    """this class stores all the settings of the game"""

    def __init__(self):
        """initialize the game settings"""
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        # ship
        self.ship_speed = 1.7
        self.ship_limit = 3
        # bullets
        self.bullet_speed = 1.3
        self.bullet_width = 15
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 10
        # aliens
        self.fleet_drop_speed = 10

        # how the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """starts settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet direction 1 = right, -1 = left
        self.fleet_direction = 1

    def increase_speed(self):
        """increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
