from core_software.operation import Operation

class TennisElbow(Operation):
    def __init__(self):
        self.name ="Tennis Elbow"

    def buzzer_rings_when(self):
        if (self.number - 5) <= 0:
            print("BZZZZZZZZ!!!!!!")
            print("Ooops! You missed. Please try again.")
        else:
            print("You have successfully removed the Tennis Elbow")

