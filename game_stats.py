class GameStats:
    """Track ALIEN invade stats"""
    def __init__(self, ai_game):
        """initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()
        # start A.I game in an active state
        self.game_active = False

    def reset_stats(self):
        """initialize stats that can change during a game"""
        self.ships_left = self.settings.ship_limit
