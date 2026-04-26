import pygame.font

class Button:
    def __init__(self, game, msg) -> None:
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        