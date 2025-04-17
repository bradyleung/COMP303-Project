from abc import ABC, abstractmethod

class NPCStrategy(ABC):
    
    @abstractmethod
    def interact(self, input: str) -> str:
        pass