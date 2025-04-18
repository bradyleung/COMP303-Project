from .NPCStrategy import NPCStrategy

class CrushStrategy(NPCStrategy):
    """Strategy for a sarcastic NPC responding to romantic poems."""


    def __init__(self, wrapper):
        """Initializes with an API wrapper for response generation."""
        self.wrapper = wrapper


    def interact(self, poem: str) -> str:
        """Generates a sarcastic response to the given poem (max 20 words)."""

        prompt = f"""
            You are a sarcastic and tired women in a midieval tavern where another regular has a crush on you and recites you poems.
            You're tired of hearing them but you're not rude enough to tell him to stop. 
            Give a sarcastic, rude response rating the poem provided and do not exceed 20 words.
            Poem provided: {poem}"""
            

        # Gets a response that should be very creative w/ repetition average
        response = self.wrapper.get_response(prompt, 0.2, 0.5, 0.5)

        return response

