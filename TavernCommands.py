# Imports
from .imports import *
from .Strategies import *
from .TavernEnvironment import TavernEnvironment
from .Enums import PlayerState, NPCNames

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from message import Message, DialogueMessage, ChatMessage
    from command import MenuCommand
    from Player import HumanPlayer

class InteractCommand(MenuCommand):
    """
    Contructor takes as input the string input for the interaction strategy and the interaction strategy 
    and returns the message(s) to the user through a DialogueMessage.
    """
    
    def __init__(self, option: str, interact_strategy: NPCStrategy):
        self.option = option
        self.interact_strategy = interact_strategy

    # Implementing the execute function for this MenuCommand
    def execute(self, context, player) -> list[Message]:
        talking_to = player.get_state(PlayerState.TALKING_TO.value)
        
        # Check if it's the crush to get the player's last generated poem 
        if talking_to == NPCNames.CRUSH.value:
            self.option = player.get_state(PlayerState.POEM.value)

        response = self.interact_strategy.interact(self.option)

        # Post interaction state changes
        if talking_to == NPCNames.POET.value:
            player.set_state(PlayerState.POEM.value, response)

        # Get current state (handle and handle None/empty cases)
        if talking_to == NPCNames.TAVERNKEEPER.value:
            unlocked_npcs = player.get_state(PlayerState.UNLOCKED_NPCS.value, list())

            if self.option not in unlocked_npcs:
                unlocked_npcs.append(self.option)
            
            player.set_state(PlayerState.UNLOCKED_NPCS.value, unlocked_npcs)
        
        # Remove the state of who they're talking to after executing. 
        player.set_state(PlayerState.TALKING_TO.value, None)

        return [DialogueMessage(
            sender = self, 
            recipient = player,
            text = response,
            image = 'snow'
        )]
    
class PoetYesCommand(MenuCommand):

    def execute(self, context, player: HumanPlayer):
        return [DialogueMessage(
            sender = self, 
            recipient = player,
            text = "Awesome! Although, I'm not sure what to say. Tell me a theme to write about using /theme! ",
            image = 'snow'
        ),DialogueMessage(
            sender = self, 
            recipient = player,
            text = "Also, she seems to have barricaded herself behind those tables... so uh, you'll have to go tell it to her ... she's scary.",
            image = 'snow')
        ]
        
class PoetNoCommand(MenuCommand):

    def execute(self, context, player: HumanPlayer):
        
        player.set_state("talking_to", None)

        return [DialogueMessage(
            sender = self, 
            recipient = player,
            text = "That's fine... it probably wouldn't have worked anyway...",
            image = 'snow'
        )]
    
class CrushNoCommand(MenuCommand):

    def execute(self, context, player: HumanPlayer):
        
        player.set_state("talking_to", None)

        return [DialogueMessage(
            sender = self, 
            recipient = player,
            text = "Good decision. I sincerely thank you.",
            image = 'snow'
        )]

class ChangeArtifactCommand(MenuCommand):

    def __init__(self, artifact: MapObject, newArtifact: str, tavern: TavernEnvironment):
        self.artifact = artifact
        self.newArtifact = newArtifact
        self.tavern = tavern

    def execute(self, context, player: HumanPlayer):
        
        # Update the image and the tavern itself
        self.artifact.set_image_name(f'tile/int_decor/{self.newArtifact}')
        pos = self.artifact.get_position()
        self.tavern.set_artifact(self.newArtifact)

        context.remove_from_grid(self.artifact, pos)
        context.add_to_grid(self.artifact, pos)

        context.send_grid_to_players()

        return [DialogueMessage(
            sender = self, 
            recipient = player,
            text = "Successfully changed artifacts!",
            image = 'snow'
        )]


# Create CommandFactory classes to decouple NPCs from Commands
class InteractCommandFactory:
    def create(self, option: str, strategy: NPCStrategy) -> InteractCommand:
        return InteractCommand(option, strategy)
    
class ChangeArtifactFactory:
    def create(self, artifact: MapObject, newArtifact: str, tavern: TavernEnvironment) -> InteractCommand:
        return ChangeArtifactCommand(artifact, newArtifact, tavern)

class YesNoCommandFactory:

    @staticmethod
    def create_poet_yes() -> PoetYesCommand:
        return PoetYesCommand()
    
    @staticmethod
    def create_poet_no() -> PoetNoCommand:
        return PoetNoCommand()
    
    @staticmethod
    def create_crush_no() -> CrushNoCommand:
        return CrushNoCommand()

