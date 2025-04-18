from .NPCStrategy import NPCStrategy
from ..APIWrapper import APIWrapper

class GoodPoetStrategy(NPCStrategy): 
    """Attempts to generate a more serious poem given the theme provided."""

    def __init__(self, wrapper):
        """Initialized with an API wrapper for the poem generation."""
        self.wrapper = wrapper


    def interact(self, theme: str) -> str:
        """Creates a 4 line love poem about the specified theme."""

        assert theme != "", "No theme was provided"

        prompt = f"""STRICTLY FOLLOW ALL INSTRUCTIONS.
        Write a 4 line poem with AT MOST 5 WORDS PER LINE.
        You are the Poet, who is a hopelessly romantic individual in a midieval tavern who has been reciting poems to try to win over your crush, without success. 
        You have decided to get some help from another guest, suggesting you write a serious love poem about: {theme}.
        DO NOT EXCEED 5 WORDS PER LINE"""

        # Gets a response that should be very creative w/ repetition average
        poem = self.wrapper.get_response(prompt, 0.2, 0.5, 0.5)
    
        return poem
    

class FunnyPoetStrategy(NPCStrategy): 
    """Generates a more humorous poem based on a given theme."""


    def __init__(self, wrapper): 
        """Initializes with an API wrapper for poem generation."""
        self.wrapper = wrapper


    def interact(self, theme: str) -> str:
        """Creates a 4 line funny love poem about the specified theme."""

        assert theme != "", "No theme was provided"

        prompt = f"""STRICTLY FOLLOW ALL INSTRUCTIONS.
        Write a 4 line poem with AT MOST 5 WORDS PER LINE.
        You are the Poet, who is a hopelessly silly and romantic individual in a midieval tavern who has been reciting poems to try to win over your crush, without success. 
        You have decided to get some help from another guest, suggesting you write a funny love poem about: {theme}.
        DO NOT EXCEED 5 WORDS PER LINE"""

        # Gets a response that should be very creative w/ repetition average
        poem = self.wrapper.get_response(prompt, 0.2, 0.5, 0.5)
    
        return poem
