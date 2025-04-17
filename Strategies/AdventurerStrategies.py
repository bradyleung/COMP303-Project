from ..APIWrapper import APIWrapper
from .NPCStrategy import NPCStrategy


class RegularAdventurerStrategy(NPCStrategy):
    """ 
    Takes as input both the Singleton instances and has a private field is_unlocked to determine how its interact method works. 
    Acts as an observer on the 
    """

    def __init__(self, wrapper):
        self.wrapper = wrapper


    def interact(self, current_artifact: str) -> str:
        """
        Takes as input the current_artifact to generate a story about it using the APIWrapper 
        """
        assert current_artifact != None, "current_artifact was not passed in"
        
        prompt = (
            f"You are a boastful and loud Adventurer in a tavern who loves to tell stories about how you obtained your trophies you display. "
            f"The current trophy on display is: {current_artifact}. Make up a short ~18 word story about this trophy pretending you are him speaking to me."
        )

        print(prompt)

        # Gets a response that should be unpreditable without repeating itself
        return self.wrapper.get_response(prompt, 0.2, 0.8, 0.8)

 
class NostalgicAdventurerStrategy(NPCStrategy):
    """ 
    Takes as input both the Singleton instances and has a private field is_unlocked to determine how its interact method works. 
    Acts as an observer on the 
    """

    def __init__(self, wrapper):
        self.wrapper = wrapper


    def interact(self, current_artifact: str) -> str:
        """
        Takes as input the current_artifact to generate a story about it using the APIWrapper 
        """
        assert current_artifact != None, "current_artifact was not passed in"
        
        prompt = (
            f"You are a boastful and loud Adventurer in a midieval tavern who loves to tell nostalgic childhood stories about trophies that your family has given you. "
            f"The current trophy on display is: {current_artifact}. Make up a short ~18 word story about how you got this trophy."
        )

        print(prompt)

        # Gets a response that should be unpreditable without repeating itself
        return self.wrapper.get_response(prompt, 0.2, 0.8, 0.8)