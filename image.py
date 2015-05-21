from pygame import image
from view import Renderable

class Image(Renderable):
    def __init__(self, pos, img, h_anchor=0, v_anchor=0, filename=""):
        Renderable.__init__(self, pos)

        if filename != "":
            self.img = image.load(filename).convert()
        else:
            self.img = surface
        self.h_anchor = h_anchor
        self.v_anchor = v_anchor

    def __del__(self):
        super(Renderable)

    def draw(surface):
        size = self.img.get_size()

        if self.h_anchor < 0:
            x_offset = -size[0]
        elif self.h_anchor > 0:
            x_offset = 0
        else:
            x_offset = -size[0] / 2

        if self.v_anchor < 0:
            y_offset = -size[1]
        elif self.v_anchor > 0:
            y_offset = 0
        else:
            y_offset = -size[1] / 2

        surface.blit(self.img, (self.pos[0] + x_offset, self.pos[1] + y_offset))