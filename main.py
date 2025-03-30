# from .APIWrapper import APIWrapper
# from .TavernEnvironment import TavernEnvironment
# from .Strategies import *

# def main():
#     # Initialize Singletons
#     wrapper = APIWrapper()
#     tavern = TavernEnvironment()
    
#     # Create the NPCs
#     tavernkeeper = TavernkeeperStrategy(tavern, wrapper)
#     adventurer = AdventurerStrategy(tavern, wrapper)


#     print(tavernkeeper.interact("Adventurer"))

#     response = adventurer.interact("Dragon Tooth")
#     print(response)


# if __name__ == "__main__":
#     main()