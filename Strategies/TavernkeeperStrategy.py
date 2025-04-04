from .NPCStrategy import NPCStrategy

class TavernkeeperStrategy(NPCStrategy):

    def __init__(self, wrapper):
        self.wrapper = wrapper
       
        # Tavernkeeper gets a dictionary to store the descriptions of each customer to be able to describe them
        self._descriptions = {
        "Adventurer": "The Adventurer is a boastful and loud individual who loves to tell tales of the artifacts he displays in the tavern.",
        "Scholar": "The Scholar is a cryptic and mysterious individual who knows the answers to all questions past or present, or at least pretends to know.",
        "Poet": "The poet is a silly and hopelessly romantic individual who has been writing poems to his crush to try to win her over.",
        "Crush": "The poet's crush is a rude and sarcastic individual who is tired of the Poet reading her poems every time she vists the tavern."
    }

    def interact(self, npc_name: str) -> str:
        
        prompt = f"""
            You are a playful Tavernkeeper in a midieval tavern.
            Introduce the described patron in 20 words or less by paraphrasing their description.
            Patron description: {self._descriptions.get(npc_name)}
        """

        # Gets a more fixed response that will not repeat itself
        return(self.wrapper.get_response(prompt, 0.2, 0.5, 0.5))