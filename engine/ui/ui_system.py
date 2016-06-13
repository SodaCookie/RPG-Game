"""Implements the UI System"""
from collections import OrderedDict

import pygame

from engine.system import System, Message
import engine.ui.manager as manager

class UISystem(System):
    """System responsible for handling game related events"""

    layouts = {
        "scenario" : ["background", "party", "scenario"],
        "default" : ["background", "party", "castbar", "sidebar"],
        "character" : ["background", "party", "castbar", "sidebar",
                       "character"],
        # "battle" : ["background", "party", "castbar", "encounter"],
        # "travel" : ["background", "party", "travel", "sidebar"],
        # "loot" : ["background", "party", "loot", "sidebar"]
    }

    def __init__(self, game):
        super().__init__(game, "ui")
        self.managers = OrderedDict()
        self.rendering = []

    def init(self, game):
        width, height = pygame.display.get_surface().get_size()
        self.managers["background"] = manager.BackgroundManager(
            "image/ui/catacomb-background-COPYRIGHTED.jpg")
        self.managers["party"] = manager.PartyManager(32, height - 204)
        self.managers["sidebar"] = manager.SideBarManager(0, 10, width)
        # self.managers["encounter"] = manager.EncounterManager()
        self.managers["castbar"] = manager.CastBarManager(
            width // 2 - (56 * 10 + 14) // 2, 440, 10)
        # self.managers["loot"] = manager.LootManager(450, 20, 300, 400)
        self.managers["scenario"] = manager.ScenarioManager(
            width // 2 - 300, 52, 600, 400)
        # self.managers["travel"] = manager.TravelManager(
        #     800, 300, 1280//2-800//2, 100)
        # self.managers["level"] = manager.LevelUpManager(1280, 720)
        self.managers["character"] = manager.CharacterManager(
            width // 2 - 400, 72, 800, 348)
        self.rendering = self.layouts["scenario"]

    def update(self, delta, game):
        messages = self.flush_messages()
        for message in messages:
            self.dispatch(message, game)

        # Render Managers
        surface = pygame.display.get_surface()
        surface.fill((0, 0, 0))
        for manager in self.rendering:
            self.managers[manager].render(surface, game, self.game)

    def set_layout(self, layout):
        self.rendering = self.layouts[layout]

    def dispatch(self, message, game):
        """Function for determining what action to call depending on the
        message"""
        if message.mtype == "layout": # Travels the part
            layout = message.args[0]
            self.set_layout(layout)