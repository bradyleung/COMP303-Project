from NPCStrategy import NPCStrategy
from TavernEnvironment import TavernEnvironment
from APIWrapper import APIWrapper

class PoetStrategy(NPCStrategy):

    def __init__(self, tavern: TavernEnvironment, wrapper: APIWrapper):

        self.tavern = tavern
        self.wrapper = wrapper

        # Set the Poet as an observer of the TavernEnvironment
        self.tavern.add_observer(self)
        self._is_unlocked = False


    def interact(self, theme: str) -> str:
        """
        Takes as input the theme the user asked and if the NPC is able to be spoken to he will return a poem. 
        """
        assert theme != "", "No theme was provided"
        
        if not self._is_unlocked: 
            return "Why would I trust you to help me out? You might steal my work!"
        
        else:
            return self._write_poem(theme)


    def update(self, event: str):
        """ 
        Reacts to any events from the TavernEnvironment to become interactable
        """

        if (event == "Poet"):
            self._is_unlocked = True
            print("Poet has been unlocked")


    def _write_poem(self, theme: str) -> str:
        """
        Creates a poem with that theme using the API
        """

        prompt = (
            f"You're the Poet, who is silly and hopelessly romantic individual who has been writing poems to his crush to try to win her over"
            f"You asked the guest for a theme and they told you to write a less than 40 word love poem about: {theme}."
        )

        # Gets a response that should be very creative w/ repetition average
        poem = self.wrapper.get_response(prompt, 1.0, 0.5, 0.5)

        self.tav2ern.set_poem(poem)
    
        return poem

