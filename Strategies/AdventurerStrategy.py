from .NPCStrategy import NPCStrategy

class AdventurerStrategy(NPCStrategy):
    """ 
    Takes as input both the Singleton instances and has a private field is_unlocked to determine how its interact method works. 
    Acts as an observer on the 
    """

    def __init__(self, tavern, wrapper):
        self.tavern = tavern
        self.wrapper = wrapper


    def interact(self, current_artifact: str) -> str:
        """
        Takes as input the current_artifact and if the NPC is able to be spoken to will generate a story about the current trophy on display. 
        """
        assert current_artifact != None, "current_artifact was not passed in"
        
        return self._generate_story(current_artifact)


    def _generate_story(self, current_artifact: str) -> str:
        """
        Generates a story using the APIWrapper and the current_artifact if he is unlocked
        """

        prompt = (
            f"You are a boastful and loud Adventurer in a tavern who loves to tell stories about you obtained your trophies you display. "
            f"The current trophy on display is: {current_artifact}. Make up a short ~18 word story about this trophy."
        )

        print(prompt)

        # Gets a response that should be unpreditable without repeating itself
        return self.wrapper.get_response(prompt, 0.2, 0.8, 0.8)