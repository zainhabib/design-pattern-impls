from abc import ABC, abstractmethod


# Abstract Product B
class CapitalCity(ABC):
    def get_population(self) -> int:
        pass

    def list_top_attractions(self) -> []:
        pass