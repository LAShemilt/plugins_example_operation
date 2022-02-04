from .funny_bone import FunnyBone
from .tennis_elbow import TennisElbow
from random import randint

def play_operation():

     # select number
     num = int(input("Type in a number between 1-10:"))
     print("Your number is :", num)

     # Select
     print("try to remove the funny bone")
     trigger = randint(0 , 1)

     operations = [FunnyBone, TennisElbow]
     operations[trigger].remove_item()


if __name__ == "__main__":
    play_operation()