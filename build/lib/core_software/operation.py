from abc import ABC, abstractmethod


class Operation(ABC):

    number: int
    name: str

    @abstractmethod
    def remove_item(self, number):
        print(f"Removing {self.name}")
        self.number = number
        self.buzzer_rings_when()

    @abstractmethod
    def buzzer_rings_when(self):
        raise NotImplementedError
