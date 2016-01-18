
class Item(object):
    """This is the base class for all items"""

    def __init__(self, name, itype, slot, stats, rarity="common",
        attributes=None):
        """Item is simply a container of the item definition. Slot is
        the equipment slot the item fits into."""
        self.name = name
        self.itype = itype
        self.slot = slot
        self.stats = stats
        self.rarity = rarity
        if attributes:
            self.attributes = attributes
        else:
            attributes = []