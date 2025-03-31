from .imports import *
from .Strategies import *
from .TavernEnvironment import TavernEnvironment
from .APIWrapper import APIWrapper
from .TavernCommands import NPC_Command

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from coord import Coord
    from maps.base import Map
    from tiles.base import MapObject
    from tiles.map_objects import *
    from message import Message
    from NPC import NPC

########################################################################################################
class Tavernkeeper(NPC, SelectionInterface):
    """
    Creating the Tavern NPC by extending the NPC to also implement a selection interface then copying computer.
    """
    
    def __init__(self, tavern: TavernEnvironment, wrapper: APIWrapper, strategy: NPCStrategy):
        
        self.tavern = tavern
        self.wrapper = wrapper
        self.strategy = strategy

        menu_options = {
            "The Adventurer": NPC_Command("Adventurer", self.strategy),
            "The Scholar": NPC_Command("Scholar", self.strategy),
            "The Poet": NPC_Command("Poet", self.strategy),
            "The Crush": NPC_Command("Crush", self.strategy)
        }

        super().__init__(
            name="Tavernkeeper",
            image="player3",
            encounter_text="Welcome to my Tavern! I would love to introduce you to my patrons! Most are slightly shy and won't talk to you until you ask me about them, so ask away!",
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
        if self.tavern.has_interacted(npc_name="Tavernkeeper"):
            return [MenuMessage(self, player, self.__menu_name, list(self.__menu_options))]
        
        self.tavern.has_interacted("Tavernkeeper")

        player.set_current_menu(self)
        return [DialogueMessage(self, player, self._NPC__encounter_text, self.get_image_name()) ,
                 MenuMessage(self, player, self.__menu_name, list(self.__menu_options))]
 

########################################################################################################
# Class for Adventurer
class Adventurer(NPC):

    # Constructor for the Adventurer
    def __init__(self, tavern: TavernEnvironment, wrapper: APIWrapper, strategy: NPCStrategy):

        self.tavern = tavern
        self.wrapper = wrapper
        self.strategy = strategy

        super().__init__(
            name="Adventurer",
            image="player4",
            encounter_text="",
            facing_direction="down",
            staring_distance = 0,
            bg_music='',
        )

    def player_interacted(self, player: "HumanPlayer") -> list[Message]:
        
        self.command = NPC_Command(self.tavern.get_artifact(), self.strategy)
        
        return self.command.execute(player.get_current_room(), player)
    
########################################################################################################
        
# class Scholar
        
# class Poet
        
# class Crush
        