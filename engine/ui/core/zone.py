"""Defines the Zone class"""
import pygame

class Zone(object):
    """Zone object defines clickable zones on the screen that can
    execute events (functions). It is not responsible for the rendering
    of the elements on the screen."""

    NEUTRAL = 0
    HOVERED = 1
    CLICKED = 2

    def __init__(self, rect):
        """Takes a pygame rect or any tuple equivalents and a on_click
        the rect describes where the zone is on the screen, and the on_click
        is the function that is given a game object on click.
        on_hover and off hover have also been defined"""
        super(Zone, self).__init__()
        self.rect = pygame.Rect(rect)
        self.state = Zone.NEUTRAL

    def update_rect(self, rect):
        self.rect = rect

    def update(self, game):
        """Updates the state of the zone using mouse input from pygame."""
        # if previously clicked and button is no longer clicked we call
        # on click
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            state = Zone.HOVERED
            if pygame.mouse.get_pressed()[0]:
                state = Zone.CLICKED
        else:
            state = Zone.NEUTRAL
        self.state = state
