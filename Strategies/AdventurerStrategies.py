from ..APIWrapper import APIWrapper
from .NPCStrategy import NPCStrategy


class RegularAdventurerStrategy(NPCStrategy):
    """Strategy for a boastful adventurer generating stories about the artifacts."""

    def __init__(self, wrapper):
        """Initializes with an API wrapper for story generation."""
        self.wrapper = wrapper


    def interact(self, current_artifact: str) -> str:
        """Generates a short prideful story about the given artifact."""
        assert current_artifact != None, "current_artifact was not passed in"
        
        prompt = (
            f"You are a boastful and loud Adventurer in a tavern who loves to tell stories about how you obtained your trophies you display. "
            f"The current trophy on display is: {current_artifact}. Make up a short ~18 word story about this trophy pretending you are him speaking to me."
        )

        print(prompt)

        # Gets a response that should be unpreditable without repeating itself
        return self.wrapper.get_response(prompt, 0.2, 0.8, 0.8)

 
class NostalgicAdventurerStrategy(NPCStrategy):
    """Strategy for a nostalgic adventurer generating childhood artifact stories."""

    def __init__(self, wrapper):
        """Initializes with an API wrapper for story generation."""
        self.wrapper = wrapper


    def interact(self, current_artifact: str) -> str:
        """Generates a short nostalgic story about the given artifact."""
        
        assert current_artifact != None, "current_artifact was not passed in"
        
        prompt = (
            f"You are a boastful and loud Adventurer in a midieval tavern who loves to tell nostalgic childhood stories about trophies that your family has given you. "
            f"The current trophy on display is: {current_artifact}. Make up a short ~18 word story about how you got this trophy."
        )

        print(prompt)

        # Gets a response that should be unpreditable without repeating itself
        return self.wrapper.get_response(prompt, 0.2, 0.8, 0.8)