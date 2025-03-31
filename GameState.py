
class GameState:
    def __init__(self):
        self.unlocked_npcs = set()
        self.interacted_npcs = set()
        self.current_artifact = "Dragon's Claw"

    def unlock_npc(self, npc_name: str):
        self.unlocked_npcs.add(npc_name)

    def get_unlocked_npcs(self):
        return self.unlocked_npcs
    
    def interacted_with_npc(self, npc_name: str):
        self.talked_to_npcs.add(npc_name)

    def get_interacted_npcs(self):
        return self.interacted_npcs

    def set_artifact(self, artifact: str):
        self.current_artifact = artifact
        
    def get_artifact(self) -> str:
        return self.current_artifact
    
    def set_poem(self, poem: str) :
        self.poem = poem

    def get_poem(self) -> str:
        return self.poem