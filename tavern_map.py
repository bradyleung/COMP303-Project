# Imports
from .imports import *
from .ScholarInterpreter import ScholarInterpreter
from .TavernEnvironment import TavernEnvironment
from .APIWrapper import APIWrapper
from .TavernNPCs import *
from .Enums import PlayerState, NPCNames

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from coord import Coord
    from maps.base import Map
    from tiles.base import MapObject
    from tiles.map_objects import *
    from command import ChatCommand
    from message import Message
    from NPC import NPC
    from Player import HumanPlayer

##############################################################################################   
class ScholarInputCommand(ChatCommand):
    name = 'ask'
    desc = 'Ask the Scholar any question after interacting with the NPC.'

    @classmethod
    def matches(cls, command_text: str) -> bool:
        return command_text.startswith("ask")
    
    def execute(self, command_text: str, context: "ExampleHouse", player: HumanPlayer) -> list[Message]: 
        
        # Get the player's current state and make sure that they are currently talking to the Scholar
        talking_to = player.get_state(PlayerState.TALKING_TO.value)

        if talking_to == "Scholar":

            # Get the instance of the scholar to use his strategy from the npcs dict
            scholar = context.npcs.get("Scholar")
            interpreter = ScholarInterpreter(context.wrapper)

            command_text = command_text[3:] # Remove "ask" from their input
            
            # If their question is not a question
            if "?" not in command_text:                
                command = InteractCommand(command_text, scholar.rude)

            else: 
                # use the wrapper to determine which strategy to set 
                understood = interpreter.is_question_understood(command_text)
                
                if understood: 
                    command = InteractCommand(command_text, scholar.mysterious)
                
                else:
                    command = InteractCommand(command_text, scholar.confused)

            return command.execute(player.get_current_room(), player)
        
        else:
            return [ChatMessage(
                sender = self, 
                recipient = player,
                text = "You are not currently speaking to the Scholar. Interact to ask him a question.",
            )]         

class PoetInputCommand(ChatCommand):
    name = 'theme'
    desc = "Say the theme for the Poet's poem."

    @classmethod
    def matches(cls, command_text: str) -> bool:
        return command_text.startswith("theme")
    
    def execute(self, command_text: str, context: "ExampleHouse", player: HumanPlayer) -> list[Message]: 
        
        # Get the player's current state and make sure that they are currently talking to the Poet
        talking_to = player.get_state(PlayerState.TALKING_TO.value)

        if talking_to == NPCNames.POET.value:

            command_text = command_text[5:] # Remove "theme" from their theme
            
            # Get the instance of the poet to use his strategies 
            poet = context.npcs.get("Poet")

            strategy = 

            command = InteractCommand(command_text, poet.strategy)

            return command.execute(player.get_current_room(), player)
        
        else:
            return [ChatMessage(
                sender = self, 
                recipient = player,
                text = "You are not currently speaking to the Poet. Go help him out!.",
            )]     

class ResetStateCommand(ChatCommand):
    name = 'reset'
    desc = 'Reset all saved progress with NPCs'

    @classmethod
    def matches(cls, command_text: str) -> bool:
        return command_text.startswith("reset")
    
    def execute(self, command_text: str, context: "ExampleHouse", player: HumanPlayer) -> list[Message]: 
        
        player.set_state(PlayerState.UNLOCKED_NPCS.value, list())
        player.set_state(PlayerState.POEM.value, None)
        player.set_state(PlayerState.TALKING_TO.value, None)

        return [ChatMessage(
                sender = self, 
                recipient = player,
                text = "You and the NPCs have now forgotten everything...",
            )] 

######################################################################################################
# DECORATIONS
class TavernCounter(IntDecor):
        def __init__(self, npc: "NPC") -> None:
            super().__init__('counter3')
            self.__npc: "NPC" = npc

        def player_interacted(self, player: "HumanPlayer") -> None:
           return self.__npc.player_interacted(player)
        
class Table(MapObject):
    def __init__(self, image_name: str='roundtable', z_index: int = 0) -> None:
        super().__init__(f'tile/int_decor/{image_name}', passable=False, z_index=z_index)

class RightChair(MapObject):
    def __init__(self, image_name: str='rightchair', z_index: int = 0) -> None:
        super().__init__(f'tile/int_decor/{image_name}', passable=False, z_index=z_index)

class LeftChair(MapObject):
    def __init__(self, image_name: str='leftchair', z_index: int = 0) -> None:
        super().__init__(f'tile/int_decor/{image_name}', passable=False, z_index=z_index)

class TopChair(MapObject):
    def __init__(self, image_name: str='topchair', z_index: int = 0) -> None:
        super().__init__(f'tile/int_decor/{image_name}', passable=False, z_index=z_index)

class BottomChair(MapObject):
    def __init__(self, image_name: str='bottomchair', z_index: int = 0) -> None:
        super().__init__(f'tile/int_decor/{image_name}', passable=False, z_index=z_index)

class Bookshelf(MapObject):
    def __init__(self, image_name: str='bookshelf', z_index: int = 0) -> None:
        super().__init__(f'tile/int_decor/{image_name}', passable=False, z_index=z_index)

class Armorstand(MapObject):
    def __init__(self, image_name: str='armorstand', z_index: int = 0) -> None:
        super().__init__(f'tile/int_decor/{image_name}', passable=False, z_index=z_index)

