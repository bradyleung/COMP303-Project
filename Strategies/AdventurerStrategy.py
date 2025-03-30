from .NPCStrategy import NPCStrategy

class AdventurerStrategy(NPCStrategy):
    """ 
    Takes as input both the Singleton instances and has a private field is_unlocked to determine how its interact method works. 
    Acts as an observer on the 
    """

    def __init__(self, tavern, wrapper):
        self.tavern = tavern
        self.wrapper = wrapper

        # Set the Adventurer as an observer of the TavernEnvironment
        self.tavern.add_observer(self)
        self._is_unlocked = False


    def interact(self, current_artifact: str) -> str:
        """
        Takes as input the current_artifact and if the NPC is able to be spoken to will generate a story about the current trophy on display. 
        """
        assert current_artifact != None, "current_artifact was not passed in"
        
        if not self._is_unlocked: 
            return "Stay away from me and my precious trophies until you speak to the Tavernkeeper!"
        
        else:
            return self._generate_story(current_artifact)


    def update(self, event: str):
        """ 
        Reacts to any events from the TavernEnvironment to become interactable
        """

        if (event == "Adventurer"):
            self._is_unlocked = True
            print("Adventurer has been unlocked")


    def _generate_story(self, current_artifact: str) -> str:
        """
        Generates a story using the APIWrapper and the current_artifact if he is unlocked
        """

        prompt = (
            f"You are a boastful and loud Adventurer in a tavern who loves to tell stories about you obtained your trophies you display. "
            f"The current trophy on display is: {current_artifact}. Make up a short ~50 word story about this trophy."
        )

        # Gets a response that should be unpreditable without repeating itself
        return self.wrapper.get_response(prompt, 1.0, 0.8, 0.8)