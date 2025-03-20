from NPCStrategy import NPCStrategy
from TavernEnvironment import TavernEnvironment
from APIWrapper import APIWrapper

class CrushStrategy(NPCStrategy):

    def __init__(self, tavern: TavernEnvironment, wrapper: APIWrapper):

        self.tavern = tavern
        self.wrapper = wrapper

        # Set the Crush as an observer of the TavernEnvironment
        self.tavern.add_observer(self)
        self._is_unlocked = False


    def interact(self, poem: str) -> str:
        """
        Takes as input the poem the user asked and if the NPC is able to be spoken to he will return a poem. 
        """        
        if not self._is_unlocked: 
            return "You should talk with the Tavernkeeper first! He'll catch you up to speed."
        
        elif poem == "":
            return "Please go talk to the Poet instead!"
        
        else:
            return self._read_poem(poem)


    def update(self, event: str):
        """ 
        Reacts to any events from the TavernEnvironment to become interactable
        """

        if (event == "Crush"):
            self._is_unlocked = True
            print("Crush has been unlocked")


    def _read_poem(self, poem: str) -> str:
        """
        Read a poem using the API
        """

        print(f"The poem provided was: {poem}")

        prompt = (
            f"You're in a midieval tavern and this man wrote a poem about you. State your opinion about it and be critical: {poem}."
            f"If its thought it was good begin your response with a 1, if you thought it was bad start with a 0, then give your response in 40 words."
        )

        # Gets a response that should be very creative w/ repetition average
        response = self.wrapper.get_response(prompt, 1.0, 0.5, 0.5)

        rating = response[0]
        print (f"The rating is: {rating}")
        response = response[1:]

        return response

