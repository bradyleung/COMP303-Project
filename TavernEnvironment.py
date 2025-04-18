class TavernEnvironment:
    """Singleton class managing tavern artifacts and their descriptions."""
    _instance = None

    def __new__(cls):
        """Creates or returns the singleton instance with initialized artifacts."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        """Initializes all the artifacts w/ default values."""
        self.artifacts = {
            "skull": "It appears to be mysterious skull of unknown origin",
            "dragonhead": "There is a large mounted head of a young dragon", 
            "feather": "There is a giant feather from from a seemingly large creature",
            "orb": "It appears to be some sort of mysterious orb pulsing with magical energy"
            }

        self.current_artifact: str = "skull"
    
    def set_artifact(self, artifact: str):
        """Sets the currently active artifact."""
        self.current_artifact = artifact

    def get_artifact(self) -> str:
        """Returns the currently active artifact's key(name)."""
        return self.current_artifact
    
    def get_artifact_description(self) -> str:
        """Returns the description of the currently active artifact."""
        return self.artifacts.get(self.current_artifact)

