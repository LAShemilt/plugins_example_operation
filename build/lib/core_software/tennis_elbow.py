from .operation import Operation

class TennisElbow:
    def __init__(self):
        self.name="Tennis Elbow"


    def buzzer_goes_when(self):
        if (self.number - 5) <= 0:
            print("BZZZZZZZZ!!!!!!")
            print("Ooops! You missed. Please try again.")
        else:
            print("You have successfully removed the Tennis Elbow")

