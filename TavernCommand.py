# Imports
from .imports import *
from .Strategies import *

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from message import Message, DialogueMessage
    from command import MenuCommand


class NPC_Command(MenuCommand):
    """
    Contructor takes as input the string input for the interaction strategy and the interaction strategy 
    and returns the message(s) to the user through a DialogueMessage
    """

    # Command factory design 
    def __init__(self, option: str, interact_strategy: NPCStrategy):
        self.option = option
        self.interact_strategy = interact_strategy

    # Implementing the execute function for this MenuCommand
    def execute(self, context, player) -> list[Message]:
 
        return [DialogueMessage(
            sender = self, 
            recipient = player,
            text = self.interact_strategy.interact(self.option),
            image = 'snow'
        )]
    
