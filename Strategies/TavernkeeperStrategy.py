from .NPCStrategy import NPCStrategy

class TavernkeeperStrategy(NPCStrategy):

    def __init__(self, tavern, wrapper):
        self.tavern = tavern
        self.wrapper = wrapper
       
        # Tavernkeeper gets a dictionary to store the descriptions of each customer to be able to describe them
        self._descriptions = {
        "Adventurer": "The Adventurer is a boastful and loud individual who loves to tell tales of the artifacts he displays in the tavern.",
        "Scholar": "The Scholar is a cryptic and mysterious individual who knows the answers to all questions, or at least pretends to know.",
        "Poet": "The poet is a silly and hopelessly romantic individual who has been writing poems to his crush to try to win her over.",
        "Crush": "The poet's crush is a shy but friendly individual who was initially uninterested in his poems but is slowly growing to like them."
    }

    def interact(self, npc_name: str) -> str:
        
        self.tavern.unlock_npc(npc_name)

        prompt = self._descriptions.get(npc_name) + "You are a playful tavernkeeper in a midieval tavern, introduce the described patron in 40 words or less by paraphrasing their description. "

        # Gets a more fixed response that will not repeat itself
        return(self.wrapper.get_response(prompt, 0.2, 0.5, 0.5))