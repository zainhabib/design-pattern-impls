from behavioral.observer.event import Event


class PropertyObservable:
    def __init__(self):
        self.property_changed = Event()
