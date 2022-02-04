from abc import ABC, abstractmethod


class Operation(ABC):

    number: int
    name: str


    @abstractmethod
    def remove_item(self):
        pass

    @abstractmethod
    def buzzer_rings_when(self):
        pass
