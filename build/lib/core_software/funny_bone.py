from .operation import Operation


class FunnyBone(Operation):

    def __init__(self):
        self.name = "Funny Bone"


    def buzzer_rings_when(self):
        if self.number*2/3 > 5:
            print("BUZZZZZZ!!!!!!!!!!!")
            print("You failed! Try again")
        else:
            print("You extracted the funny bone successfully")