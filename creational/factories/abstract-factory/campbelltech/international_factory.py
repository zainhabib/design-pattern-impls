from abc import ABC, abstractmethod
from language import Language
from capital_city import CapitalCity


# Abstract Factory
class InternationalFactory(ABC):
    @abstractmethod
    def create_language(self) -> Language:
        pass

    @abstractmethod
    def create_capital_city(self) -> CapitalCity:
        pass