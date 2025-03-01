from behavioral.observer.event import Event
from behavioral.observer.property_observable import PropertyObservable


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.falls_ill = Event()

    def catch_a_cold(self):
        self.falls_ill(self.name, self.address)


class PersonObservable(PropertyObservable):
    def __init__(self, age=0):
        super().__init__()
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        old_can_vote = self.can_vote
        if self._age == value:
            return
        self._age = value
        self.property_changed("age", value)

        if old_can_vote != self.can_vote:
            self.property_changed("can_vote", self.can_vote)

    @property
    def can_vote(self) -> bool:
        return self._age >= 18
