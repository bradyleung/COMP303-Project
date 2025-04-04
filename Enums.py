from enum import Enum

class PlayerState(Enum):
    TALKING_TO = "talking_to"
    POEM = "poem"
    UNLOCKED_NPCS = "unlocked_npcs"

class NPCNames(Enum):
    TAVERNKEEPER =  "Tavernkeeper"
    ADVENTURER = "Adventurer"
    SCHOLAR = "Scholar"
    POET = "Poet"
    CRUSH = "Crush"