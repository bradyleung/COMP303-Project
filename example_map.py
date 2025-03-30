# Imports
from .imports import *
from .Strategies import *
from .TavernEnvironment import TavernEnvironment
from .APIWrapper import APIWrapper
from .TavernCommand import NPC_Command

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from coord import Coord
    from maps.base import Map
    from tiles.base import MapObject
    from tiles.map_objects import *
    from message import Message
    from NPC import NPC

#############################################################################

# class Tavernkeeper(NPC): 

#     def __init__()

class Tavernkeeper(NPC, SelectionInterface):
    """
    Creating the Tavern NPC by extending the NPC to also implement a selection interface then copying computer.
    """
    
    def __init__(self, tavern: TavernEnvironment, wrapper: APIWrapper):
        
        self.tavern = tavern
        self.wrapper = wrapper

        menu_options = {
            "The Adventurer": NPC_Command("Adventurer", TavernkeeperStrategy(tavern, wrapper)),
            "The Scholar": NPC_Command("Scholar", TavernkeeperStrategy(tavern, wrapper)),
            "The Poet": NPC_Command("Poet", TavernkeeperStrategy(tavern, wrapper)),
            "The Crush": NPC_Command("Crush", TavernkeeperStrategy(tavern, wrapper))
        }

        super().__init__(
            name="Tavernkeeper",
            image="player3",
            encounter_text="Welcome to my Tavern! I would love to introduce you to the... lovely patrons we have here. Just ask about any of them and I'll introduce them to you!",
            facing_direction="right",
            staring_distance = 0,
            bg_music='',
        )

        self.__menu_name = "Which NPC would you wish to learn about?"
        self.__menu_options = menu_options


    def select_option(self, player: "HumanPlayer", option: str) -> list[Message]:
        return self.__menu_options[option].execute(player.get_current_room(), player)
    

    # Method for when the player interacts with the Tavernkeeper
    def player_interacted(self, player: "HumanPlayer") -> list[Message]:

        # If its the first time talking to him he will introduce himself.
        if self.tavern.is_npc_unlocked(npc_name="Tavernkeeper"):
            return [MenuMessage(self, player, self.__menu_name, list(self.__menu_options))]
        
        self.tavern.unlock_npc("Tavernkeeper")

        player.set_current_menu(self)
        return [DialogueMessage(self, player, self._NPC__encounter_text, self.get_image_name()) ,
                 MenuMessage(self, player, self.__menu_name, list(self.__menu_options))]
 


# Class for Adventurer
        
# class Scholar
        
# class Poet
        
# class Crush
        


class ExampleHouse(Map):
    def __init__(self) -> None:
        
        # Getting singleton instances
        self.tavern = TavernEnvironment()
        self.wrapper = APIWrapper()
        
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
        tavernkeeper = Tavernkeeper(tavern = self.tavern, wrapper = self.wrapper )
        objects.append((tavernkeeper, Coord(11, 1))) 


        return objects
    



# class ScorePressurePlate(PressurePlate):
#     def __init__(self, image_name='pressure_plate'):
#         super().__init__(image_name)
    
#     def player_entered(self, player) -> list[Message]:
#         messages = super().player_entered(player)

#         # add score to player
#         player.set_state("score", player.get_state("score") + 1)

#         return messages