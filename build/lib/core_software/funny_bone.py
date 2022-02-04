from .operation import Operation


class FunnyBone(Operation):

    def __init__(self, number):
        self.name = "funny bone"
        self.number = number

    def remove_item(self):
        print("removing funny bone")
        self.buzzer_rings_when()

    def buzzer_rings_when(self):
        if self.number*2/3 > 5:
            print("BUZZZZZZ!!!!!!!!!!!")
            print("You failed! Try again")
        else:
            print("You extracted the funny bone successfully")