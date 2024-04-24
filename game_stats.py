import json


class GameStats:
    """Track statistics for alien invasion"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        # start Alien Invasion in a active state.
        self.game_active = False
        self.high_score = self.get_saved_high_score()

    def get_saved_high_score(self):
        """"Get saved high score from the file if it exists"""
        try:
            with open('high_score.json') as f:
                return json.load(f)
        except FileNotFoundError:
            return 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
