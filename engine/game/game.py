"""Define Game object"""

class Game(object):
    """Game object used to hold all the data required for
    rendering and holding the important info for the game"""

    DUNGEON_TYPES = ["catacomb", "caverns"]

    def __init__(self):
        super(Game, self).__init__()
        self.difficulty = "normal"
        self.floor_level = 1
        self.floor_type = ""
        self.current_location = None
        self.current_dialog = None

        self.party = []
        self.encounter = []
        self.current_move = None
        self.current_target = None
        self.current_dialog = None
        self.focus_window = None

        self.shop = None
        self.alter = None
        self.loot = []

        self.mouse_button = (0, 0, 0)
        self.mouse_x = 0
        self.mouse_y = 0
        self.resolution = (0, 0)

        self.selected_move = None
        self.selected_target = None
        self.selected_player = None

        self.current_hover = None
        self.hover_x = 0
        self.hover_y = 0

        self.render_travel = False