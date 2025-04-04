from .NPCStrategy import NPCStrategy

class PoetStrategy(NPCStrategy):

    def __init__(self, tavern, wrapper):

        self.tavern = tavern
        self.wrapper = wrapper


    def interact(self, theme: str) -> str:
        """
        Takes as input the theme the user asked and if the NPC is able to be spoken to he will return a poem. 
        """
        assert theme != "", "No theme was provided"
        
        return self._write_poem(theme)


    def _write_poem(self, theme: str) -> str:
        """
        Creates a poem with the provided theme using the API
        """

        prompt = f"""STRICTLY FOLLOW ALL INSTRUCTIONS.
        Write a 4 line poem with AT MOST 5 WORDS PER LINE.
        You are the Poet, who is silly and hopelessly romantic individual in a midieval tavern who has been reciting poems to your crush to win her over, to no avail.
        You have decided to get some help from another guest, suggesting you write a funny love poem about: {theme}.
        DO NOT EXCEED 5 WORDS PER LINE"""

        # Gets a response that should be very creative w/ repetition average
        poem = self.wrapper.get_response(prompt, 0.2, 0.5, 0.5)
    
        return poem

