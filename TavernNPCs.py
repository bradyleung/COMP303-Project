from .imports import *
from .TavernEnvironment import TavernEnvironment
from .APIWrapper import APIWrapper
from .Strategies import *
from .TavernCommands import *
from .Enums import PlayerState, NPCNames

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
    
    def __init__(self, tavern: TavernEnvironment, wrapper: APIWrapper, interact_factory: InteractCommandFactory):
        
        self.tavern = tavern
        self.wrapper = wrapper
        self.strategy = TavernkeeperStrategy(tavern, wrapper)

        menu_options = {
            "The Adventurer": interact_factory.create(NPCNames.ADVENTURER.value, self.strategy),
            "The Scholar": interact_factory.create(NPCNames.SCHOLAR.value, self.strategy),
            "The Poet": interact_factory.create(NPCNames.POET.value, self.strategy),
            "The Crush": interact_factory.create(NPCNames.CRUSH.value, self.strategy)
        }

        super().__init__(
            name="Tavernkeeper",
            image="tavernkeeper",
            encounter_text="Welcome to my Tavern! I'd love to introduce you to my loyal patrons, who would ya like to get to know?",
            facing_direction="right",
            staring_distance = 0,
            bg_music='',
        )

        self.__menu_name = "Which NPC would you wish to learn about?"
        self.__menu_options = menu_options


    def select_option(self, player: "HumanPlayer", option: str) -> list[Message]:
        return self.__menu_options[option].execute(player.get_current_room(), player=player)
    

    # Method for when the player interacts with the Tavernkeeper
    def player_interacted(self, player: "HumanPlayer") -> list[Message]:
        player.set_state(PlayerState.TALKING_TO.value, NPCNames.TAVERNKEEPER.value)
        player.set_current_menu(self)

        return [DialogueMessage(self, player, self._NPC__encounter_text, self.get_image_name()),
                 MenuMessage(self, player, self.__menu_name, list(self.__menu_options))]
 

########################################################################################################
class Adventurer(NPC):

    def __init__(self, tavern: TavernEnvironment, wrapper: APIWrapper, interact_factory: InteractCommandFactory):

        self.tavern = tavern
        self.wrapper = wrapper
        self.interact_factory=interact_factory
        self.strategy = AdventurerStrategy(tavern, wrapper)

        super().__init__(
            name="Adventurer",
            image="player10",
            encounter_text="As you see, I have my impressive trophies next to me each with impressive stories. You can em change out by interacting with them!.",
            facing_direction="down",
            staring_distance = 0,
            bg_music='',
        )

    def player_interacted(self, player: "HumanPlayer") -> list[Message]:

        unlocked_npcs = player.get_state(PlayerState.UNLOCKED_NPCS.value)
        if NPCNames.ADVENTURER.value not in unlocked_npcs:
            return [ChatMessage(
                sender = self, 
                recipient = player,
                text = "You have not yet unlocked the Adventurer. Speak to the Tavernkeeper to unlock them.",
            )]  
        
        player.set_state(PlayerState.TALKING_TO.value, NPCNames.ADVENTURER.value)

        command = self.interact_factory.create(self.tavern.get_artifact(), self.strategy)
        messages = command.execute(player.get_current_room(), player)

        messages.append(DialogueMessage(
            sender=self, 
            recipient=player, 
            text=self._NPC__encounter_text, 
            image=self.get_image_name()))

        return messages
        
    
########################################################################################################
class Scholar(NPC):

    def __init__(self, tavern: TavernEnvironment, wrapper: APIWrapper):

        self.tavern = tavern
        self.wrapper = wrapper
        self.strategy = ScholarStrategy(tavern, wrapper)

        super().__init__(
            name="Scholar",
            image="scholar",
            encounter_text="Ah... so you seek the one they whisper of in shadowed halls... the Scholar.",
            facing_direction="down",
            staring_distance = 0,
            bg_music='',
        )


    def player_interacted(self, player: "HumanPlayer") -> list[Message]:

        unlocked_npcs = player.get_state(PlayerState.UNLOCKED_NPCS.value)
        if NPCNames.SCHOLAR.value not in unlocked_npcs:
            return [ChatMessage(
                sender = self, 
                recipient = player,
                text = "You have not yet unlocked the Scholar. Speak to the Tavernkeeper to unlock them.",
            )]  

        player.set_state(PlayerState.TALKING_TO.value, NPCNames.SCHOLAR.value)

        unlocked_text = "Names are but fleeting echoes, yet knowledge... knowledge endures. The path to truth begins with /ask... then enter return on this menu."

        player.set_current_menu(self)
        return [DialogueMessage(
            sender=self, 
            recipient=player, 
            text=self._NPC__encounter_text, 
            image=self.get_image_name(), 
            press_enter=False),
                DialogueMessage(
            sender=self, 
            recipient=player, 
            text=unlocked_text, 
            image=self.get_image_name(),
            press_enter=True),
        ]

