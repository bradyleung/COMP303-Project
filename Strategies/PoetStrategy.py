from .NPCStrategy import NPCStrategy

class PoetStrategy(NPCStrategy):

    def __init__(self, wrapper):
        self.wrapper = wrapper


    def interact(self, theme: str) -> str:
        """
        Takes as input the theme the user asked for and generates a poem using the API 
        Args: The theme the user wants the Poet to write about
        Returns: A poem using that theme
        """

        assert theme != "", "No theme was provided"

        prompt = f"""STRICTLY FOLLOW ALL INSTRUCTIONS.
        Write a 4 line poem with AT MOST 5 WORDS PER LINE.
        You are the Poet, who is silly and hopelessly romantic individual in a midieval tavern who has been reciting poems to your crush to win her over, to no avail.
        You have decided to get some help from another guest, suggesting you write a funny love poem about: {theme}.
        DO NOT EXCEED 5 WORDS PER LINE"""

        # Gets a response that should be very creative w/ repetition average
        poem = self.wrapper.get_response(prompt, 0.2, 0.5, 0.5)
    
        return poem
