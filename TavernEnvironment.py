from GameState import GameState
from EventManager import EventManager
from NPCStrategy import NPCStrategy

class TavernEnvironment:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        self.game_state = GameState()  # Delegate game state management
        self.event_manager = EventManager()  # Delegate event management

    def unlock_npc(self, npc_name: str):
        self.game_state.unlock_npc(npc_name)
        self.event_manager.notify_observers(npc_name)

    def set_artifact(self, artifact: str):
        self.game_state.set_artifact(artifact)
        self.event_manager.notify_observers(f"artifact_changed:{artifact}")

    def get_artifact(self) -> str:
        return self.game_state.get_artifact()

    def add_observer(self, observer: NPCStrategy):
        self.event_manager.add_observer(observer)

    def set_poem(self, poem: str):
        self.game_state.set_poem(poem)

    def get_poem(self) -> str:
        return self.game_state.get_poem()