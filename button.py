import pygame.font

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Button:
    def __init__(self, game: 'AlienInvasion', msg) -> None:
        self.game = game
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
