from .NPCStrategy import NPCStrategy

class CrushStrategy(NPCStrategy):

    def __init__(self, tavern, wrapper):

        self.tavern = tavern
        self.wrapper = wrapper


    def interact(self, poem: str) -> str:
        """
        Takes as input the poem and gives a response.
        """       
        
        if poem == None:            
            return "Go away, please. You don't seem to have anything to say to me."
        
        else:
            return self._read_poem(poem)


    def _read_poem(self, poem: str) -> str:
        """
        Read a poem using the API
        """

        prompt = f"""
            You are a sarcastic and tired women in a midieval tavern where another regular has a crush on you and recites you poems.
            You're tired of hearing them but you're not rude enough to tell him to stop. 
            Give a sarcastic, rude response rating the poem provided and do not exceed 20 words.
            Poem provided: {poem}"""
            

        # Gets a response that should be very creative w/ repetition average
        response = self.wrapper.get_response(prompt, 0.2, 0.5, 0.5)

        return response

