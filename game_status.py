class GameStatus:
    def __init__(self, ai_game):
        self.ships_left = None
        self.settings = ai_game.settings
        self.reset_status()
        self.game_active = False
        self.score = 0
        self.highest_score = 0
        self.level = 1

    def reset_status(self):
        self.ships_left = self.settings.ship_limit
