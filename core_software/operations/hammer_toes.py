from ..operation import Operation


class HammerToes(Operation):

    def __init__(self):
        self.name = "Hammer Toes"

    def buzzer_rings_when(self):
        if self.number**2 >= 25:
            print("BUZZZZZZ!!!!!!!!!!!")
            print("No luck this time! Try again")
        else:
            print("You extracted the Hammer Toes successfully")