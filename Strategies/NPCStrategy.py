from abc import ABC, abstractmethod

class NPCStrategy(ABC):
    """Abstract interface to be implemented so I can use the Strategy pattern for my NPCs"""

    @abstractmethod
    def interact(self, input: str) -> str:
        pass