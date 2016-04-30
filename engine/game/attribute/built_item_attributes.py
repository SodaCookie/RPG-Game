"""Compilation of attributes that can be used for items. Some will be unique
for unique items. Some will be classified as available for rare items, Some
will be classified as available for legendary items."""

from engine.game.attribute.built_attributes import *

RARE_ATTRIBUTES = {}
LEGENDARY_ATTRIBUTES = {}
UNIQUE_ATTRIBUTES = {}

# RARE ATTRIBUTE SEGMENT
RARE_ATTRIBUTES["strong"] = RaiseStat(2, "attack")
RARE_ATTRIBUTES["unbreaking"] = RaiseStat(2, "defense")
RARE_ATTRIBUTES["arcane"] = RaiseStat(2, "magic")
RARE_ATTRIBUTES["resisting"] = RaiseStat(2, "resist")
RARE_ATTRIBUTES["quick"] = RaiseStat(2, "speed")
RARE_ATTRIBUTES["bolstering"] = RaiseStat(2, "health")
RARE_ATTRIBUTES["preemptive"] = RaiseStat(2, "action")

# LEGENDARY ATTRIBUTE SEGMENT
LEGENDARY_ATTRIBUTES["really strong"] = RaiseStat(3, "attack")
LEGENDARY_ATTRIBUTES["really unbreaking"] = RaiseStat(3, "defense")
LEGENDARY_ATTRIBUTES["really arcane"] = RaiseStat(3, "magic")
LEGENDARY_ATTRIBUTES["really resisting"] = RaiseStat(3, "resist")
LEGENDARY_ATTRIBUTES["really quick"] = RaiseStat(3, "speed")
LEGENDARY_ATTRIBUTES["really bolstering"] = RaiseStat(3, "health")
LEGENDARY_ATTRIBUTES["really preemptive"] = RaiseStat(3, "action")