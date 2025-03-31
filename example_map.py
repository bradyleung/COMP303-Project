# Imports
from .imports import *
from .Strategies import *
from .TavernEnvironment import TavernEnvironment
from .APIWrapper import APIWrapper
from .TavernNPCs import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from coord import Coord
    from maps.base import Map
    from tiles.base import MapObject
    from tiles.map_objects import *
    from message import Message
    from NPC import NPC

#############################################################################

class ExampleHouse(Map):
    def __init__(self) -> None:
        
        # Getting singleton instances & instances of every NPCStrategy
        self.tavern = TavernEnvironment()
        self.wrapper = APIWrapper()

        self.tavernkeeperStrategy = TavernkeeperStrategy(tavern=self.tavern, wrapper=self.wrapper)
        self.adventurerStrategy = AdventurerStrategy(tavern=self.tavern, wrapper=self.wrapper)
        self.scholarStrategy = ScholarStrategy(tavern=self.tavern, wrapper=self.wrapper)
        
        super().__init__(
            name="Example House",
            description="Welcome to the Tavern",
            size=(15, 15),
            entry_point=Coord(14, 7),
            background_tile_image='wood_planks',
        )

    
    def get_objects(self) -> list[tuple[MapObject, Coord]]:
        objects: list[tuple[MapObject, Coord]] = []

        # add a door
        door = Door('int_entrance', linked_room="Trottier Town")
        objects.append((door, Coord(14, 7)))

        # add a pressure plate
        # pressure_plate = ScorePressurePlate()
        # objects.append((pressure_plate, Coord(13, 7)))

        # add the tavernkeeper
        tavernkeeper = Tavernkeeper(tavern=self.tavern, wrapper=self.wrapper, strategy=self.tavernkeeperStrategy)
        objects.append((tavernkeeper, Coord(11, 1))) 

        # add the adventurer
        adventurer = Adventurer(tavern=self.tavern, wrapper=self.wrapper, strategy=self.adventurerStrategy)
        objects.append((adventurer, Coord(2, 13)))


        return objects
    



# class ScorePressurePlate(PressurePlate):
#     def __init__(self, image_name='pressure_plate'):
#         super().__init__(image_name)
    
#     def player_entered(self, player) -> list[Message]:
#         messages = super().player_entered(player)

#         # add score to player
#         player.set_state("score", player.get_state("score") + 1)

#         return messages