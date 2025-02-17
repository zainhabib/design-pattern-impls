from abc import ABC, abstractmethod


# Abstract Product A
class Language(ABC):
    @abstractmethod
    def greet(self) -> str:
        pass