########################################################################################################
class Poet(NPC, SelectionInterface):

    def __init__(self, tavern: TavernEnvironment, wrapper: APIWrapper, yesno_factory: YesNoCommandFactory):

        self.tavern = tavern
        self.wrapper = wrapper
        self.strategy = PoetStrategy(tavern, wrapper)

        super().__init__(
            name="Poet",
            image="poet",
            encounter_text="I'm stuck! My crush deserves perfect words... but I can't think of what to say. Can you help me out?",
            facing_direction="right",
            staring_distance = 0,
            bg_music='',
        )

        menu_options = {
            "Yes!": yesno_factory.create_poet_yes(),
            "No...": yesno_factory.create_poet_no()
        }

        self.__menu_name = "Will you help out the Poet?"
        self.__menu_options = menu_options
    
    def select_option(self, player: "HumanPlayer", option: str) -> list[Message]:
        return self.__menu_options[option].execute(player.get_current_room(), player=player)

    def player_interacted(self, player: "HumanPlayer") -> list[Message]:
        
        unlocked_npcs = player.get_state(PlayerState.UNLOCKED_NPCS.value)
        if NPCNames.POET.value not in unlocked_npcs:
            return [ChatMessage(
                sender = self, 
                recipient = player,
                text = "You have not yet unlocked the Poet. Speak to the Tavernkeeper to unlock them.",
            )]  

        player.set_state(PlayerState.TALKING_TO.value, NPCNames.POET.value)

        player.set_current_menu(self)

        return[DialogueMessage(self, player, self._NPC__encounter_text, self.get_image_name()),
            MenuMessage(self, player, self.__menu_name, list(self.__menu_options))   
        ]


##############################################xw##########################################################
class Crush(NPC, SelectionInterface):

    def __init__(self, tavern: TavernEnvironment, wrapper: APIWrapper, interact_factory: InteractCommandFactory, yesno_factory: YesNoCommandFactory):

        self.tavern = tavern
        self.wrapper = wrapper
        self.strategy = CrushStrategy(tavern, wrapper)

        super().__init__(
            name="Crush",
            image="crush",
            encounter_text="Oh, you're not ... him, are you? Please tell me he has a messenger now...\nDo you have something to tell me?..",
            facing_direction="down",
            staring_distance = 0,
            bg_music='',
        )

        menu_options = {
            "Yes": interact_factory.create("", self.strategy),
            "No": yesno_factory.create_crush_no()
        }

        self.__menu_name = "Retell the poem to his crush?"
        self.__menu_options = menu_options

    
    def select_option(self, player: "HumanPlayer", option: str) -> list[Message]:
        return self.__menu_options[option].execute(player.get_current_room(), player=player)


    def player_interacted(self, player: "HumanPlayer") -> list[Message]:
        
        unlocked_npcs = player.get_state(PlayerState.UNLOCKED_NPCS.value)
        if NPCNames.CRUSH.value not in unlocked_npcs:
            return [ChatMessage(
                sender = self, 
                recipient = player,
                text = "You have not yet unlocked the Crush. Speak to the Tavernkeeper to unlock them.",
            )]  
        
        if player.get_state(PlayerState.POEM.value) == None:
            text = "Wait... you don't actually have anything to tell me, do you? If that poet didn't put you up to this what are you doing here? Skedaddle."   
            return DialogueMessage(self, player, text, self.get_image_name())

        
        player.set_state(PlayerState.TALKING_TO.value, NPCNames.CRUSH.value)

        player.set_current_menu(self)

        return[DialogueMessage(self, player, self._NPC__encounter_text, self.get_image_name()),
            MenuMessage(self, player, self.__menu_name, list(self.__menu_options))   
        ]

################################################################################################
##Treating this as an NPC as I have all my interactable objects here
class Trophy(MapObject, SelectionInterface):
    """An interactable trophy that can switch between different artifacts."""
    
    def __init__(self, tavern: TavernEnvironment, factory: ChangeArtifactFactory):
        super().__init__(f'tile/int_decor/skull', passable=False, z_index=0)
        self.tavern = tavern
        self.__menu_name = "Select an artifact to display:"
    
        self.__menu_options = {
            "An Unknown Skull": factory.create(self, "skull", tavern),
            "A Dragon's Head": factory.create(self, "dragonhead", tavern),
            "A Giant Feather": factory.create(self, "feather", tavern),
            "A Magical Orb": factory.create(self, "orb", tavern)
        }


    def select_option(self, player: "HumanPlayer", option: str) -> list[Message]:
        return self.__menu_options[option].execute(player.get_current_room(), player=player)
        

    # Method for when the player interacts with the Object
    def player_interacted(self, player: "HumanPlayer") -> list[Message]:
    
        description = self.tavern.get_artifact_description()

        player.set_current_menu(self)

        return [DialogueMessage(self, player, f"{description}. You are given the option to change the artifact.", self.get_image_name()),
                 MenuMessage(self, player, self.__menu_name, list(self.__menu_options))]