from .Strategies import NPCStrategy

class EventManager:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer: NPCStrategy):
        self.observers.append(observer)

    def notify_observers(self, event: str):
        for observer in self.observers:
            observer.update(event)

    