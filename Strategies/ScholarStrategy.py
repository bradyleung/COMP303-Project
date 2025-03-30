from .NPCStrategy import NPCStrategy

class ScholarStrategy(NPCStrategy):

    def __init__(self, tavern, wrapper):

        self.tavern = tavern
        self.wrapper = wrapper

        # Set the Scholar as an observer of the TavernEnvironment
        self.tavern.add_observer(self)
        self._is_unlocked = False


    def interact(self, question: str) -> str:
        """
        Takes as input the question the user asked and if the NPC is able to be spoken to will answer it.
        """
        assert question != "", "No question was asked"
        
        if not self._is_unlocked: 
            return "I do not answer questions from strangers..."
        
        else:
            return self._answer_question(question)


    def update(self, event: str):
        """ 
        Reacts to any events from the TavernEnvironment to become interactable
        """

        if (event == "Scholar"):
            self._is_unlocked = True
            print("Scholar has been unlocked")


    def _answer_question(self, question: str) -> str:
        """
        Answers the question using the APIWrapper
        """

        prompt = (
            f"You're the Scholar, who is a cryptic and mysterious individual who knows the answers to all questions, or at least pretends to know."
            f"The guest has asked the question: {question}. Answer cryptically in less than 30 words."
        )

        # Gets a response that should be slightly telegraphed w/ repetition allowed
        return self.wrapper.get_response(prompt, 0.4, 0.2, 0.2)