class TrophyCarpet(MapObject):
    def __init__(self, image_name: str='carpet', z_index: int = 0) -> None:
        super().__init__(f'tile/int_decor/{image_name}', passable=True, z_index=z_index)

class Carpet(MapObject):
    def __init__(self, image_name: str='carpet2', z_index: int = 0) -> None:
        super().__init__(f'tile/int_decor/{image_name}', passable=True, z_index=z_index)

class Chest(MapObject):
    def __init__(self, image_name: str='chest', z_index: int = 0) -> None:
        super().__init__(f'tile/int_decor/{image_name}', passable=False, z_index=z_index)
        
class BlackTable(MapObject):
    def __init__(self, image_name: str='blacktable', z_index: int = 0) -> None:
        super().__init__(f'tile/int_decor/{image_name}', passable=False, z_index=z_index)
        
        
class ExampleHouse(Map):
    
    MAIN_ENTRANCE = True
    
    def __init__(self) -> None:

        # Getting singleton instances & and one instance of CommandFactories
        self.tavern = TavernEnvironment()
        self.wrapper = APIWrapper()

        self.interactFactory = InteractCommandFactory()
        self.responseFactory = YesNoCommandFactory()
        self.artifactFactory = ChangeArtifactFactory()

 
        super().__init__(
            name="Example House",
            description="Welcome to the Tavern!!!",
            size=(15, 15),
            entry_point=Coord(14, 7),
            background_tile_image='tavernfloor1',
            chat_commands=[ScholarInputCommand, PoetInputCommand, ResetStateCommand]
        )
    
    def get_objects(self) -> list[tuple[MapObject, Coord]]:
        objects: list[tuple[MapObject, Coord]] = []

        # add a door
        door = Door('int_entrance', linked_room="Trottier Town", is_main_entrance = True)
        objects.append((door, Coord(14, 7)))

        # add a pressure plate
        # pressure_plate = ScorePressurePlate()
        # objects.append((pressure_plate, Coord(13, 7)))


        tavernkeeper = Tavernkeeper(tavern=self.tavern, wrapper=self.wrapper, interact_factory=self.interactFactory)

        # add the bar for the tavernkeeper to be behind
        counter = TavernCounter(tavernkeeper)
        objects.append((counter, Coord(8,0)))

        # add tables
        table = Table()
        right_chair = RightChair()
        left_chair = LeftChair()
        bottom_chair = BottomChair()
        top_chair = TopChair()

        objects.append((table, Coord(12,12)))
        objects.append((table, Coord(9,12)))
        objects.append((table, Coord(6,12)))
        objects.append((table, Coord(7,7)))
        objects.append((table, Coord(6,7)))
        
        objects.append((right_chair, Coord(12,13)))
        objects.append((right_chair, Coord(9,13)))
        objects.append((right_chair, Coord(5,14)))
        objects.append((right_chair, Coord(7,8)))
        objects.append((right_chair, Coord(6,8)))

        objects.append((left_chair, Coord(12,11)))
        objects.append((left_chair, Coord(9,11)))
        objects.append((left_chair, Coord(6,11)))
        objects.append((left_chair, Coord(7,6)))
        objects.append((left_chair, Coord(6,6)))

        objects.append((bottom_chair, Coord(13,12)))
        objects.append((bottom_chair, Coord(10,12)))
        objects.append((bottom_chair, Coord(7,12)))
        objects.append((bottom_chair, Coord(8,7)))

        objects.append((top_chair, Coord(11,12)))
        objects.append((top_chair, Coord(8,12)))
        objects.append((top_chair, Coord(5,13)))
        objects.append((top_chair, Coord(5,7)))

        # add the bookshelves and carpet near the Scholar 
        bookshelf = Bookshelf()
        carpet = Carpet()
        objects.append((bookshelf, Coord(0,0)))
        objects.append((bookshelf, Coord(0,1)))
        objects.append((bookshelf, Coord(0,2)))
        objects.append((carpet, Coord(2,1)))

        blacktable = BlackTable()
        objects.append((blacktable, Coord(2,4)))
        objects.append((blacktable, Coord(4,4)))

        # add the armorstand to the corner w/ the Adventurer
        armorstand = Armorstand()
        chest = Chest()
        objects.append((armorstand, Coord(0, 14)))
        objects.append((chest, Coord(1, 10)))    

        #add the trophy & the carpet
        trophycarpet = TrophyCarpet()
        objects.append((trophycarpet, Coord(2,10)))

        trophy = Trophy(self.tavern, self.artifactFactory)
        objects.append((trophy, Coord(2,11)))

        # add the tavernkeeper
        objects.append((tavernkeeper, Coord(10, 0))) 

        # add the adventurer
        adventurer = Adventurer(self.tavern, self.wrapper, self.interactFactory)
        objects.append((adventurer, Coord(2, 12)))

        # add the scholar
        scholar = Scholar(tavern=self.tavern, wrapper=self.wrapper)
        objects.append((scholar, Coord(1, 1)))

        # add the poet
        poet = Poet(self.tavern,self.wrapper, self.responseFactory)
        objects.append((poet, Coord(6, 0)))

        # add the crush
        crush = Crush(self.tavern, self.wrapper, self.interactFactory, self.responseFactory)
        objects.append((crush, Coord(7, 13)))
        
        self.npcs = {
            "Scholar": scholar,
            "Poet": poet
        }

        return objects
    